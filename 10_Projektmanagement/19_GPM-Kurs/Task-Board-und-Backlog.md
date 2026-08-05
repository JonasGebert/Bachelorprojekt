---
typ: methode
titel: "Task Board, Product Backlog, Sprint Backlog"
bereich: gpm
tags:
  - gpm
  - methode
  - backlog
quelle: "Koeppen GPM Teil 2 Folien 13-17"
aktualisiert: 2026-08-05
---


# Task Board, Product Backlog, Sprint Backlog

## Die vier Spalten

| Spalte | `status` im Repository | Bedeutung |
|---|---|---|
| Product Backlog | `product-backlog` | alle bekannten Aufgaben, priorisiert, noch keinem Sprint zugeordnet |
| Sprint Backlog | `sprint-backlog` | für den laufenden Sprint eingeplant (`sprint: N` gesetzt) |
| In Arbeit | `in-arbeit` | wird gerade bearbeitet |
| Erledigt | `erledigt` | Definition of Done erfüllt |

> **Kein „blockiert" als Spalte.** Scrum kennt diese Spalte nicht. Blockaden werden im Feld `blockiert_durch` einer Aufgabe erfasst, die Aufgabe bleibt in ihrer Spalte stehen. So bleibt das Board methodenkonform und die Abhängigkeit trotzdem sichtbar.

## Regeln

- Jede Aufgabe erhält eine **eigene Karte** → im Repository eine eigene Datei in `20_Backlog/Aufgaben/`.
- Vor Beginn eines Sprints muss die Spalte „In Arbeit" **leer** sein.
- Nicht zu viele Aufgaben gleichzeitig auf „In Arbeit" ziehen.
- Aufgaben werden **gezogen**, nicht zugewiesen: das Teammitglied trägt sich selbst als `verantwortlich` ein.
- Der Product Backlog ist nicht statisch; er muss zu Beginn nicht vollständig sein. Eine Aufgabe im Product Backlog gilt noch **nicht** als dem Kunden zugesagt.
- Finale Priorisierungsentscheidung trifft der Product Owner.

## Aufgabenzuschnitt

| Größe | Wert |
|---|---|
| Zielgröße | 10–15 h |
| Minimum | 5 h |
| Maximum | 20 h |

Zu kleine Aufgaben erzeugen unverhältnismäßigen Organisationsaufwand, zu große Aufgaben sind über das Board nicht steuerbar. Bei geplanter Sprintkapazität von z. B. 170 h ergeben sich ca. **10–15 Aufgaben pro Sprint**.

**Wichtig:** Der Arbeitsumfang meint die **Netto-Zeit**. Arbeiten zwei Personen je 6 h an einer Aufgabe, beträgt der Aufwand 12 h.
