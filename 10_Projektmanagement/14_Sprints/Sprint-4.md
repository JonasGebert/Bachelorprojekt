---
typ: sprint
nummer: 4
titel: "Sprint 4"
status: geplant
start: 2026-09-21
ende: 2026-09-27
kapazitaet_h: 72
geplant_h: 
sprintziel: "Abgabefähige Dokumentation und Optimierungsmaßnahmen"
bereich: gpm
tags:
  - gpm
  - sprint
aktualisiert: 2026-08-05
---


# Sprint 4 (2026-09-21 – 2026-09-27)

> Termine nach **Variante B** des [[Ablaufplan]]s (im Team beschlossen).
> Planning: Mo 21.09.2026 · Review + Retro: Mo 28.09.2026 · Abstimmung Prof. Pähler: 27.09.2026 · GPM Teil 4: Mi 30.09.2026

## Sprintziel

Abgabefähige Dokumentation und Optimierungsmaßnahmen *(im Sprint Planning schärfen — ein Sprint muss ein handfestes Ergebnis haben)*

## Kapazität

| Größe | Wert |
|---|---|
| Teamkapazität rechnerisch | ≈ 72 h |
| tatsächlich eingeplant (Summe `aufwand_h`) | *(nach Planning Poker eintragen)* |
| Anzahl Aufgaben | Richtwert 10–15 |

## Sprint Backlog

Alle Aufgaben mit `sprint: 4` und `status: sprint-backlog` / `in-arbeit` / `erledigt`.

```base
filters:
  and:
    - 'typ == "aufgabe"'
    - 'sprint == 4'
views:
  - type: table
    name: "Sprint 4"
    groupBy:
      property: note.status
      direction: ASC
    order:
      - file.name
      - titel
      - status
      - verantwortlich
      - aufwand_h
      - prioritaet
```

## Sprint Planning

- Datum: *(eintragen)*
- Teilnehmende: *(eintragen)*
- Planning Poker durchgeführt für: *(alle Aufgaben im Sprint Backlog — Pflicht)*

## Sprint Review

- Datum: *(eintragen)* · Teilnehmende inkl. Product Owner: *(eintragen)*
- Sprintziel erreicht? ☐ ja ☐ teilweise ☐ nein
- Vorgestellte Ergebnisse:
- Feedback des Product Owners:

## Sprint Retrospective

| Was lief gut? | Was lief nicht gut? | Maßnahme für den nächsten Sprint | Verantwortlich |
|---|---|---|---|
|  |  |  |  |

## Burndown

→ [[Burndown-Chart]], Datenblatt `Burndown-Sprint-4`
