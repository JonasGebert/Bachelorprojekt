---
typ: controlling
titel: "Burndown-Chart"
bereich: gpm
verantwortlich: "Paul Wettering"
tags:
  - gpm
  - controlling
  - burndown
aktualisiert: 2026-08-05
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
| 1 | 2026-08-11 | 129 |  |  |
| 2 | 2026-08-12 | 114 |  |  |
| 3 | 2026-08-13 | 100 |  |  |
| 4 | 2026-08-14 | 86 |  |  |
| 5 | 2026-08-17 | 72 |  |  |
| 6 | 2026-08-18 | 57 |  |  |
| 7 | 2026-08-19 | 43 |  |  |
| 8 | 2026-08-20 | 29 |  |  |
| 9 | 2026-08-21 | 14 |  |  |
| 10 | 2026-08-23 | 0 |  |  |

> Die Grafik für den Statusbericht wird aus dieser Tabelle erzeugt (Excel oder Skript). Verantwortlich: siehe [[Rollen-und-Verantwortlichkeiten]].
