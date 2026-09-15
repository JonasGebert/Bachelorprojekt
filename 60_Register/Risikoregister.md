---
typ: uebersicht
titel: "Risikoregister"
bereich: beide
tags:
  - risiko
  - uebersicht
aktualisiert: 2026-08-28
---


# Risikoregister

> Methode: [[Risikomanagement-Methode]]. Sicherheitsrisiken für **Personen** stehen nicht hier, sondern in [[Arbeitssicherheit]] (G1–G10). Hier: Risiken für den **Projekterfolg**.
> Bewertung: Schadenswahrscheinlichkeit (W) × Schadenshöhe (H), Skala je 1–3. Zone: `ok` (< 3) · `monitor` (3–5) · `act` (≥ 6).

![[Risikomatrix.base]]

## Risikomatrix

![[Risikomatrix_Sprint-1.png]]

*Abbildung: Risikomatrix nach Koeppen, Stand 28.08.2026. Ausgearbeitetes Kapitel: [[Statusbericht-1]], Abschnitt 2.4.*


| W \ H | 1 (niedrig) | 2 (mittel) | 3 (hoch) |
|---|---|---|---|
| **3 (hoch)** | monitor | **act** | **act** |
| **2 (mittel)** | ok/monitor | monitor | **act** |
| **1 (niedrig)** | ok | ok | monitor |

## Aktuelle Top-Risiken (Zone „act")

[[R13]] (9) · [[R02]] (6) · [[R07]] (6) · [[R09]] (6) · [[R10]] (6) · [[R14]] (6) · [[R15]] (6)

> **[[R13]] ist mit Risikozahl 9 das höchstbewertete Risiko im Projekt.** Es entsteht direkt aus [[E10]]: Die Vorversuche laufen unter anderen Bedingungen als der spätere Laborversuch. Ein Versuch, der bei Göpfert reproduzierbar ist, kann im FtT-Labor scheitern — und das fällt erst bei der Generalprobe V-Z1 auf, also spät.

## Die fünf Risiken für den Statusbericht

GPM verlangt eine Einigung auf die **fünf wichtigsten** Risiken. Sieben liegen bei einer Risikozahl ≥ 6 — ausgewählt wurde nach Risikozahl, Bedrohung des Projektziels und Abdeckung unterschiedlicher Risikoklassen.

| # | Risiko | W × H | Klasse | Maßnahmentyp | Verantwortlich |
|---|---|---|---|---|---|
| 1 | [[R13]] Transferrisiko Göpfert ↔ FtT-Labor | **9** | technisch | präventiv | Jonas Gebert |
| 2 | [[R10]] Vogelsand + Speiseöl ungeeignet | 6 | technisch | präventiv | Fynn Barmwater |
| 3 | [[R09]] Gefährdungsbeurteilung zu spät → keine Freigabe | 6 | organisatorisch | präventiv | Paul Wettering |
| 4 | [[R07]] Deadline 04.10.2026 wird gerissen | 6 | terminlich | präventiv | Fynn Barmwater |
| 5 | [[R02]] Zeitbudget 3 h reicht nicht für 2 Abgüsse | 6 | terminlich | präventiv | Paul Wettering |

**Nicht in den Top 5, obwohl Risikozahl 6:**

- [[R15]] (Sicherheit im Fremdbetrieb) wird durch [[TASK-041]] bereits in Sprint 1 aufgelöst — die Eintrittswahrscheinlichkeit sinkt binnen zwei Wochen auf 1.
- [[R14]] (Fahrzeit nach Heide) ist über die Aufwandsschätzung bereits eingepreist und wirkt damit nicht mehr unerkannt.

Beide bleiben im Register und werden im Sprint Review neu bewertet.

## Entfallene Risiken

| ID | Risiko | Grund |
|---|---|---|
| R01 | Kochplatte erreicht Gießtemperatur nicht | entfallen 04.07.2026 — Nabertherm-Ofen 5,5 kW, siehe [[E06]] |
| R03 | Materialkosten sprengen Budget | entfallen 04.07.2026 — Budget unkritisch (F2), Reinzinn mit Vollrecycling |

## Review

Risiken bei jedem Sprint Review neu bewerten, Änderungen in [[Projektlog]] notieren.
