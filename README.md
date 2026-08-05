# Bachelorprojekt — Entwicklung eines Versuchs zum Thema Metallguss für das FtT-Labor

**S26 · PRODT P01 · HAW Hamburg · Betreuer: Prof. Dr.-Ing. Dietmar Pähler · GPM: Prof. Dr. Birgit Koeppen · Abgabe: 05.10.2026**

Dieses Repository ist gleichzeitig ein **Git-Repository** und ein **Obsidian-Vault**. Es enthält die gesamte Projektdokumentation: fachlichen Inhalt, Projektmanagement nach Scrum und die Wissensbasis.

---

## Schnellstart

```bash
git clone <repo-url>
cd Bachelorprojekt
```

### 1. Obsidian einrichten

1. [Obsidian](https://obsidian.md) installieren (Version **1.9 oder neuer** — ältere Versionen kennen den Bases-Plugin nicht).
2. *Open folder as vault* → diesen Ordner wählen.
3. In den Einstellungen unter **Core plugins** aktivieren: **Bases**, **Templates**, **Graph view**, **Outgoing links**, **Backlinks**.
4. Unter *Templates* den Vorlagenordner auf `00_Meta/Vorlagen` setzen.
5. `Dashboard.md` öffnen — das ist der Einstiegspunkt.

> Ohne Bases funktioniert der Vault weiterhin, es fehlen lediglich die Tabellen- und Kartenansichten. Alle Inhalte bleiben als reines Markdown lesbar, auch in VS Code oder auf GitHub.

### 2. Als Projekt in Claude Cowork anlegen

1. Cowork öffnen → neues Projekt anlegen.
2. Als Arbeitsordner diesen geklonten Ordner auswählen.
3. `CLAUDE.md` im Wurzelverzeichnis wird automatisch gelesen und enthält alle Arbeitsanweisungen — Struktur, Konventionen und die wiederkehrenden Arbeitsabläufe.
4. Direkt einsatzbereite Aufträge:
   - „Was haben wir noch zu tun?"
   - „Erstelle mir den Sprint Backlog für Sprint 2"
   - „Erstelle den Statusbericht für Sprint 1"
   - „Lege eine Aufgabe für die Beschaffung des Thermoelements an"
   - „Dokumentiere den Vorversuch V-F1"
   - „Leere die Inbox"

### 3. Dashboard auf GitHub Pages aktivieren

Einmalig, ~2 Minuten:

1. Repository → **Settings → Pages** → *Source* auf **GitHub Actions** stellen.
2. Einmal auf `main` pushen. Die Action `Dashboard bauen und veröffentlichen` läuft an.
3. Die Seite liegt danach unter `https://<user>.github.io/<repo>/`.

Ab dann wird die Seite bei **jedem Push** neu gebaut, der `20_Backlog/`, `10_Projektmanagement/`, `60_Register/` oder `tools/` berührt — Latenz rund eine Minute.

Lokale Vorschau ohne GitHub:

```bash
pip install pyyaml
python3 tools/build_dashboard.py
python3 -m http.server -d _site 8000    # → http://localhost:8000
```

> Das Dashboard ist ein **Betrachter, keine Datenquelle.** Es liest nur das YAML-Frontmatter und schreibt nie zurück. Ein Klick auf eine Karte öffnet die zugehörige Markdown-Datei auf GitHub — dort wird geändert, und der nächste Build zieht nach. So gibt es keine zweite Wahrheit neben dem Vault.

---

## Öffentliches Repository — was das bedeutet

Dieses Repository ist öffentlich einsehbar. Zwei Regeln folgen daraus:

1. **Keine personenbezogenen Einzelbewertungen.** Das [Team-Management-Barometer](10_Projektmanagement/17_Controlling/Team-Management-Barometer.md) speichert ausschließlich **Mittelwerte**. Einzelwerte werden verdeckt erhoben, im Meeting besprochen und nicht archiviert.
2. **Retrospektiven sachlich halten.** Kritik am Vorgehen, nicht an Personen — und keine Namensnennung bei negativen Punkten.

Kontaktdaten Dritter (z. B. die E-Mail-Adresse des Betreuers in der Original-Aufgabenstellung) stammen aus dem offiziellen Projektaushang der HAW. Wer das nicht öffentlich haben möchte, maskiert sie in `30_Fachprojekt/31_Auftrag/Aufgabenstellung.md`.

---

## Aufbau

```
Dashboard.md              ← Einstiegspunkt
CLAUDE.md                 ← Arbeitsanweisung für den KI-Assistenten
00_Inbox/                 Roherfassung je Person, wird im Weekly verteilt
00_Meta/                  Konventionen, Ordnerstruktur, Vorlagen
10_Projektmanagement/     GPM: Projektauftrag, Team, User Stories, Sprints,
                          Statusberichte, Meetings, Controlling, Kursunterlagen
20_Backlog/               alle Aufgaben als Einzelnotizen + Task Board
30_Fachprojekt/           Auftrag, Konstruktion, Vorversuche, Laborversuch,
                          Arbeitssicherheit, Ergebnisse
40_Wissensbasis/          Fachwissen: Gießverfahren, Formstoffe, Werkstoffe, Gießfehler
50_Quellen/               Literaturverzeichnis Q01–Q25, Normen
60_Register/              Entscheidungen E##, Risiken R##, offene Fragen F##
70_Journal/               Projektlog
90_Assets/                CAD-Dateien, Bilder, Datenblätter
tools/                    Generator für das GitHub-Pages-Dashboard
.github/workflows/        Action, die die Seite bei jedem Push baut
```

### Das Strukturprinzip

Der Vault trennt **Sichten**, nicht **Daten**:

- **Bachelorprojekt (BP)** beantwortet: *Was bauen wir und warum so?* → [`30_Fachprojekt/Projekt-Dashboard.md`](30_Fachprojekt/Projekt-Dashboard.md)
- **Projektmanagement (GPM)** beantwortet: *Wie steuern und belegen wir das?* → [`10_Projektmanagement/GPM-Dashboard.md`](10_Projektmanagement/GPM-Dashboard.md)

Beide greifen auf **dieselben** Aufgaben, Risiken, Entscheidungen und Fragen zu. Der Sprint Backlog der GPM-Veranstaltung besteht inhaltlich vollständig aus Bachelorprojekt-Aufgaben — zwei getrennte Listen würden nach dem ersten Sprint auseinanderlaufen. Details: [`00_Meta/Ordnerstruktur.md`](00_Meta/Ordnerstruktur.md)

---

## Konventionen in Kurzform

| Präfix | Bedeutung | Ort |
|---|---|---|
| `A##` | Anforderung aus der Aufgabenstellung | `30_Fachprojekt/31_Auftrag/Aufgabenstellung.md` |
| `TASK-###` | Aufgabe | `20_Backlog/Aufgaben/` |
| `US-##` | User Story | `10_Projektmanagement/13_User-Stories/` |
| `E##` | Entscheidung | `60_Register/Entscheidungen/` |
| `R##` | Projektrisiko | `60_Register/Risiken/` |
| `F##` | Offene Frage | `60_Register/Offene-Fragen.md` |
| `Q##` | Quelle | `50_Quellen/Literatur.md` |
| `V-*` | Vorversuch | `30_Fachprojekt/33_Vorversuche/` |

**Quellensystem:** `[Q##]` = geprüfte Quelle · `[Fachwissen – Quelle nachtragen]` = fachlich etabliert, aber noch unbelegt. Nichts mit dem zweiten Tag geht ungeprüft in den Projektbericht.

**Dateinamen** enthalten keine Umlaute und kein ß — macOS und Windows kodieren diese unterschiedlich, was in Git Phantomänderungen erzeugt. Im Inhalt sind Umlaute normal.

Vollständig: [`00_Meta/Konventionen.md`](00_Meta/Konventionen.md)

---

## Mitarbeiten

1. Neue Notizen immer aus einer Vorlage in `00_Meta/Vorlagen/` erzeugen — das Frontmatter steuert alle Tabellenansichten.
2. Aufgabenstatus nur aus `product-backlog` · `sprint-backlog` · `in-arbeit` · `erledigt`. Es gibt kein „halb fertig".
3. Aufwände (`aufwand_h`) werden ausschließlich im Planning Poker im Team bestimmt, nie geschätzt.
4. Wesentliche Änderungen in `70_Journal/Projektlog.md` festhalten (neueste Einträge oben).
5. Aussagekräftige Commit-Nachrichten, gern mit ID: `TASK-024: Ergebnisse V-F1 dokumentiert`.
