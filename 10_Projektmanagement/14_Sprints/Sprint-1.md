---
typ: sprint
nummer: 1
titel: "Sprint 1"
status: abgeschlossen
start: 2026-08-10
ende: 2026-08-23
kapazitaet_h: 146
geplant_h: 143
sprintziel: "V-F1 und V-W1 ausgewertet, Bauteilkonzept freigegeben"
bereich: gpm
tags:
  - gpm
  - sprint
aktualisiert: 2026-08-27
---


# Sprint 1 (2026-08-10 – 2026-08-23)

> Termine nach **Variante B** des [[Ablaufplan]]s (im Team beschlossen).
> Planning: Mo 10.08.2026 · Review + Retro: Mo 24.08.2026 · Abstimmung Prof. Pähler: Mo 10.08.2026 (Kick-off, Bauteilfreigabe F14, [[TASK-012]])

## Sprintziel

**Die beiden Materialgrundlagen stehen und das Bauteil ist freigegeben.**

Konkret am 23.08.2026 erfüllt, wenn:

1. **V-F1 ist ausgewertet** — eine reproduzierbare Sandrezeptur (Vogelsand-Marke, Ölanteil, Verdichtung) ist dokumentiert und in [[E04]] eingetragen.
2. **V-W1 ist ausgewertet** — Aufheizkurve und Gießtemperaturfenster für Reinzinn liegen mit Thermoelement gemessen vor, [[E09]] ist entschieden.
3. **Das Bauteilkonzept ist von Prof. Pähler freigegeben** und damit eingefroren (F14).

Warum diese drei: Sie lösen die Blockaden mit der größten Reichweite. Ohne Sandrezeptur ist kein Kern-, Trennmittel- und Fehlerversuch planbar; ohne Temperaturfenster kein Abguss; ohne freigegebenes Bauteil keine finale Konstruktion.

## Kapazität

| Größe | Wert |
|---|---|
| Teamkapazität rechnerisch (3 Personen × 2 Wochen) | ≈ 146 h |
| eingeplant (Summe `aufwand_h`, Referenzschätzung) | **143 h** |
| Auslastung | 98 % |
| Anzahl Aufgaben | **12** (Richtwert 10–15 ✅) |

| Person | eingeplant | ≈ pro Woche |
|---|---|---|
| Jonas Gebert | 50 h | 25 h |
| Fynn Barmwater | 47 h | 23,5 h |
| Paul Wettering | 46 h | 23 h |

> ⚠️ **98 % Auslastung ist kein Puffer.** Jede Störung im Sprint schlägt direkt auf das Sprintziel durch. Bewusst so geplant, weil die Pufferwoche am Projektende liegt ([[Ablaufplan]] Variante B) — bei Störungen wird nach Priorität gekürzt, nicht der Sprint verlängert.
> ⚠️ Alle Werte sind **Referenzschätzungen** (`schaetzung: referenz`). Nach dem Planning Poker überschreiben und auf `schaetzung: poker` setzen.

## Sprint Backlog — 12 Aufgaben

| # | Aufgabe | h | Wer | Woche |
|---|---|---|---|---|
| 1 | [[TASK-018]] Beschaffung, v. a. Thermoelement Typ K | 8 | Fynn | **1 — Tag 1** |
| 2 | [[TASK-001]] Projektauftrag unterschreiben lassen | 10 | Jonas | 1 (bis 12.08.) |
| 3 | [[TASK-002]] Ablaufplan einreichen | 8 | Jonas | 1 (bis 12.08.) |
| 4 | [[TASK-041]] Unterweisung und Versicherung bei Göpfert klären | 8 | Paul | 1 |
| 5 | [[TASK-012]] Abstimmungstermin Prof. Pähler (F14/F16/F17/F7b/F25/F27) | 14 | Fynn | 1 (Anfrage Tag 1) |
| 6 | [[TASK-016]] Formkästen vermessen | 10 | Paul | 1 |
| 7 | [[TASK-024]] V-F1 Sandrezeptur | 20 | Fynn | 1 |
| 8 | [[TASK-019]] Fachbuch Fritz/Schulze [Q1] beschaffen | 5 | Fynn | 1 |
| 9 | [[TASK-017]] Ofen dokumentieren, Aufheizkurve | 12 | Paul | 2 |
| 10 | [[TASK-025]] V-W1 Ofen- und Temperaturverhalten | 16 | Paul | 2 |
| 11 | [[TASK-021]] Parametrisches CAD-Modell | 20 | Jonas | 2 |
| 12 | [[TASK-042]] Ausstattungsvergleich Göpfert ↔ FtT-Labor | 12 | Jonas | 2 |

### Kritischer Pfad

```
TASK-018 (Bestellung Thermoelement, Tag 1)
    └─> TASK-025 V-W1  ──┐
TASK-024 V-F1 ───────────┼─> Sprintziel
TASK-012 Freigabe F14 ───┘
    └─> TASK-021 CAD (braucht auch TASK-016)
```

**Geht die Bestellung aus [[TASK-018]] nicht am 10.08. raus, ist Sprintziel 2 nicht erreichbar.** Das ist der einzige Punkt im Sprint, an dem ein einzelner verpasster Tag das Ziel kippt.

### Zwei Aufgaben am Zuschnittsmaximum

[[TASK-021]] (CAD) und [[TASK-024]] (V-F1) liegen mit je 20 h auf der Obergrenze. Im Planning prüfen, ob geteilt wird:

- TASK-021 → „Bauteil + Kern" (12 h) und „Kernkasten + Modell" (10 h)
- TASK-024 → „Siebanalyse und Aufbereitung" (8 h) und „Rezepturvariation und Festigkeitsbewertung" (12 h)

Vorteil der Teilung: feinerer Burndown, früher sichtbarer Fortschritt. Nachteil: zwei Karten mehr, Sprint läge bei 14 Aufgaben — noch im Rahmen.

### Bewusst nicht in Sprint 1

| Aufgabe | Grund |
|---|---|
| [[TASK-031]] Gefährdungsbeurteilung | 12 h → Sprint läge bei 155 h. Freigabevoraussetzung ist sie erst für den HAW-Betrieb; für Göpfert deckt [[TASK-041]] den Bedarf. Sprint 2, Position 1. |
| [[TASK-026]] V-K1, [[TASK-027]] V-S1, [[TASK-028]] V-T1 | brauchen die Sandrezeptur aus V-F1 |
| [[TASK-029]] V-G1…G9, [[TASK-030]] V-Z1 | brauchen gelingende Abgüsse |
| [[TASK-023]] finale Bauteilmaße | blockiert durch V-S1 |
| [[TASK-022]] Probedruck | braucht CAD-Modell |
| [[TASK-032]] Versuchsskript, [[TASK-020]] Normen, [[TASK-033]] Quellen-Tags | niedrigere Priorität |

## Sprint Backlog

Alle Aufgaben mit `sprint: 1` und `status: sprint-backlog` / `in-arbeit` / `erledigt`.

### Live-Ansicht

```base
filters:
  and:
    - 'typ == "aufgabe"'
    - 'sprint == 1'
views:
  - type: table
    name: "Sprint 1"
    groupBy:
      property: note.status
      direction: ASC
    order:
      - file.name
      - titel
      - verantwortlich
      - aufwand_h
      - schaetzung
    summaries:
      note.aufwand_h: Sum
```

## Sprint Planning

- **Datum:** Mo 10.08.2026 (Kick-off + Planning 1) · Vorbereitung in GPM Teil 3, Fr 07.08.2026
- **Teilnehmende:** Paul Wettering (Scrum Master, Moderation), Fynn Barmwater (Product Owner), Jonas Gebert
- **Planning Poker:** für alle 12 Aufgaben durchzuführen. Referenzschätzungen liegen als Ausgangswert in den Aufgabennotizen. Ablauf: [[Planning-Poker]]
- **Zu klären im Planning:**
  - [ ] Werden TASK-021 und TASK-024 geteilt?
  - [ ] Ist die Fahrzeit nach Heide in den Schätzungen enthalten? ([[R14]], F28)
  - [ ] Wer fährt wann nach Heide — Versuchstage bündeln
  - [ ] 98 % Auslastung: Welche Aufgabe fliegt zuerst, wenn es klemmt? *(Vorschlag: TASK-019, dann TASK-042)*

## Sprint Review

- **Datum:** Mo 24.08.2026 · **Teilnehmende:** Paul Wettering (Scrum Master), Fynn Barmwater (Product Owner), Jonas Gebert. Prof. Pähler nicht anwesend — sein Feedback wurde im Abstimmungstermin am 17.08. eingeholt.
- **Sprintziel erreicht?** ☑ ja ☐ teilweise ☐ nein — alle drei Bedingungen erfüllt.

| # | Bedingung | Ergebnis |
|---|---|---|
| 1 | V-F1 ausgewertet, Sandrezeptur dokumentiert | ✅ Rezeptur steht, in [[E04]] eingetragen |
| 2 | V-W1 ausgewertet, Aufheizkurve und Gießtemperaturfenster gemessen | ✅ mit Thermoelement Typ K gemessen, [[E09]] entschieden |
| 3 | Bauteilkonzept von Prof. Pähler freigegeben | ✅ am 17.08.2026, Variante **Stehbuchse mit Fußplatte** (F33), damit auch F14 und F17 beantwortet |

- **Nicht fertig geworden:** [[TASK-021]] parametrisches CAD-Modell (20 h). Bis zur Bauteilfreigabe am 17.08. blockiert, danach nicht mehr abschließbar. Geht vollständig in Sprint 2.
- **Feedback des Product Owners:** Sprintziel inhaltlich erfüllt; die Aushebbarkeitsprüfung wird als eigenständiges Ergebnis gewertet, weil sie zwei fehlerhafte Entwürfe vor dem Modellbau abgefangen hat.

## Sprint Retrospective

| Was lief gut? | Was lief nicht gut? | Maßnahme für den nächsten Sprint | Verantwortlich |
|---|---|---|---|
| Vorversuche bei Göpfert ohne Terminreibung; V-F1 und V-W1 an je einem Tag durchgezogen | Aushebbarkeit wurde erst nach zwei verworfenen Entwürfen geprüft | Aushebbarkeitsprüfung (`check_aushebbarkeit.py`) ist verbindliches Gate, bevor ein CAD-Modell beginnt | Jonas Gebert |
| Beide GPM-Abgaben termingerecht am 12.08. raus | Terminanfrage an Prof. Pähler ging erst am Sprintstart raus, Kennzahl lief auf gelb | Feste 14-Tage-Taktung mit dem Auftraggeber; Anfrage jeweils am ersten Sprinttag | Fynn Barmwater |
| Kennzahlen (Burndown, weiches Kriterium, Barometer) wurden durchgehend gepflegt | Ein 20-h-Paket blockierte den ganzen Sprint sichtbar | TASK-021 in zwei Pakete teilen; ab Sprint 2 keine Aufgabe über 15 h, wenn sie an einer offenen Frage hängt | Paul Wettering |

## Burndown

→ [[Burndown-Chart]], Datenblatt `Burndown-Sprint-1`
