---
typ: meta
titel: "Ordnerstruktur"
tags:
  - meta
aktualisiert: 2026-08-05
---

# Ordnerstruktur

## Leitgedanke

Der Vault trennt **Sichten**, nicht **Daten**. GPM und Bachelorprojekt haben eigene Ordner und eigene Dashboards, greifen aber auf **dieselben** Aufgaben, Risiken, Entscheidungen und Fragen zu. Eine Aufgabe existiert genau einmal — als Datei in `20_Backlog/Aufgaben/`. Ob sie im GPM-Sprintbericht oder in der fachlichen Planung auftaucht, entscheidet ein Filter über das Frontmatter, keine Kopie.

Der Grund ist praktisch: Der Sprint Backlog der GPM-Veranstaltung besteht inhaltlich vollständig aus Bachelorprojekt-Aufgaben. Zwei getrennte Listen würden nach dem ersten Sprint auseinanderlaufen.

## Die Ordner

| Ordner | Inhalt | Sicht |
|---|---|---|
| `00_Inbox/` | Roherfassung je Person, wird im Weekly verteilt | beide |
| `00_Meta/` | Konventionen, Ordnerstruktur, Vorlagen | beide |
| `10_Projektmanagement/` | GPM: Projektauftrag, Team, User Stories, Sprints, Statusberichte, Meetings, Controlling, Kursunterlagen | GPM |
| `20_Backlog/` | **die Brücke**: alle Aufgaben als Einzelnotizen, Task Board, Ideenspeicher | beide |
| `30_Fachprojekt/` | BP: Auftrag, Konstruktion, Vorversuche, Laborversuch, Arbeitssicherheit, Ergebnisse | BP |
| `40_Wissensbasis/` | verfahrensneutrales Fachwissen (Gießverfahren, Formstoffe, Werkstoffe, Gießfehler) | BP |
| `50_Quellen/` | Literaturverzeichnis Q01–Q25, Normen | BP |
| `60_Register/` | Entscheidungen E##, Risiken R##, offene Fragen F## | beide |
| `70_Journal/` | Projektlog, chronologisch | beide |
| `90_Assets/` | CAD-Dateien, Bilder, Datenblätter | beide |

## Unterordner 10_Projektmanagement

| Ordner | Inhalt |
|---|---|
| `11_Projektauftrag/` | Projektauftrag, Ablaufplan, Teamregeln — die unterschriebenen bzw. eingereichten Dokumente |
| `12_Team/` | Rollen und Verantwortlichkeiten |
| `13_User-Stories/` | US-01 … US-05 |
| `14_Sprints/` | Sprint-1 … Sprint-4, je mit Planning, Review, Retrospective |
| `15_Statusberichte/` | One Pager je Sprint + Vorlage |
| `16_Meetings/` | Protokolle: Weekly, Planning, Review, Retro, AG-Abstimmung |
| `17_Controlling/` | Burndown-Chart, Team-Management-Barometer, weiches Kriterium |
| `19_GPM-Kurs/` | Methodenreferenz aus der Vorlesung + Foliensätze als PDF + Abgaben-Tracker |

## Unterordner 30_Fachprojekt

| Ordner | Inhalt |
|---|---|
| `31_Auftrag/` | Original-Aufgabenstellung (PDF + Markdown) mit Anforderungen A1–A10 |
| `32_Konstruktion/` | Bauteilkonzept, Modellbau, Kernkasten, Formkasten |
| `33_Vorversuche/` | Vorversuchsplan + je Versuch eine Notiz (V-F1, V-W1, …) |
| `34_Laborversuch/` | Versuchskonzept, Gussfehler-Provokation, später das Versuchsskript |
| `35_Arbeitssicherheit/` | Gefährdungen G1–G10, Gefährdungsbeurteilung |
| `36_Ergebnisse/` | Testlauf, Werkstückbewertung, Optimierungsmaßnahmen |

## Die Inbox

Erfassen und Einsortieren sind getrennte Vorgänge. Die Inbox nimmt Rohnotizen auf, ohne dass im Moment des Erfassens entschieden werden muss, wohin sie gehören. Geleert wird sie **im Weekly** — nicht in einem separaten Wochenritual, das neben der bestehenden Scrum-Kadenz auf Dauer nicht durchgehalten wird.

Eine Datei **pro Person** (`Inbox-Jonas.md`, `Inbox-Fynn.md`, `Inbox-Paul.md`): Bei einer gemeinsamen Datei erzeugt jeder parallele Eintrag einen Git-Merge-Konflikt in derselben Zeile. Regeln und Routing-Tabelle: [[Inbox]].

## Warum Einzelnotizen statt Sammellisten

| Registertyp | Form | Begründung |
|---|---|---|
| Aufgaben | eine Datei je Aufgabe | Task Board braucht Karten; Aufwand, Verantwortliche und Sprint sind je Aufgabe zu pflegen |
| Risiken | eine Datei je Risiko | Risikomatrix braucht W und H als Zahlenfelder; jede Maßnahme hat eine:n Verantwortliche:n |
| Entscheidungen | eine Datei je Entscheidung | Entscheidungen werden einzeln zitiert und revidiert |
| Offene Fragen | **eine gemeinsame Tabelle** | hoher Umschlag, kurze Inhalte, werden in Blöcken beantwortet — Einzelnotizen wären reiner Overhead |
| Quellen | **eine gemeinsame Tabelle** | Zitieren ist einfacher aus einer Liste als aus 25 Dateien |
| Projektlog | **eine Datei**, neueste oben | chronologisches Lesen ist wichtiger als Verlinkung |

## Dateinamen

- Keine Umlaute und kein ß in Dateinamen (`Giessverfahren.md`, nicht `Gießverfahren.md`). Grund: macOS speichert Umlaute in zerlegter Form (NFD), Windows und Linux in zusammengesetzter Form (NFC) — das erzeugt in Git Phantomänderungen und doppelte Dateien. Im **Inhalt** sind Umlaute selbstverständlich.
- Präfix-IDs bleiben stabil: `TASK-###`, `US-##`, `E##`, `R##`, `V-*`, `Sprint-#`.
- Bindestrich statt Unterstrich in Notiznamen.
