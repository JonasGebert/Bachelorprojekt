---
typ: uebersicht
titel: "Inbox — Erfassen und Verteilen"
bereich: beide
tags:
  - inbox
aktualisiert: 2026-08-05
---

# Inbox — Erfassen und Verteilen

> **Zweck:** Gedanken, Beobachtungen und Zufallsfunde festhalten, ohne im Moment entscheiden zu müssen, wohin sie gehören. Erfassen kostet Sekunden, Einsortieren kostet Nachdenken — das wird getrennt.

## Drei Dateien, eine pro Person

| Datei | Wer |
|---|---|
| [[Inbox-Jonas]] | Jonas Gebert |
| [[Inbox-Fynn]] | Fynn Barmwater |
| [[Inbox-Paul]] | Paul Wettering |

**Warum getrennt:** Bei einer gemeinsamen Datei erzeugt jeder parallele Eintrag einen Git-Merge-Konflikt in genau derselben Zeile. Drei Dateien, an die nur angehängt wird, kollidieren nie. Anhänge (Fotos vom Ofen-Typenschild, Datenblätter, Skizzen) landen direkt als Datei in diesem Ordner und werden beim Verteilen nach `90_Assets/` verschoben.

## Wann wird geleert

**Kein separates Wochenritual.** Die Inbox hängt an den Scrum-Terminen, die ohnehin stattfinden:

| Termin | Was mit der Inbox passiert |
|---|---|
| **Weekly** (Di und Do, 15–30 min) | Jede:r geht die eigene Inbox durch. Alles, was klar ist, wird sofort verteilt. Alles Unklare bleibt liegen — mit einer Rückfrage versehen. |
| **Sprint Planning** | Die Inbox muss **leer** sein, bevor priorisiert wird. Sonst plant ihr gegen einen unvollständigen Backlog. |
| **Sprint Retrospective** | Wiederkehrende Inbox-Einträge sind ein Signal: Was landet hier immer wieder, das eigentlich eine Aufgabe oder eine Regel sein müsste? |

## Die eine harte Regel

> **Aus der Inbox geht nichts direkt in den laufenden Sprint.**

Eine erfasste Aufgabe wird zu `TASK-###` mit `status: product-backlog`. Sie kommt frühestens im nächsten Sprint Planning in einen Sprint. Grund: GPM Teil 2 verbietet ausdrücklich, während eines laufenden Sprints Aufgaben zum Sprint Backlog hinzuzufügen — sonst ist die Kapazitätsplanung und das Burndown-Chart wertlos.

**Ausnahme:** Ein Fund, der eine Aufgabe im laufenden Sprint *blockiert*. Der gehört sofort ins Feld `blockiert_durch` der betroffenen Aufgabe und ins nächste Weekly — das ist keine neue Aufgabe, sondern eine Statusänderung an einer bestehenden.

## Wohin was verteilt wird

| Was du erfasst hast | Ziel | Vorlage |
|---|---|---|
| konkretes To-do | `20_Backlog/Aufgaben/TASK-###.md`, `status: product-backlog` | [[Vorlage-Aufgabe]] |
| Idee ohne Auftrag, noch nicht bewertet | [[Ideenspeicher]] | — |
| Frage an Prof. Pähler oder Prof. Koeppen | [[Offene-Fragen]], nächste freie `F##` | — |
| fachliche Erkenntnis, Zusammenhang | passende Notiz in `40_Wissensbasis/` | [[Vorlage-Wissen]] |
| Quelle, Buch, Norm, Link | [[Literatur]] als `Q##` bzw. [[Normen]] | — |
| „das könnte schiefgehen" | `60_Register/Risiken/R##.md` | [[Vorlage-Risiko]] |
| getroffene Festlegung mit Alternativen | `60_Register/Entscheidungen/E##.md` | [[Vorlage-Entscheidung]] |
| Messwert, Beobachtung aus einem Versuch | zugehörige Versuchsnotiz in `33_Vorversuche/` | [[Vorlage-Versuch]] |
| Foto, CAD-Datei, Datenblatt | `90_Assets/` und aus der Fachnotiz verlinken | — |
| reine Statusinfo, „heute passiert" | [[Projektlog]], neuester Eintrag oben | — |
| gehört nirgendwohin | löschen. Nicht alles muss aufgehoben werden. | — |

## Abgrenzung: Inbox, Tagesnotiz, Projektlog

Drei Orte, die leicht verwechselt werden. Die Zuordnung ist eindeutig:

| | Inbox | Tagesnotiz | Projektlog |
|---|---|---|---|
| **Wofuer** | Gedanke zwischendurch, ohne Kontext | Mitschrift waehrend der Arbeit, v. a. Versuchstage bei Goepfert | kuratierte Projektgeschichte |
| **Lebensdauer** | bis zum naechsten Weekly | bis zum Ende des Arbeitstags | dauerhaft |
| **Wer liest das spaeter** | niemand | niemand | Team, Prof. Paehler, der Projektbericht |
| **Ort** | `00_Inbox/Inbox-<Name>.md` | `70_Journal/Tagesnotizen/JJJJ-MM-TT.md` | `70_Journal/Projektlog.md` |

**Faustregel:** Inbox und Tagesnotiz sind Zwischenlager mit Verfallsdatum. Nur der Projektlog ist Archiv. Steht etwas nach dem Weekly noch in der Inbox oder nach dem Arbeitstag noch in der Tagesnotiz, ist es nicht verteilt worden — und damit faktisch verloren.

## Erfassungsformat

Eine Zeile reicht. Datum voranstellen, damit später nachvollziehbar ist, wann der Gedanke entstand:

```
- 2026-08-11 Vogelsand Marke X riecht stark nach Anis — Ölanteil in V-F1 evtl. anpassen
- 2026-08-11 Frage: Darf der Ofen über Nacht laufen? (Pähler)
- 2026-08-12 https://... Video Handformverfahren, evtl. QR-Code fürs Skript
```

Kein Frontmatter, keine Formatierung, keine Vollständigkeit. Wer beim Erfassen formatiert, erfasst irgendwann nicht mehr.

## Mit Claude leeren

> „Leere meine Inbox" oder „Triagiere die Inbox"

Claude schlägt für jeden Eintrag ein Ziel vor, legt nach Bestätigung die Notizen an und entfernt die Zeilen aus der Inbox. Details in `CLAUDE.md`, Abschnitt 4.
