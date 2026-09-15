---
typ: controlling
titel: "Burndown-Chart"
bereich: gpm
verantwortlich: "Paul Wettering"
tags:
  - gpm
  - controlling
  - burndown
aktualisiert: 2026-09-13
---


# Burndown-Chart

> Methodik: [[Projektcontrolling]]. **Je Sprint neu erstellen und täglich aktualisieren.**

## Prinzip

Das Burndown-Chart visualisiert die Abarbeitung der Arbeitspakete: Für jeden Sprint wird der Restaufwand über den Tagen des Sprints aufgetragen. Jedes fertige Arbeitspaket wird aus dem Stapel genommen. Am Ende des Sprints sollte der Stapel leer sein.

- Fällt die Kurve **kontinuierlich** ab → regelmäßige Abarbeitung.
- Fällt sie **nicht** kontinuierlich ab → verzögernde Arbeitspakete aufdecken und Maßnahmen zu ihrer Fertigstellung finden.
- **Prüfen:** Entspricht der Gesamt-Arbeitsaufwand am Anfang der Kapazität des Sprints?

## Datenblatt Sprint 1

**Startwert = 143 h** (Summe `aufwand_h` über die 12 Aufgaben in [[Sprint-1]], Referenzschätzung — nach dem Planning Poker anpassen).

**Idealline:** 143 h über 10 Arbeitstage ≈ 14,3 h Abbau je Tag. Da Aufgaben nur ganz oder gar nicht abgebaut werden, verläuft die reale Kurve treppenförmig — entscheidend ist, dass sie der Idealline folgt und nicht erst in der zweiten Woche abfällt.

**Prüfung nach GPM Teil 3:** Entspricht der Gesamtaufwand am Anfang der Sprintkapazität? 143 h gegenüber 146 h Kapazität = 98 % → ja, aber ohne Reserve.

| Tag | Datum | Ideal [h] | Rest ist [h] | erledigte Aufgaben |
|---|---|---|---|---|
| 0 | 2026-08-10 | 143 | **143** | — (Sprintstart) |
| 1 | 2026-08-11 | 129 | **135** | [[TASK-018]] Beschaffung, v. a. Thermoelement Typ K (8 h) |
| 2 | 2026-08-12 | 114 | **117** | [[TASK-002]] Ablaufplan einreichen (8 h), [[TASK-001]] Projektauftrag unterschreiben lassen (10 h) |
| 3 | 2026-08-13 | 100 | **112** | [[TASK-019]] Fachbuch Fritz/Schulze [Q1] beschaffen (5 h) |
| 4 | 2026-08-14 | 86 | **102** | [[TASK-016]] Formkästen vermessen (10 h) |
| 5 | 2026-08-17 | 72 | **88** | [[TASK-012]] Abstimmungstermin Prof. Pähler (F14/F16/F17/F7b/F25/F27) (14 h) |
| 6 | 2026-08-18 | 57 | **80** | [[TASK-041]] Unterweisung und Versicherung bei Göpfert klären (8 h) |
| 7 | 2026-08-19 | 43 | **68** | [[TASK-017]] Ofen dokumentieren, Aufheizkurve (12 h) |
| 8 | 2026-08-20 | 29 | **48** | [[TASK-024]] V-F1 Sandrezeptur (20 h) |
| 9 | 2026-08-21 | 14 | **32** | [[TASK-025]] V-W1 Ofen- und Temperaturverhalten (16 h) |
| 10 | 2026-08-23 | 0 | **20** | [[TASK-042]] Ausstattungsvergleich Göpfert ↔ FtT-Labor (12 h) |

> Aufgabennamen sind wortgleich mit der Spalte „Aufgabe" im Sprint Backlog von [[Sprint-1]] (inkl. TASK-ID als Wikilink) — Bewertung Statusbericht 1 bemängelte abweichende Kurznamen zwischen Burndown-Grafik und Sprint Backlog.

## Auswertung Sprint 1

**11 von 12 Aufgaben erledigt, 123 h abgebaut, 20 h Restaufwand.** Die Kurve fällt kontinuierlich — regelmäßige Abarbeitung ist damit belegt. Sie verläuft durchgehend etwa 10 bis 20 h oberhalb der Idealline und endet nicht bei null.

**Ursache des Restaufwands:** [[TASK-021]] (parametrisches CAD-Modell, 20 h) war bis zum 17.08. durch die offene Bauteilentscheidung F33 blockiert und konnte im Sprint nicht mehr fertiggestellt werden. Die Aufgabe wird vollständig nach Sprint 2 übernommen — nach Scrum gibt es nur *ganz fertig*, kein *fast fertig*, deshalb wird kein Teilfortschritt abgebucht.

**Konsequenz für Sprint 2:** Die 20 h gehen als Erstes in den neuen Sprint. Die Aufgabe wird zusätzlich geteilt (Bauteil + Kern / Kernkasten + Modell), damit der Burndown feiner auflöst und eine Blockade nicht mehr ein Paket von 20 h stehen lässt.

> Die Grafik für den Statusbericht wird aus dieser Tabelle erzeugt (Excel oder Skript). Verantwortlich: siehe [[Rollen-und-Verantwortlichkeiten]].
