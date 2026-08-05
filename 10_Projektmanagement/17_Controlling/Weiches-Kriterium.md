---
typ: controlling
titel: "Weiches Kriterium zur Fortschrittskontrolle"
bereich: gpm
status: definiert
verantwortlich: "Jonas Gebert"
nullpunkt: 2026-08-03
aelteste_offene_frage_seit: 2026-08-03
aktualisiert: 2026-08-05
tags:
  - gpm
  - controlling
---

# Weiches Kriterium zur Fortschrittskontrolle

> Weiche Messgrößen sind ein **Frühwarnsystem** für die harten Messgrößen. Anders als das [[Team-Management-Barometer]] brauchen sie eine **objektive Messvorschrift**, keine subjektive Einschätzung. Methodik: [[Projektcontrolling]].
> Verantwortlich: Jonas Gebert (Scrum Master), gemeinsam mit dem [[Statusbericht-Vorlage|One Pager]].

## Gewähltes Kriterium

**Alter der ältesten unbeantworteten Klärungsfrage mit Priorität „hoch"** aus [[Offene-Fragen]], in Kalendertagen.

### Warum dieses Kriterium

Das Lehrbeispiel der Vorlesung ist die Reaktionszeit auf Anfragen des Scrum Masters. Für dieses Projekt ist das der falsche Indikator: Das Team arbeitet bei der Firma Göpfert vor Ort zusammen, teaminterne Reaktionszeiten sind unkritisch.

Was das Projekt tatsächlich bremst, sind **unbeantwortete Fragen an Dritte** — an Prof. Pähler, an das FtT-Labor, an die Firma Göpfert. Genau diese Fragen blockieren Konstruktion, Beschaffung und Gefährdungsbeurteilung. Mehrere Aufgaben im Backlog haben ein `blockiert_durch`, das auf eine offene Frage zurückgeht.

Das Kriterium ist zudem **ohne Zusatzaufwand messbar**: Der Wert lässt sich direkt aus [[Offene-Fragen]] ablesen.

## Messvorschrift

**Alter einer Frage** = Tage seit dem **späteren** dieser beiden Zeitpunkte:

1. dem Tag, an dem die Frage erfasst wurde, und
2. dem **Projektstart 03.08.2026** (Beginn des Moduls, GPM Teil 1)

| Status | Bedingung |
|---|---|
| 🟢 grün | älteste offene Hoch-Priorität-Frage ist **≤ 7 Tage** alt |
| 🟡 gelb | **8 bis 14 Tage** |
| 🔴 rot | **> 14 Tage** |

Erhebung: in jedem Weekly (Di und Do) durch den Scrum Master.

> **Für das Dashboard:** Das Feld `aelteste_offene_frage_seit` im Frontmatter dieser Notiz steuert die Anzeige auf der Webseite. Wird eine der Fragen beantwortet, wird das Feld auf das Datum der nächstältesten offenen Hoch-Prio-Frage gesetzt — oder auf das heutige Datum, wenn keine mehr offen ist. Das ist der einzige Handgriff, den die Kennzahl braucht.

### Warum der Nullpunkt auf dem Projektstart liegt

Die Wissensbasis, das Bauteilkonzept und die Fragen F1–F19 sind am 04.07.2026 entstanden — **vier Wochen vor Modulbeginn, aus Eigeninitiative**. Diese Zeit gegen das Projekt zu rechnen wäre in zweifacher Hinsicht falsch:

- Es gab vor dem 03.08.2026 kein Projekt, keinen Auftrag und keine Verpflichtung des Auftraggebers zu antworten. Eine Kennzahl, die Zeit vor dem eigenen Nullpunkt zählt, misst nicht das System, das sie steuern soll.
- Sie würde eine Vorleistung als Versäumnis darstellen. Für den Statusbericht ist die Vorarbeit ein **Aktivposten**, kein Rückstand.

### Warum das Kriterium trotzdem scharf bleibt

Der Nullpunkt verschiebt sich, die Regel nicht. Eine Frage, die seit Projektstart offen ist und nicht gestellt wurde, altert weiter — genau wie eine gestellte, auf die keine Antwort kommt. Das ist beabsichtigt: **Beides bremst das Projekt gleich stark.** Ein Kriterium, das nur gestellte Fragen zählt, ließe sich trivial grün halten, indem man einfach nicht fragt.

## Maßnahmen

| Status | Maßnahme |
|---|---|
| 🟢 grün | keine |
| 🟡 gelb | Scrum Master prüft, ob nachgefasst werden muss, und benennt eine:n Verantwortliche:n je Frage |
| 🔴 rot | **zwingend:** Nachfassen mit konkreter Frist. Zusätzlich prüfen, ob die blockierte Aufgabe umgangen werden kann — etwa durch eine dokumentierte Arbeitsannahme, die bei Antwort revidiert wird. Eskalation an den Product Owner. |

## Verlauf

| Datum | Älteste offene Hoch-Prio-Frage | Alter [d] | Status | Maßnahme |
|---|---|---|---|---|
| 2026-08-05 | F14, F15, F17, F19 | **2** | 🟢 **grün** | keine — [[TASK-012]] ist für Sprint 1 eingeplant |

### Erste Messung — Auswertung

**2 Tage, Status grün.** Die vier Fragen wurden zwar am 04.07.2026 erfasst, das Projekt läuft aber erst seit dem 03.08.2026. Gemessen wird ab Nullpunkt.

### Prognose — hier wird es unbequem

Die vier Fragen sind mit dem Nullpunkt vom 03.08. gekoppelt und altern ab jetzt:

| Datum | Alter | Status | was dann gilt |
|---|---|---|---|
| 10.08.2026 | 7 d | 🟢 gerade noch grün | Sprintstart, [[TASK-012]] beginnt |
| **11.08.2026** | 8 d | 🟡 **gelb** | Scrum Master muss nachfassen |
| **18.08.2026** | 15 d | 🔴 **rot** | Maßnahme zwingend, Eskalation an den Product Owner |
| 24.08.2026 | 21 d | 🔴 rot | Sprint Review — Status geht so in [[Statusbericht-1]] |

Damit hat das Kriterium eine harte Konsequenz: **Der Abstimmungstermin mit Prof. Pähler muss in der ersten Sprintwoche stattfinden, nicht in der zweiten.** Findet er erst nach dem 17.08. statt, steht im ersten Statusbericht an den Auftraggeber ein rotes weiches Kriterium — und die Ursache ist eine Terminanfrage, die zu spät rausging.

Das ist genau die Frühwarnung, für die weiche Messgrößen gedacht sind: Sie zeigt das Problem, während es noch drei Tage kostet, und nicht erst, wenn es zwei Wochen kostet.
