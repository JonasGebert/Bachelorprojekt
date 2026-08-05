---
typ: methode
titel: "Risikomanagement"
bereich: gpm
tags:
  - gpm
  - methode
  - risiko
quelle: "Koeppen GPM Teil 2 Folien 23-29"
aktualisiert: 2026-08-05
---


# Risikomanagement

**Ziel:** Identifikation der größten Risiken und Definition von Maßnahmen zu ihrer Reduktion.

## Drei Phasen

1. Risikoidentifizierung
2. Risikobewertung
3. Risikoreduktion — präventive und korrektive Maßnahmen

## Risikoklassen (vgl. DIN IEC 61511-3)

- technisch
- organisatorisch
- persönlich
- finanziell
- terminlich

Diese Klassen sind im Feld `klasse` jeder Risikonote hinterlegt.

## Risikomatrix

|  | Schadenshöhe niedrig | Schadenshöhe hoch |
|---|---|---|
| **Schadenswahrscheinlichkeit hoch** | Monitor | **Act!** |
| **Schadenswahrscheinlichkeit niedrig** | Ok | Monitor |

Im Repository: `wahrscheinlichkeit` und `schadenshoehe` je 1–3, `risikozahl` = Produkt, `zone` = `ok` (< 3), `monitor` (3–5), `act` (≥ 6).

## Maßnahmen

| Typ | Wirkung |
|---|---|
| **präventiv** | kann Schadenswahrscheinlichkeit **und** Schadenshöhe verringern |
| **korrektiv** | kann **nur** die Schadenshöhe verringern |

Präventive Maßnahmen sind zu bevorzugen. Korrektive Maßnahmen sind erforderlich, wenn präventive nicht möglich, nicht ausreichend oder unverhältnismäßig sind.

## Anforderungen an die Abgabe

- Auf die **fünf wichtigsten** Risiken einigen.
- Im Statusbericht nicht nur Titel, sondern **konkrete Beschreibung** des Risikos.
- Je Risiko **eine konkrete Maßnahme**, konkret erläutert.
- Je Maßnahme **ein:e Verantwortliche:r** aus dem Team.
- Je Maßnahme angeben: präventiv oder korrektiv, und ob sie Wahrscheinlichkeit und/oder Höhe reduziert.

→ Register: [[Risikoregister]]
