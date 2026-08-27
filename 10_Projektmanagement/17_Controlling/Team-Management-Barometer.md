---
typ: controlling
titel: "Team-Management-Barometer"
bereich: gpm
verantwortlich: "Paul Wettering"
tags:
  - gpm
  - controlling
  - team
aktualisiert: 2026-08-27
---


# Team-Management-Barometer

> **In jedem Daily/Weekly erheben** und als Graph (Barograph) über der Zeit darstellen. Bewertung erfolgt **verdeckt**, die/der Verantwortliche sammelt ein und stellt dem Team vor.
> **Verantwortlich: Paul Wettering** (zugleich Scrum Master). Zielkonflikt und kompensierende Kontrolle — verdeckte Abgabe, Auszählung durch **Fynn Barmwater**, Paul erhält nur den Mittelwert — siehe [[Rollen-und-Verantwortlichkeiten]], Abschnitt „Zielkonflikt".

## Erhebung — nur Mittelwerte werden gespeichert

**Ablauf:** Jede:r notiert die vier Werte (1–6) verdeckt auf Papier oder im Chat an Paul. Paul bildet die Mittelwerte und trägt **nur diese** in die Messreihe unten ein. Die Einzelzettel werden nicht archiviert.

> **Warum keine Einzelwerte im Repository:** Das Repository ist öffentlich. Eine Zeile „Paul: Teammotivation 2" wäre eine dauerhaft einsehbare, namentlich zuordenbare Bewertung einer Person. Für den Barograph im Statusbericht braucht Koeppen ohnehin nur den Mittelwert — die Einzelwerte dienen ausschließlich der Diskussion im Meeting und sind danach erledigt.

**Konsequenz für die Auswertung:** Ausreißer sieht man im Mittelwert nicht. Deshalb die Regel: Weichen die Einzelwerte eines Kriteriums um mehr als 2 Punkte voneinander ab, wird das **im Meeting besprochen** und das Ergebnis der Diskussion in der Spalte „Maßnahme" festgehalten — ohne Namensnennung.

> **Vorher klären, sonst misst ihr Rauschen:** Was heißt „Auftraggebereinbindung" konkret — Kontakt zu Prof. Pähler oder zum Product Owner Fynn? Da der Product Owner teamintern besetzt ist, muss das Team sich auf eine Lesart einigen. Empfehlung: **Prof. Pähler**, denn er ist der Kunde, dessen Einbindung das Risiko trägt.

## Die vier Kriterien (Skala 1–6)

| Kriterium | 1 = gering | 6 = sehr hoch |
|---|---|---|
| **Teammotivation** | Einzel-Interesse ermüdet, Wir-Gefühl schwach | jede:r zeigt vollen Einsatz, fühlt sich wohl, kann persönliche Interessen befriedigen |
| **Zielausrichtung** | Ziele kaum bekannt | Ziele von allen akzeptiert, jede:r steuert transparent seinen Zielbeitrag |
| **Auftraggebereinbindung** | kaum Kontakt zum AG, Kommunikation und Akzeptanz schwach | AG über abgesprochenes Berichtswesen persönlich eingebunden |
| **Arbeitsfortschritt** | große Zeitverzüge, fachliche Unklarheit | plankonforme Abarbeitung, alle Risiken bewertet und beherrschbar |

## Messreihe

Skala 1–6. Verdeckte Abgabe, Auszählung durch Fynn Barmwater, gespeichert werden **nur Mittelwerte**.

| Datum | Anlass | Motivation | Zielausrichtung | AG-Einbindung | Arbeitsfortschritt | Maßnahme |
|---|---|---|---|---|---|---|
| 2026-08-10 | Erstmessung, Sprintstart | 5,0 | 4,7 | **2,7** | 4,0 | AG-Einbindung mit Abstand niedrigster Wert → Abstimmungstermin mit Prof. Pähler priorisiert |
| 2026-08-17 | Weekly | 5,3 | 5,0 | 4,3 | **3,7** | Arbeitsfortschritt gefallen (CAD durch F33 blockiert) → Bauteilentscheidung als erster Punkt im Review |
| 2026-08-24 | Sprint Review | 5,3 | 5,3 | 4,7 | 4,3 | keine |

### Auswertung Sprint 1

Die Absolutwerte sind wenig aussagekräftig, die **Tendenz** ist es: Alle vier Kriterien steigen über den Sprint.

Der Ausschlag liegt bei der **Auftraggebereinbindung** — von 2,7 auf 4,7. Das deckt sich mit dem [[Weiches-Kriterium|weichen Kriterium]], das im selben Zeitraum von gelb auf grün wechselte. Zwei unabhängig erhobene Größen zeigen dieselbe Ursache: den Abstimmungstermin am 17.08.

Der **Arbeitsfortschritt** ist der einzige Wert, der zwischenzeitlich fiel (4,0 → 3,7). Ursache war die blockierte CAD-Aufgabe, nicht die Arbeitsmenge — sichtbar auch im [[Burndown-Chart]], das im selben Zeitraum weiterlief. Nach der Bauteilentscheidung erholt sich der Wert auf 4,3.

## Bekannte Risiken der Methode

- Unterschiedliche Interpretation der Fragen → **vorher klären**.
- Absolutwerte nur bedingt aussagekräftig — die **Tendenz** ist wichtiger.
- Zu positive Antworten aus Furcht vor Konsequenzen, zu negative aus Unmut → als **Diskussionsgrundlage** verwenden, Werte hinterfragen.
- Bei schlechten Werten Maßnahmen ergreifen, aber **kein blinder Aktionismus, keine Vorwürfe** — sonst wird nicht mehr ehrlich geantwortet.
