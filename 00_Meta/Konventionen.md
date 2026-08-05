---
typ: meta
titel: "Konventionen"
tags:
  - meta
aktualisiert: 2026-08-05
---

# Konventionen

## ID-Systeme

| Präfix | Bedeutung | Ort |
|---|---|---|
| `A##` | Anforderung aus der Aufgabenstellung | [[Aufgabenstellung]] (Tabelle) |
| `TASK-###` | Aufgabe / Backlog Item | `20_Backlog/Aufgaben/` |
| `US-##` | User Story | `10_Projektmanagement/13_User-Stories/` |
| `E##` | Entscheidung | `60_Register/Entscheidungen/` |
| `R##` | Projektrisiko | `60_Register/Risiken/` |
| `F##` | Offene Frage | [[Offene-Fragen]] (Tabelle) |
| `Q##` | Quelle | [[Literatur]] (Tabelle) |
| `G##` | Gefährdung (Arbeitsschutz) | [[Arbeitssicherheit]] |
| `V-*` | Vorversuch | `30_Fachprojekt/33_Vorversuche/` |

**IDs werden nie wiederverwendet.** Entfallene Einträge bleiben mit Begründung stehen (siehe R01, R03 in [[Risikoregister]]).

## Quellensystem

| Kennzeichnung | Bedeutung |
|---|---|
| `[Q##]` | geprüfte Quelle aus [[Literatur]] |
| `[Fachwissen – Quelle nachtragen]` | fachlich etablierte Aussage ohne konkreten Beleg |

**Regel:** Nichts mit dem zweiten Tag geht in den Projektbericht, ohne vorher gegen Primärliteratur geprüft zu werden ([[E02]]).

## Frontmatter

Jede Notiz beginnt mit YAML-Frontmatter. Pflichtfelder für alle: `typ`, `titel`, `tags`, `aktualisiert`.

### `typ` — steuert, welche Base eine Notiz erfasst

`aufgabe` · `user-story` · `sprint` · `statusbericht` · `meeting` · `risiko` · `entscheidung` · `versuch` · `wissen` · `quellen` · `konstruktion` · `laborversuch` · `sicherheit` · `register` · `uebersicht` · `dashboard` · `methode` · `kurs` · `vorlage` · `meta` · `journal`

### `bereich` — steuert, in welcher Sicht eine Notiz erscheint

| Wert | Bedeutung |
|---|---|
| `bp` | fachlicher Inhalt des Bachelorprojekts |
| `gpm` | Methode, Nachweise, Abgaben der GPM-Veranstaltung |
| `beide` | Register, die beide Sichten speisen |

### Aufgaben (`typ: aufgabe`)

| Feld | Werte |
|---|---|
| `status` | `product-backlog` · `sprint-backlog` · `in-arbeit` · `erledigt` · `entfallen` |
| `schaetzung` | `referenz` (Ausgangswert, noch nicht im Team bestätigt) · `poker` (Ergebnis des Planning Pokers) |
| `zusammengefuehrt_in` | Wikilink, nur bei `status: entfallen` |
| `kategorie` | `klaerung` · `bestandsaufnahme` · `beschaffung` · `konstruktion` · `fertigung` · `vorversuch` · `laborversuch` · `sicherheit` · `dokumentation` · `methode` · `abgabe` |
| `prioritaet` | `hoch` · `mittel` · `niedrig` |
| `sprint` | Zahl oder leer |
| `aufwand_h` | Zahl — **nur** nach [[Planning-Poker]] füllen, nie schätzen |
| `verantwortlich` | Name — wird **gezogen**, nicht zugewiesen |
| `blockiert_durch` | Liste von Wikilinks |
| `vorleistung` | `true` für Aufgaben, die vor Modulbeginn (03.08.2026) erledigt wurden — keinem Sprint zugeordnet, nicht im Burndown |
| `erledigt_am` | Datum, nur bei `status: erledigt` |

> **Zu `entfallen`:** Das Task Board hat vier Spalten — `entfallen` ist keine davon. Eine entfallene oder zusammengeführte Aufgabe existiert auf dem Board nicht mehr; die Datei bleibt nur bestehen, damit die ID nicht wiederverwendet wird und die Historie nachvollziehbar bleibt. Alle Board-Ansichten filtern `entfallen` heraus.

### Risiken (`typ: risiko`)

`klasse` (technisch/organisatorisch/persoenlich/finanziell/terminlich) · `wahrscheinlichkeit` 1–3 · `schadenshoehe` 1–3 · `risikozahl` = Produkt · `zone` (ok/monitor/act) · `massnahme_typ` (praeventiv/korrektiv) · `wirkung` (wahrscheinlichkeit/schadenshoehe/beide) · `verantwortlich`

## Zeitliche Bezugspunkte

| Datum | Bedeutung |
|---|---|
| 04.07.2026 | Beginn der freiwilligen Vorarbeit (Wissensbasis, Bauteilkonzept, Fragenregister) — **kein** Projektzeitraum |
| **03.08.2026** | **Modulbeginn / Projektstart**, GPM Teil 1. Nullpunkt aller Kennzahlen |
| 10.08.2026 | Beginn Sprint 1, Start der Burndown-Messung |
| 05.10.2026 | Abgabe |

Kennzahlen rechnen **nie** vor dem 03.08.2026. Aufgaben, die vorher erledigt wurden, tragen `vorleistung: true`.

## Verlinkung

- Interne Verweise als Wikilink: `[[Giessverfahren]]`, nicht als Pfad. Der Vault ist flach genug, dass Dateinamen eindeutig sind.
- Jede Fachnotiz verlinkt mindestens auf die Entscheidung oder den Versuch, in dem sie angewendet wird.
- Bases werden mit `![[Task-Board.base]]` eingebettet (Dateiname mit Endung).

## Wissenschaftliche Mindeststandards

- SI-Einheiten, Einheit immer angeben, Dezimalkomma im deutschen Fließtext.
- Zahlenwerte ohne Quelle sind als `[Fachwissen – Quelle nachtragen]` zu kennzeichnen.
- Messwerte mit Messmittel und Messunsicherheit dokumentieren.
- Vorläufige Empfehlungen sind keine Entscheidungen — Status bleibt `vorgeschlagen`.
- Fehlende Informationen werden als offene Frage F## erfasst, nicht durch Annahmen ersetzt.
