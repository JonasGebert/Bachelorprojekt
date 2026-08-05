---
typ: uebersicht
titel: "Product Backlog"
bereich: beide
tags:
  - backlog
  - uebersicht
aktualisiert: 2026-08-05
---


# Product Backlog

> **Einzige Quelle für Aufgaben.** Jede Aufgabe ist eine eigene Notiz in `Aufgaben/`. Der Sprint Backlog ist keine zweite Liste, sondern eine **Auswahl** hieraus (`sprint: N`).
> Spielregeln: [[Task-Board-und-Backlog]] · Schätzung: [[Planning-Poker]]

## Task Board

![[Task-Board.base]]

## Spalten und Statuswerte

| Spalte im Task Board | `status` |
|---|---|
| Product Backlog | `product-backlog` |
| Sprint Backlog | `sprint-backlog` |
| In Arbeit | `in-arbeit` |
| Erledigt | `erledigt` |
| *(nicht auf dem Board)* | `entfallen` — stillgelegt oder zusammengeführt, ID bleibt vergeben |

Blockaden stehen im Feld `blockiert_durch` — **nicht** als eigene Spalte, das kennt Scrum nicht.

## Stand 2026-08-05

| | Anzahl | Aufwand |
|---|---|---|
| Sprint Backlog (Sprint 1) | 12 | 143 h (Referenzschätzung) |
| Product Backlog | 26 | noch nicht geschätzt |
| Erledigt im Projektzeitraum (ab 03.08.2026) | 1 | — |
| **Vorleistung vor Projektstart** (04.07.2026) | 6 | nicht im Burndown |
| Entfallen (zusammengeführt in [[TASK-012]]) | 3 | — |

> `schaetzung: referenz` heißt: Ausgangswert für den Planning Poker. Erst nach dem Poker im Team gilt `schaetzung: poker`.
>
> **Zur Vorleistung:** Wissensbasis, Literaturrecherche, Bauteilkonzept und das Fragenregister entstanden am 04.07.2026 — vier Wochen vor Modulbeginn, aus Eigeninitiative. Diese Aufgaben tragen `vorleistung: true`, sind keinem Sprint zugeordnet und gehen nicht in den Burndown ein. Im Statusbericht gehören sie unter „aktuelle Ergebnisse" als Ausgangsbasis, nicht als Sprintleistung.

## Wenn Bases nicht verfügbar ist

Die Aufgaben lassen sich auch ohne Plugin lesen: `20_Backlog/Aufgaben/TASK-*.md`, sortiert nach ID. Das Frontmatter enthält alle Steuerinformationen.

## Ideen, die noch keine Aufgaben sind

→ [[Ideenspeicher]]
