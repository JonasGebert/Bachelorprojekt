---
typ: controlling
titel: "Team-Management-Barometer"
bereich: gpm
verantwortlich: "Paul Wettering"
tags:
  - gpm
  - controlling
  - team
aktualisiert: 2026-09-13
---


# Team-Management-Barometer

> **In jedem Daily/Weekly erheben** und als Graph (Barograph) über der Zeit darstellen. Bewertung erfolgt **verdeckt**, die/der Verantwortliche sammelt ein und stellt dem Team vor.
> **Achtung Diagrammtyp:** Die Grafik braucht eine echte Datums-/xy-Achse, keine Kategorieachse mit gleich breiten Abständen — sonst stimmt der zeitliche Abstand zwischen den Erhebungsterminen nicht (Bewertung Statusbericht 1, Runde 1: „Vermutlich wurde ein Liniendiagramm statt xy-Graph verwendet"). 10.08. → 17.08. sind 7 Tage, 17.08. → 21.08. sind nur 4 Tage — das muss sich in der Punktabstand-Breite widerspiegeln.
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
| 2026-08-17 | Weekly | 5,3 | 5,0 | **2,7** | **3,7** | Arbeitsfortschritt gefallen (CAD durch F33 blockiert) → Bauteilentscheidung als erster Punkt im Review |
| 2026-08-21 | Weekly, letzter Sprinttag | 5,3 | 5,3 | **3,0** | 4,3 | AG-Einbindung bleibt niedrigster Wert → festes Berichtswesen mit Prof. Pähler vereinbaren (kurzer Statusmail-Turnus je Sprintwechsel) |

### Auswertung Sprint 1

Die Absolutwerte sind wenig aussagekräftig, die **Tendenz** ist es.

**Teammotivation und Zielausrichtung** liegen durchgehend im oberen Bereich (5,0–5,3) und steigen leicht — die Rollenverteilung vom 05.08. und das geschärfte Sprintziel wirken.

Der **Arbeitsfortschritt** fiel zwischenzeitlich (4,0 → 3,7). Ursache war die blockierte CAD-Aufgabe, nicht die Arbeitsmenge — sichtbar auch im [[Burndown-Chart]], das im selben Zeitraum weiterlief. Nach der Bauteilentscheidung erholt sich der Wert auf 4,3.

Die **Auftraggebereinbindung** ist über den gesamten Sprint das schwächste Kriterium (2,7 / 2,7 / 3,0). Der Kontakt zu Prof. Pähler beschränkt sich bisher auf Einzeltermine ohne festen Turnus; ein abgesprochenes Berichtswesen im Sinne der Kriteriendefinition existiert nicht. Das ist konsistent mit dem [[Weiches-Kriterium|weichen Kriterium]] (Alter der ältesten offenen Hoch-Prio-Frage) und mit [[R13]]: offene Fragen, die nur der Auftraggeber entscheiden kann, bleiben lange liegen.

**Maßnahme für Sprint 2 (präventiv, verantwortlich Fynn Barmwater):** fester Abstimmungsrhythmus zum Sprintwechsel — Kurzstatus per Mail montags, Präsenztermin zum Sprint Review. Zielwert für die nächste Erhebung: ≥ 4,0.

## Bekannte Risiken der Methode

- Unterschiedliche Interpretation der Fragen → **vorher klären**.
- Absolutwerte nur bedingt aussagekräftig — die **Tendenz** ist wichtiger.
- Zu positive Antworten aus Furcht vor Konsequenzen, zu negative aus Unmut → als **Diskussionsgrundlage** verwenden, Werte hinterfragen.
- Bei schlechten Werten Maßnahmen ergreifen, aber **kein blinder Aktionismus, keine Vorwürfe** — sonst wird nicht mehr ehrlich geantwortet.
