---
typ: methode
titel: "Planning Poker"
bereich: gpm
tags:
  - gpm
  - methode
  - schaetzung
quelle: "Koeppen GPM Teil 2 Folie 16"
aktualisiert: 2026-08-05
---


# Planning Poker

Verfahren zur Aufwandsschätzung im Sprint Planning. Geleitet vom **Scrum Master**; der Product Owner kann teilnehmen.

## Ablauf

1. Ein Teammitglied oder der Product Owner erläutert die Aufgabe.
2. Alle schätzen **gleichzeitig und unabhängig** den Aufwand in Stunden.
3. Die Personen mit dem **niedrigsten** und dem **höchsten** Wert begründen ihre Schätzung.
4. Das Team diskutiert, danach folgt eine **zweite Schätzrunde**.
5. Bei weiterhin großen Unterschieden: weitere Diskussions- und Schätzrunden.
6. Liegen alle Werte dicht beieinander, wird der **Mittelwert** gebildet und als `aufwand_h` eingetragen.

## Beispiel aus der Vorlesung

| Teammitglied | 1. | 2. | 3. | 4. | 5. |
|---|---|---|---|---|---|
| Aufwand [h] | 10 | 5 | 11 | 9 | 15 |

→ Nr. 2 und Nr. 5 begründen, danach zweite Runde.

## Regel für dieses Repository

Das Feld `aufwand_h` in einer Aufgabennote wird **ausschließlich** durch Planning Poker gefüllt. Ein leeres Feld bedeutet „noch nicht geschätzt" — es wird nicht geraten.
