---
typ: controlling
titel: "Weiches Kriterium zur Fortschrittskontrolle"
bereich: gpm
status: definiert
verantwortlich: "Jonas Gebert"
nullpunkt: 2026-08-03
aelteste_offene_frage_seit: 2026-08-21
aktualisiert: 2026-08-27
tags:
  - gpm
  - controlling
---

# Weiches Kriterium zur Fortschrittskontrolle

> Weiche Messgrößen sind ein **Frühwarnsystem** für die harten Messgrößen. Anders als das [[Team-Management-Barometer]] brauchen sie eine **objektive Messvorschrift**, keine subjektive Einschätzung. Methodik: [[Projektcontrolling]].
> Verantwortlich: Jonas Gebert, gemeinsam mit dem [[Statusbericht-Vorlage|One Pager]].

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

Erhebung: in jedem Weekly (Di und Do) durch den Verantwortlichen (Jonas Gebert).

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
| 🟡 gelb | Der Verantwortliche prüft, ob nachgefasst werden muss, und benennt eine:n Verantwortliche:n je Frage |
| 🔴 rot | **zwingend:** Nachfassen mit konkreter Frist. Zusätzlich prüfen, ob die blockierte Aufgabe umgangen werden kann — etwa durch eine dokumentierte Arbeitsannahme, die bei Antwort revidiert wird. Eskalation an den Product Owner. |

## Verlauf

Erhebung im Weekly (Mo und Fr) durch Jonas Gebert.

| Datum | Älteste offene Hoch-Prio-Frage | Alter [d] | Status | Maßnahme |
|---|---|---|---|---|
| 2026-08-05 | F14, F15, F17, F19 | 2 | 🟢 grün | keine — [[TASK-012]] für Sprint 1 eingeplant |
| 2026-08-10 | F14, F15, F17 | 7 | 🟢 grün | keine — Terminanfrage an Prof. Pähler am Sprintstart raus |
| 2026-08-14 | F14, F15, F17 | 11 | 🟡 gelb | nachgefasst; Termin auf Mo 17.08. bestätigt |
| 2026-08-17 | F14, F15, F17 | 14 | 🟡 gelb | Abstimmungstermin fand statt — F14, F16, F17, F7b, F23, F25 und F27 beantwortet |
| 2026-08-21 | keine externe Hoch-Prio-Frage offen | 0 | 🟢 grün | — |

### Auswertung Sprint 1

Der Verlauf ist grün → gelb → gelb → grün. Das Kriterium hat genau das geleistet, wofür weiche Messgrößen gedacht sind: Es zeigte am 14.08. an, dass der Abstimmungstermin zu spät lag, **während** das Nachfassen noch drei Tage kostete. Ohne die Kennzahl wäre der Termin vermutlich in die zweite Sprintwoche gerutscht, und die Bauteilfreigabe hätte den Sprint gekippt.

Der Rückfall auf grün am 21.08. ist kein Selbstläufer: Er entstand durch die Maßnahme, nicht durch Zeitablauf. Für Sprint 2 gilt die daraus abgeleitete Regel — die Terminanfrage an den Auftraggeber geht am **ersten Sprinttag** raus, nicht wenn die Frage akut wird.

**Präzisierung der Messvorschrift (17.08.2026):** Gezählt werden nur Fragen, die von **außerhalb des Teams** beantwortet werden müssen — Prof. Pähler, FtT-Labor, Firma Göpfert. Fachliche Fragen, die das Team selbst über einen Vorversuch beantwortet (etwa F12, Kernbinder), sind keine Wartezeit, sondern Arbeit. Sie zählen ab jetzt nicht mehr in die Kennzahl.
