---
typ: meta
titel: "Arbeitsrhythmus — was wann zu tun ist"
bereich: beide
tags:
  - meta
  - anleitung
aktualisiert: 2026-08-05
---

# Arbeitsrhythmus — was wann zu tun ist

> Diese Notiz beantwortet genau eine Frage: **Was muss ich heute tun, damit das Projekt läuft?**
> Wenn du dich verloren fühlst, ist das hier die einzige Seite, die du brauchst.

## Zuerst die Entwarnung

Der Vault hat rund 145 Notizen. **Gepflegt werden müssen davon etwa 20.**

| Was | Umfang | Aufwand |
|---|---|---|
| **Lebendig** — wird laufend geändert | Aufgaben im Sprint, Sprintnotiz, Burndown, Barometer, weiches Kriterium, Inbox, Versuchsnotizen | siehe unten |
| **Anlassbezogen** — nur wenn etwas passiert | Entscheidungen, Risiken, offene Fragen, Projektlog | Minuten, wenn es eintritt |
| **Nachschlagewerk** — wird gelesen, nicht gepflegt | Wissensbasis, Quellen, GPM-Kursunterlagen, Vorlagen, Konventionen | **null** |

Die dritte Gruppe ist die größte. Sie macht keine Arbeit.

---

## Täglich — an Tagen, an denen gearbeitet wurde · **2 Minuten**

| Was | Wer |
|---|---|
| Aufgabe angefangen → `status: in-arbeit` · Aufgabe fertig → `status: erledigt` | jede:r für die eigenen Karten |
| Eine Zahl ins Burndown-Datenblatt: verbleibende Stunden | Paul |
| Gedanken, die zwischendurch kommen → eigene [[Inbox]] | jede:r |

**Nicht zu viele Karten gleichzeitig auf `in-arbeit`.** Zwei pro Person ist die Obergrenze, sonst ist der Burndown nur noch Dekoration.

An **Versuchstagen bei Göpfert** zusätzlich: Tagesnotiz mitschreiben, Messwerte noch am selben Tag in die Versuchsnotiz übertragen — mit Messmittel und Messunsicherheit. Rohdaten, die drei Tage liegen, sind nicht mehr auswertbar.

---

## Zweimal pro Woche — Weekly, Di und Do · **20 Minuten**

Feste Reihenfolge, dann dauert es auch wirklich nur 20 Minuten:

1. **Runde:** Jede:r sagt drei Sätze — was seit dem letzten Mal, was bis zum nächsten Mal, was blockiert.
2. **Barometer:** vier Zahlen von 1 bis 6, verdeckt. Paul mittelt und trägt ein. *(3 min)*
3. **Weiches Kriterium:** eine Zahl — Alter der ältesten offenen Hoch-Prio-Frage. Jonas trägt ein. *(1 min)*
4. **Inbox leeren:** Jede:r geht die eigene Inbox durch, verteilt nach der Routing-Tabelle in [[Inbox]]. Neue Aufgaben bekommen `status: product-backlog` — **nie** in den laufenden Sprint.
5. **Git:** alle pullen, alle pushen.

Das ist die Mindestvorgabe aus GPM: mindestens zweimal pro Sprint **und** mindestens wöchentlich.

---

## Alle zwei Wochen — Sprintwechsel, montags · **2 bis 3 Stunden**

Am Sprintende in dieser Reihenfolge:

| Schritt | Dauer | Wer | Ergebnis landet in |
|---|---|---|---|
| **Sprint Review** — Ergebnisse vorstellen, Sprintziel erreicht? | 45 min | alle + Prof. Pähler | Sprintnotiz, Abschnitt „Sprint Review" |
| **Retrospektive** — was lief gut, was nicht, eine Maßnahme | 30 min | nur Team | Sprintnotiz, Abschnitt „Retrospective" |
| **Risiken neu bewerten** — W und H der fünf Top-Risiken prüfen | 15 min | alle | `60_Register/Risiken/` |
| **Sprint Planning** — Aufgaben auswählen, Planning Poker | 60 min | alle, Jonas moderiert | neue Sprintnotiz |
| **Burndown zurücksetzen** — neues Datenblatt, neuer Startwert | 5 min | Paul | [[Burndown-Chart]] |

Danach, **innerhalb einer Woche:** Statusbericht als One Pager an Prof. Koeppen. Jonas schreibt, zieht die Inhalte aus Sprintnotiz, Burndown und Risikoregister zusammen — es wird nichts neu erfasst.

---

## Anlassbezogen — wenn es eintritt, nicht nach Kalender

| Ereignis | Was zu tun ist |
|---|---|
| Vorversuch durchgeführt | Versuchsnotiz aus [[Vorlage-Versuch]] anlegen und vollständig ausfüllen |
| Technische Festlegung getroffen | Entscheidung `E##` anlegen — Kontext, Alternativen, Begründung |
| Neues Risiko erkannt | `R##` anlegen, bewerten, Maßnahme und Verantwortliche:n benennen |
| Frage an Prof. Pähler oder Göpfert | Zeile in [[Offene-Fragen]] |
| Meilenstein, größere Weichenstellung | Eintrag oben in [[Projektlog]] |

---

## Wer macht was

| | Jonas | Fynn | Paul |
|---|---|---|---|
| Rolle | Scrum Master | Product Owner | Teammitglied |
| Weekly | moderiert | | |
| täglich | eigene Karten | eigene Karten | eigene Karten **+ Burndown** |
| Weekly-Erhebung | weiches Kriterium | | Barometer |
| Sprintwechsel | moderiert Planning + Retro | priorisiert Backlog, führt Review | setzt Burndown zurück |
| nach dem Sprint | **Statusbericht** | | |
| Fachlich | Konstruktion, CAD, Versuchsskript | Formstoffe, V-F1/V-K1/V-T1 | Werkstoff, Schmelze, V-W1/V-S1, Arbeitssicherheit |

---

## Wenn es eng wird

Es wird Wochen geben, in denen nichts davon passiert. Dann gilt: **diese drei Dinge dürfen nicht ausfallen**, weil sie benotet werden und sich nicht rückwirkend erfinden lassen.

1. **Burndown täglich** — eine Zahl. Eine nachträglich konstruierte Kurve sieht man ihr an.
2. **Barometer im Weekly** — vier Zahlen. Lässt sich nicht nachholen, es ist eine Momentaufnahme.
3. **Statusbericht nach jedem Sprint** — feste Frist bei Prof. Koeppen.

Alles andere lässt sich aufholen. Diese drei nicht.

---

## Was du getrost ignorieren kannst

- `40_Wissensbasis/`, `50_Quellen/`, `10_Projektmanagement/19_GPM-Kurs/` — Nachschlagewerk, kein Pflegeaufwand
- `00_Meta/Vorlagen/` — nur beim Anlegen neuer Notizen relevant
- `tools/`, `.github/` — läuft von selbst
- Das Web-Dashboard — es baut sich automatisch, du musst dort nie etwas eintragen

**Und wenn du nicht weißt, was ansteht:** frag Claude „Was haben wir noch zu tun?" — die Antwort kommt aus Fristen, laufendem Sprint, Blockaden und offenen Fragen, in dieser Reihenfolge.
