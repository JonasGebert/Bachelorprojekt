#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erzeugt aus dem Obsidian-Vault eine statische Dashboard-Seite (_site/index.html).

Grundsatz: Diese Datei ist ein *Betrachter*, keine zweite Datenquelle. Sie liest
ausschliesslich das YAML-Frontmatter der Notizen. Geschrieben wird nie.

Aufruf lokal:   python3 tools/build_dashboard.py
Aufruf in CI:   siehe .github/workflows/pages.yml
"""
import os, re, json, subprocess, datetime, html, sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML fehlt.  ->  pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(ROOT, "_site")
HEUTE = datetime.date.today()

SPALTEN = [("sprint-backlog", "Sprint Backlog"), ("in-arbeit", "In Arbeit"), ("erledigt", "Erledigt")]
FARBE_PERSON = {}
PALETTE = ["#4e7a63", "#5b7fa6", "#7a6a94", "#a6773f", "#8a5a6a"]


# ---------------------------------------------------------------- Hilfsfunktionen
def frontmatter(pfad):
    """Liest das YAML-Frontmatter einer Markdown-Datei. Gibt {} zurueck, wenn keins da ist."""
    try:
        txt = open(pfad, encoding="utf-8").read()
    except OSError:
        return {}
    if not txt.startswith("---\n"):
        return {}
    try:
        return yaml.safe_load(txt.split("---\n", 2)[1]) or {}
    except yaml.YAMLError:
        return {}


def alle(unterordner):
    d = os.path.join(ROOT, unterordner)
    if not os.path.isdir(d):
        return []
    return [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(".md")]


def repo_url():
    """Basis-URL fuer Edit-Links. Override per Umgebungsvariable REPO_URL."""
    if os.environ.get("REPO_URL"):
        return os.environ["REPO_URL"].rstrip("/")
    if os.environ.get("GITHUB_REPOSITORY"):
        return "https://github.com/" + os.environ["GITHUB_REPOSITORY"]
    try:
        r = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT,
                           capture_output=True, text=True, timeout=5).stdout.strip()
        r = re.sub(r"^git@github\.com:", "https://github.com/", r)
        return re.sub(r"\.git$", "", r)
    except Exception:
        return ""


def branch():
    if os.environ.get("GITHUB_REF_NAME"):
        return os.environ["GITHUB_REF_NAME"]
    try:
        return subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, timeout=5).stdout.strip() or "main"
    except Exception:
        return "main"


def farbe(person):
    if not person:
        return "#9a9791"
    if person not in FARBE_PERSON:
        FARBE_PERSON[person] = PALETTE[len(FARBE_PERSON) % len(PALETTE)]
    return FARBE_PERSON[person]


def initialen(person):
    if not person:
        return "?"
    return "".join(w[0] for w in str(person).split()[:2]).upper()


def tage_seit(datum):
    if not datum:
        return None
    if isinstance(datum, str):
        try:
            datum = datetime.date.fromisoformat(datum)
        except ValueError:
            return None
    if isinstance(datum, datetime.datetime):
        datum = datum.date()
    return (HEUTE - datum).days


# ---------------------------------------------------------------- Daten sammeln
def lies_aufgaben():
    aufgaben = []
    for p in alle("20_Backlog/Aufgaben"):
        d = frontmatter(p)
        if d.get("typ") != "aufgabe" or d.get("status") == "entfallen":
            continue
        d["_pfad"] = os.path.relpath(p, ROOT).replace(os.sep, "/")
        d["blockiert_durch"] = [re.sub(r"[\[\]]", "", str(b)) for b in (d.get("blockiert_durch") or [])]
        aufgaben.append(d)
    return aufgaben


def lies_sprints():
    s = [frontmatter(p) for p in alle("10_Projektmanagement/14_Sprints")]
    return sorted([x for x in s if x.get("typ") == "sprint"], key=lambda x: x.get("nummer", 0))


def lies_risiken():
    r = [frontmatter(p) for p in alle("60_Register/Risiken")]
    r = [x for x in r if x.get("typ") == "risiko"]
    return sorted(r, key=lambda x: -(x.get("risikozahl") or 0))


def lies_burndown():
    """Parst die Datentabelle aus dem Burndown-Datenblatt."""
    p = os.path.join(ROOT, "10_Projektmanagement/17_Controlling/Burndown-Chart.md")
    if not os.path.exists(p):
        return []
    zeilen = []
    zelle = r"[\s*]*([\d.,]*)[\s*]*"
    muster = r"^\|\s*(\d+)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|" + zelle + r"\|" + zelle + r"\|"
    for m in re.finditer(muster, open(p, encoding="utf-8").read(), re.M):
        tag, dat, ideal, ist = m.groups()
        zahl = lambda v: float(v.replace(",", ".")) if v.strip() else None
        zeilen.append({"tag": int(tag), "datum": dat, "ideal": zahl(ideal), "ist": zahl(ist)})
    return zeilen


def lies_weiches_kriterium():
    d = frontmatter(os.path.join(ROOT, "10_Projektmanagement/17_Controlling/Weiches-Kriterium.md"))
    seit = d.get("aelteste_offene_frage_seit") or d.get("nullpunkt")
    t = tage_seit(seit)
    if t is None:
        return None
    status = "gruen" if t <= 7 else ("gelb" if t <= 14 else "rot")
    return {"tage": t, "status": status, "seit": str(seit)}


def lies_abgaben():
    """Zieht die offenen Abgaben aus dem Tracker."""
    p = os.path.join(ROOT, "10_Projektmanagement/19_GPM-Kurs/Abgaben-Tracker.md")
    if not os.path.exists(p):
        return []
    offen = []
    for zeile in open(p, encoding="utf-8"):
        if not zeile.startswith("|") or "offen" not in zeile:
            continue
        sp = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(sp) < 4:
            continue
        titel = re.sub(r"\*\*|\[\[|\]\]", "", sp[1])
        frist = re.sub(r"\*\*|→|≈", "", sp[2]).strip()
        offen.append({"titel": titel, "frist": frist})
    return offen[:5]


# ---------------------------------------------------------------- HTML
def baue():
    aufgaben = lies_aufgaben()
    sprints  = lies_sprints()
    risiken  = lies_risiken()

    aktiv = next((s for s in sprints if s.get("status") in ("laufend", "geplant")), sprints[0] if sprints else {})
    nr = aktiv.get("nummer")

    im_sprint = [a for a in aufgaben if a.get("sprint") == nr]
    erledigt_ids = {a["id"] for a in aufgaben if a.get("status") == "erledigt"}
    blockiert = [a for a in aufgaben
                 if a.get("status") != "erledigt"
                 and any(b not in erledigt_ids for b in a["blockiert_durch"])]

    geplant = sum(a.get("aufwand_h") or 0 for a in im_sprint)
    offen_h = sum(a.get("aufwand_h") or 0 for a in im_sprint if a.get("status") != "erledigt")
    kap = aktiv.get("kapazitaet_h") or 0

    pro_person = {}
    for a in im_sprint:
        w = a.get("verantwortlich") or "nicht zugewiesen"
        pro_person.setdefault(w, {"gesamt": 0, "offen": 0})
        pro_person[w]["gesamt"] += a.get("aufwand_h") or 0
        if a.get("status") != "erledigt":
            pro_person[w]["offen"] += a.get("aufwand_h") or 0

    daten = {
        "sprint": {k: (str(v) if isinstance(v, (datetime.date, datetime.datetime)) else v)
                   for k, v in aktiv.items() if not k.startswith("_")},
        "aufgaben": im_sprint,
        "backlog": [a for a in aufgaben if a.get("status") == "product-backlog"],
        "blockiert": blockiert,
        "risiken": risiken[:6],
        "burndown": lies_burndown(),
        "weiches": lies_weiches_kriterium(),
        "abgaben": lies_abgaben(),
        "personen": [{"name": k, "farbe": farbe(k), "initialen": initialen(k), **v}
                     for k, v in sorted(pro_person.items(), key=lambda x: -x[1]["gesamt"])],
        "kennzahlen": {"geplant_h": geplant, "offen_h": offen_h, "kapazitaet_h": kap,
                       "auslastung": round(geplant / kap * 100) if kap else None,
                       "anzahl": len(im_sprint),
                       "erledigt": len([a for a in im_sprint if a.get("status") == "erledigt"])},
        "meta": {"gebaut": datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
                 "repo": repo_url(), "branch": branch(),
                 "spalten": [{"key": k, "label": l} for k, l in SPALTEN]},
    }
    for a in daten["aufgaben"] + daten["backlog"] + daten["blockiert"]:
        a["_farbe"] = farbe(a.get("verantwortlich"))
        a["_initialen"] = initialen(a.get("verantwortlich"))

    os.makedirs(OUT, exist_ok=True)
    tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard.html"), encoding="utf-8").read()
    js = json.dumps(daten, ensure_ascii=False, default=str)
    if "/*__DATEN__*/null" not in tpl:
        sys.exit("FEHLER: Platzhalter /*__DATEN__*/null fehlt in tools/dashboard.html — "
                 "die Seite waere ohne Daten gebaut worden.")
    seite = tpl.replace("/*__DATEN__*/null", js)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(seite)
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    print(f"_site/index.html gebaut  ·  Sprint {nr}  ·  {len(im_sprint)} Aufgaben  ·  {geplant} h")


if __name__ == "__main__":
    baue()
