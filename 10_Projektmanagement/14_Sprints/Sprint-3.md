---
typ: sprint
nummer: 3
titel: "Sprint 3"
status: geplant
start: 2026-09-07
ende: 2026-09-20
kapazitaet_h: 146
geplant_h: 
sprintziel: "Generalprobe bestanden, Versuchsskript im Entwurf"
bereich: gpm
tags:
  - gpm
  - sprint
aktualisiert: 2026-08-05
---


# Sprint 3 (2026-09-07 – 2026-09-20)

> Termine nach **Variante B** des [[Ablaufplan]]s (im Team beschlossen).
> Planning: Mo 07.09.2026 · Review + Retro: Mo 21.09.2026 · Abstimmung Prof. Pähler: 20.09.2026

## Sprintziel

Generalprobe bestanden, Versuchsskript im Entwurf *(im Sprint Planning schärfen — ein Sprint muss ein handfestes Ergebnis haben)*

## Kapazität

| Größe | Wert |
|---|---|
| Teamkapazität rechnerisch | ≈ 146 h |
| tatsächlich eingeplant (Summe `aufwand_h`) | *(nach Planning Poker eintragen)* |
| Anzahl Aufgaben | Richtwert 10–15 |

## Sprint Backlog

Alle Aufgaben mit `sprint: 3` und `status: sprint-backlog` / `in-arbeit` / `erledigt`.

```base
filters:
  and:
    - 'typ == "aufgabe"'
    - 'sprint == 3'
views:
  - type: table
    name: "Sprint 3"
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

→ [[Burndown-Chart]], Datenblatt `Burndown-Sprint-3`
