---
typ: rollen
titel: "Rollen und Verantwortlichkeiten"
status: festgelegt
bereich: gpm
tags:
  - gpm
  - team
  - rollen
aktualisiert: 2026-08-07
---


# Rollen und Verantwortlichkeiten

> **Besetzt am 2026-08-05.** Methodische Grundlage: [[Rollen-Methode]].

## Scrum-Rollen

| Rolle | Person | Anmerkung |
|---|---|---|
| Product Owner | **Fynn Barmwater** | teamintern besetzt (laut GPM zulässig). Verantwortlich für das Endprodukt, nimmt die Kundenrolle ein, trifft die finale Priorisierungsentscheidung im Backlog |
| Scrum Master | **Paul Wettering** | **Fynn scheidet aus:** der Product Owner darf laut GPM Teil 3 nicht zugleich Scrum Master sein. Verantwortlich für die Einhaltung der Scrum-Methodik, moderiert Sitzungen, ist **kein:e Projektleiter:in** |
| Teammitglied | Jonas Gebert | |
| Teammitglied | Fynn Barmwater | |
| Teammitglied | Paul Wettering | |
| Auftraggeber | Prof. Dr.-Ing. Dietmar Pähler | unterschreibt den Projektauftrag, Adressat der Sprint Reviews und Abstimmungstermine |

## Verantwortung für PM-Methoden (Pflichtzuordnung)

Jedes Teammitglied übernimmt mindestens eine Methode; der Scrum Master koordiniert die übrigen.

| Methode | Verantwortlich | Artefakt im Repository |
|---|---|---|
| Task Board inkl. Product- und Sprint-Backlog | **Fynn Barmwater** | [[Product-Backlog]] |
| Burndown-Chart | **Paul Wettering** | [[Burndown-Chart]] |
| Team-Management-Barometer | **Paul Wettering** | [[Team-Management-Barometer]] |
| Weiches Kriterium + One Pager | **Jonas Gebert** | [[Weiches-Kriterium]], [[Statusbericht-1]] |

### Warum diese Verteilung

- **Task Board zu Fynn:** Laut GPM trifft der Product Owner die finale Priorisierungsentscheidung im Backlog. Das Board ist damit sein Arbeitsinstrument — die Verantwortung dafür an eine andere Person zu geben, würde die Rolle aushöhlen.
- **Burndown zu Paul, nicht zu Fynn:** Der Burndown misst, ob abgearbeitet wird, was priorisiert wurde. Priorisierung und Fortschrittsmessung bei derselben Person wäre eine Selbstkontrolle. Getrennte Verantwortung = Vier-Augen-Prinzip.
- **Weiches Kriterium + One Pager zu Jonas:** Beide gehören inhaltlich zusammen — das weiche Kriterium wird im One Pager berichtet. Die Kennzahl (Alter der ältesten offenen Hoch-Prio-Frage) wird aus [[Offene-Fragen]] gemessen, also aus einer Quelle, die Jonas als Verfasser der Fachfragen ohnehin führt.
- **Barometer zu Paul — bekannter Zielkonflikt, siehe unten.**

### Zielkonflikt: Barometer beim Scrum Master

Paul verantwortet als Scrum Master zugleich das Team-Management-Barometer. Das ist methodisch nicht ideal und wird hier offen ausgewiesen statt kaschiert:

- **Konflikt:** Das Barometer erhebt unter anderem, wie das Team die Zusammenarbeit und damit indirekt die Moderation bewertet. Koeppen nennt als Methodenrisiko ausdrücklich, dass „das Team zu negativ antwortet, weil es den Scrum Master ablehnt". Sammelt der Scrum Master die verdeckten Bewertungen selbst ein, ist die Anonymität faktisch aufgehoben — die Werte werden dann systematisch zu positiv.
- **Warum die Kombination trotzdem gewählt wurde:** Bei drei Personen ist eine vollständige Rollentrennung nicht erreichbar. Fynn scheidet als Product Owner aus (Selbstbewertung der Priorisierung), Jonas führt bereits weiches Kriterium und One Pager. Jede Alternative erzeugt einen anderen, nicht kleineren Konflikt.
- **Gegenmaßnahme (kompensierende Kontrolle):** Die Einzelbewertungen werden **verdeckt** abgegeben — jede:r trägt den Wert ohne Namen auf einen Zettel bzw. in ein anonymes Formular ein. **Fynn** zählt aus und bildet den Mittelwert; Paul erhält ausschließlich den Mittelwert und wertet ihn aus. Damit sieht der Scrum Master keine Einzelwerte. Im Repository werden ohnehin nur Mittelwerte gespeichert ([[Projektlog]], 2026-08-05).
- **Wirksamkeitsprüfung:** Weicht ein Barometerwert um mehr als 2 Punkte vom Mittel ab, wird das ohne Namensnennung in der Retrospektive besprochen. Bleibt das Barometer über zwei Erhebungen auffällig flach (alle Werte identisch), gilt die Anonymität als nicht wirksam und die Verantwortung wechselt.
- **Typ:** korrektiv-präventiv · **Verantwortlich für die Kontrolle:** Fynn Barmwater

**Verteilung der Last:** Paul zwei Methoden, Jonas und Fynn je eine. Paul koordiniert als Scrum Master zusätzlich die Umsetzung aller vier — das ist laut GPM seine Aufgabe.

## Inhaltliche Zuständigkeiten (Vorschlag)

| Themenfeld | Verantwortlich | Zugehörige Notizen |
|---|---|---|
| Konstruktion, CAD, Modell/Kernkasten | **Jonas Gebert** | [[Bauteilkonzept]], [[Modellbau]], [[Kernkasten]] |
| Formstoffe, Binder, Trennmittel, Vorversuche V-F1/V-K1/V-T1 | **Fynn Barmwater** | [[Formsand]], [[Binder]], [[Trennmittel]] |
| Werkstoff, Schmelze, Temperaturführung, V-W1/V-S1 | **Paul Wettering** | [[Werkstoffe]], [[Schwindung]] |
| Arbeitssicherheit und Gefährdungsbeurteilung | **Paul Wettering** | [[Arbeitssicherheit]] |
| Versuchsskript und Didaktik | **Jonas Gebert** (Federführung, Inhalte vom ganzen Team) | [[Versuchskonzept]], [[Gussfehler-Provokation]] |

> Arbeitssicherheit liegt bewusst bei derselben Person wie Schmelze und Temperaturführung: Die dominierenden Gefährdungen (heiße Schmelze ≈ 260–300 °C, Ofen, Rauchentwicklung beim Abguss) entstehen genau in diesem Arbeitsbereich.

## Verantwortung für Risiken

| Risiko | Verantwortlich |
|---|---|
| [[R13]] Transferrisiko Göpfert ↔ FtT-Labor | Jonas Gebert |
| [[R10]] Vogelsand ungeeignet | Fynn Barmwater |
| [[R09]] Gefährdungsbeurteilung zu spät | Paul Wettering |
| [[R07]] Deadline 04.10.2026 | Fynn Barmwater |
| [[R02]] Zeitbudget 3 h reicht nicht | Paul Wettering |

> Jedes Mitglied braucht **mindestens eine inhaltliche Aufgabe und mindestens eine PM-Methode**.

## Rollentypen im Team (Reflexion nach Stamm)

`move` · `follow` · `oppose` · `stand by` — alle vier sind positiv. Fehlt ein Typ, steigt das Projektrisiko. Diese Reflexion gehört in die erste Retrospektive.
