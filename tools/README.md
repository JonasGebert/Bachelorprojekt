# tools/

## build_dashboard.py

Erzeugt aus dem Vault eine statische Dashboard-Seite unter `_site/index.html`.

```bash
pip install pyyaml
python3 tools/build_dashboard.py
# lokal ansehen:
python3 -m http.server -d _site 8000   ->  http://localhost:8000
```

**Was gelesen wird** (ausschliesslich YAML-Frontmatter, nie Fliesstext):

| Quelle | wofuer |
|---|---|
| `20_Backlog/Aufgaben/*.md` | Task Board, Aufwaende, Verantwortliche, Blockaden |
| `10_Projektmanagement/14_Sprints/Sprint-*.md` | aktiver Sprint, Sprintziel, Kapazitaet |
| `60_Register/Risiken/R*.md` | Top-Risiken nach Risikozahl |
| `10_Projektmanagement/17_Controlling/Burndown-Chart.md` | Datentabelle des Burndowns |
| `10_Projektmanagement/17_Controlling/Weiches-Kriterium.md` | Feld `aelteste_offene_frage_seit` |
| `10_Projektmanagement/19_GPM-Kurs/Abgaben-Tracker.md` | offene Abgaben |

**Was nicht passiert:** Das Skript schreibt niemals in den Vault. Die Seite ist ein
Betrachter, keine zweite Datenquelle.

**Umgebungsvariablen**

| Variable | Wirkung |
|---|---|
| `REPO_URL` | Basis-URL fuer die Bearbeiten-Links (sonst aus `git remote origin`) |
| `GITHUB_REPOSITORY`, `GITHUB_REF_NAME` | werden in der Action automatisch gesetzt |

## dashboard.html

Die Vorlage. Der Platzhalter `/*__DATEN__*/null` wird beim Bauen durch das JSON ersetzt.
Layout und Farben liegen hier — Aenderungen am Aussehen betreffen nur diese Datei.
