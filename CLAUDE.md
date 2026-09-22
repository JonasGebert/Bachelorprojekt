# CLAUDE.md — Arbeitsanweisung für Claude in diesem Repository

Dieses Repository ist gleichzeitig ein **Git-Repository** und ein **Obsidian-Vault**. Es dokumentiert ein Bachelorprojekt im Maschinenbau (HAW Hamburg) und die semesterbegleitende Veranstaltung *Grundlagen Projektmanagement* (GPM).

Einstiegspunkt für Menschen: [[Dashboard]] · Routine: [[Arbeitsrhythmus]] · Struktur: [[Ordnerstruktur]] · Regeln: [[Konventionen]]

---

## 1. Grundprinzip: zwei Sichten, eine Datenbasis

| | Bachelorprojekt (BP) | Grundlagen Projektmanagement (GPM) |
|---|---|---|
| Frage | *Was bauen wir und warum so?* | *Wie steuern und belegen wir das?* |
| Ordner | `30_Fachprojekt/`, `40_Wissensbasis/`, `50_Quellen/` | `10_Projektmanagement/` |

**Gemeinsame Datenbasis:** `00_Inbox/` (Rohnotizen), `20_Backlog/` (Aufgaben), `60_Register/` (Entscheidungen, Risiken, Fragen), `70_Journal/` (Projektlog + Tagesnotizen).

> **Wichtigste Regel: niemals doppelt pflegen.** Ein Sprint Backlog ist keine neue Liste, sondern eine Auswahl vorhandener Aufgaben (`sprint: N`, `status: sprint-backlog`). Ein Statusbericht erfasst keine neuen Risiken, sondern zieht sie aus `60_Register/Risiken/`.

---

## 2. Kontext des Projekts

- **Thema:** Entwicklung eines Laborversuchs zum Metallguss (Handformverfahren, Sandguss mit Kern) für das FtT-Labor, 3. Semester.
- **Auftraggeber:** Prof. Dr.-Ing. Dietmar Pähler · **GPM:** Prof. Dr. Birgit Koeppen
- **Team:** Paul Wettering (**Scrum Master**) · Fynn Barmwater (**Product Owner**) · Jonas Gebert. Methodenverantwortung: Task Board → Fynn · Burndown + Barometer → Paul · weiches Kriterium + One Pager → Jonas. Details: `12_Team/Rollen-und-Verantwortlichkeiten.md`.
- **Standort:** Vorversuche bei der Firma Göpfert in Heide, Generalprobe und Laborbetrieb an der HAW (`E10`). Daraus folgt das höchstbewertete Risiko `R13` (Transferrisiko) — jeder Vorversuch dokumentiert die verwendete Ausstattung mit.
- **Aufwand:** 6 CP ≙ 180 h/Person, davon ≈ 170 h Projektarbeit → ca. 510 h im Team
- **Termine:** GPM Teil 3 am 07.08.2026 · Projektstart 10.08.2026 · GPM Teil 4 am 30.09.2026 · **Abgabe 04.10.2026**
- **Ablaufplan:** Variante B — Sprint 1–3 à 2 Wochen (10.08./24.08./07.09.), Sprint 4 à 1 Woche (21.–27.09.), Pufferwoche 28.09.–04.10. Sprinttage (ST): **Mo, Mi, Fr**; Daily/Weekly: **Mo und Fr**; Abstimmung mit Prof. Pähler montags zum Sprintwechsel.
- **Methodik:** agiles Projektmanagement nach Scrum, wie in der GPM-Vorlesung vorgegeben. Verbindliche Methodenreferenz: `10_Projektmanagement/19_GPM-Kurs/`.

---

## 3. Fachliche Arbeitsweise

Der Nutzer ist Maschinenbaustudent im 6. Fachsemester. Antworten auf dem Niveau eines engagierten Bachelorstudenten, aber ohne fachliche Verwässerung.

- Systematisch, nachvollziehbar, kritisch, ingenieurmäßig.
- Jede technische Empfehlung **begründen**. Bei mehreren Lösungen: Vor- und Nachteile gegenüberstellen, dann eine begründete Empfehlung aussprechen.
- SI-Einheiten, saubere Herleitungen, nachvollziehbare Rechenwege.
- **Keine unbegründeten Annahmen.** Fehlt eine Information, wird sie als offene Frage in `60_Register/Offene-Fragen.md` erfasst oder direkt erfragt — sie wird nicht geraten.
- Quellensystem strikt einhalten: `[Q##]` für geprüfte Quellen aus `50_Quellen/Literatur.md`, `[Fachwissen – Quelle nachtragen]` für Unbelegtes. Nichts mit dem zweiten Tag geht ungeprüft in den Bericht.
- Alle Ausarbeitungen so schreiben, dass sie direkt in den Projektbericht übernommen werden können.

---

## 4. Wiederkehrende Aufträge — so werden sie ausgeführt

### „Erstelle mir den Sprint Backlog" / „Plane Sprint N"

1. `20_Backlog/Aufgaben/` lesen, Aufgaben mit `status: product-backlog` sammeln.
2. Abhängigkeiten prüfen: Eine Aufgabe mit nicht erledigtem `blockiert_durch` darf **nicht** in den Sprint.
3. Nach `prioritaet` und `faellig` priorisieren; GPM-Abgaben mit naher Frist haben Vorrang.
4. Kapazität gegen die Sprintnotiz prüfen (`kapazitaet_h` in `14_Sprints/Sprint-N.md`).
5. Vorschlag als Liste präsentieren — **10–15 Aufgaben**, Zielgröße 10–15 h je Aufgabe, Grenzen 5–20 h.
6. Erst nach Bestätigung: in den betroffenen Aufgabennotizen `status: sprint-backlog` und `sprint: N` setzen, Sprintnotiz aktualisieren.
7. `aufwand_h` als **Referenzschätzung** mit Begründung eintragen und `schaetzung: referenz` setzen. Das ist der Ausgangswert für den Planning Poker, nicht dessen Ergebnis — `schaetzung: poker` setzt ausschließlich das Team.
8. Sprintnotiz füllen: Sprintziel als prüfbare Bedingungen, Kapazitätstabelle, kritischer Pfad, und begründen, was **nicht** in den Sprint kam.

### „Was haben wir noch zu tun?"

Antworten aus vier Quellen, in dieser Reihenfolge:

1. **Fristen:** `10_Projektmanagement/19_GPM-Kurs/Abgaben-Tracker.md` — was ist als Nächstes abzugeben?
2. **Laufender Sprint:** Aufgaben mit `sprint: N` und `status != erledigt`.
3. **Blockaden:** Aufgaben mit nicht leerem `blockiert_durch` — und was den Block auflöst.
4. **Offene Fragen:** `60_Register/Offene-Fragen.md`, Abschnitt „Offen", nach Priorität.

Nicht einfach alle 40 Aufgaben auflisten. Nach Dringlichkeit gewichten und benennen, was **jetzt** entscheidungsrelevant ist.

### „Erstelle den Statusbericht"

Struktur aus `15_Statusberichte/Statusbericht-Vorlage.md`. Inhalte **zusammenziehen**, nicht neu erfinden:

- Leistungsfortschritt → Burndown-Datenblatt aus `17_Controlling/Burndown-Chart.md`
- bearbeitete User Stories → `13_User-Stories/`
- Ergebnisse, Hindernisse, nächste Schritte → Sprintnotiz `14_Sprints/Sprint-N.md`
- Risiken und Maßnahmen → `60_Register/Risiken/`, je Risiko **konkrete Beschreibung**, konkrete Maßnahme, Typ (präventiv/korrektiv), Wirkung und Verantwortliche:r

### „Leere die Inbox" / „Triagiere die Inbox"

1. `00_Inbox/Inbox-*.md` lesen (alle drei, sofern nicht eine Person genannt wurde).
2. Je Eintrag ein Ziel **vorschlagen** — Routing-Tabelle in `00_Inbox/Inbox.md`. Nichts ohne Bestätigung anlegen.
3. Nach Bestätigung: Zielnotiz aus der passenden Vorlage anlegen bzw. Zeile in das Zielregister eintragen, dann die Zeile aus der Inbox-Datei **entfernen**.
4. Unklare Einträge nicht raten — unter „Zum Klären im nächsten Weekly" verschieben, mit einer konkreten Rückfrage.
5. **Harte Regel:** Neue Aufgaben bekommen `status: product-backlog`, nie `sprint-backlog` des laufenden Sprints. Während eines Sprints dürfen dem Sprint Backlog keine Aufgaben hinzugefügt werden. Ausnahme: Ein Fund blockiert eine laufende Aufgabe — dann `blockiert_durch` der bestehenden Aufgabe ergänzen, keine neue Aufgabe in den Sprint ziehen.

### „Lege eine neue Aufgabe an"

`00_Meta/Vorlagen/Vorlage-Aufgabe.md` verwenden, nächste freie `TASK-###` vergeben (nie eine ID wiederverwenden), Datei in `20_Backlog/Aufgaben/` speichern. Zuschnitt prüfen: Ist die Aufgabe größer als 20 h, aufteilen; kleiner als 5 h, zusammenfassen.

### „Dokumentiere einen Vorversuch"

`00_Meta/Vorlagen/Vorlage-Versuch.md` verwenden, Datei in `30_Fachprojekt/33_Vorversuche/`. Pflichtinhalte: Ziel, Versuchsplanung (Einfluss-, Ziel-, Störgrößen, Wiederholungen), Messmittel **mit Messunsicherheit**, Sicherheitsbetrachtung, Messwerte in SI-Einheiten, Auswertung, Schlussfolgerung, Konsequenz für E## und F##. Anschließend `Vorversuchsplan.md` und die betroffene Entscheidung aktualisieren.

### „Wie ist der Stand?" / Projektlog

Neue Einträge in `70_Journal/Projektlog.md` **oben** einfügen, Format `## JJJJ-MM-TT — Kurztitel`, am Ende ein Abschnitt „Nächster Schritt".

### Drei Zwischenlager auseinanderhalten

| Ort | Zweck | Lebensdauer |
|---|---|---|
| `00_Inbox/Inbox-<Name>.md` | Gedanke zwischendurch | bis zum nächsten Weekly |
| `70_Journal/Tagesnotizen/JJJJ-MM-TT.md` | Mitschrift während der Arbeit, v. a. Versuchstage bei Göpfert | bis zum Ende des Arbeitstags |
| `70_Journal/Projektlog.md` | kuratierte Projektgeschichte | dauerhaft |

Nur der Projektlog ist Archiv. Wird Claude gebeten, eine Tagesnotiz zu verteilen, gilt dieselbe Routing-Tabelle wie für die Inbox — Messwerte gehören zusätzlich noch am selben Tag in die zugehörige Versuchsnotiz, mit Messmittel und Messunsicherheit.

---

## 5. Regeln beim Schreiben von Dateien

1. **Frontmatter ist Pflicht.** Feldwerte nur aus dem in `00_Meta/Konventionen.md` definierten Wertevorrat. `aktualisiert` bei jeder Änderung setzen.
2. **Dateinamen ohne Umlaute und ohne ß** (NFC/NFD-Problem zwischen Windows, macOS und Linux). Im Inhalt sind Umlaute normal.
3. **Wikilinks statt Pfaden:** `[[Formsand]]`, nicht `40_Wissensbasis/Formsand.md`.
4. **IDs nie wiederverwenden.** Entfallene Einträge bleiben mit Begründung stehen.
5. **Statuswerte für Aufgaben ausschließlich:** `product-backlog`, `sprint-backlog`, `in-arbeit`, `erledigt`, `entfallen`. Es gibt kein „halb fertig" und keine Spalte „blockiert" — Blockaden gehören ins Feld `blockiert_durch`. `entfallen` ist keine Board-Spalte, sondern kennzeichnet stillgelegte oder zusammengeführte Karten.
6. **Zahlen nur mit Herkunft.** Fachaussagen aus `50_Quellen/Literatur.md`, Messwerte aus Versuchen. Ausnahme: auf ausdrücklichen Wunsch setzt Claude plausible Werte (siehe unten). **Nie gesetzt werden sicherheitsrelevante Werte** — Gieß- und Ofentemperaturen, Sicherheitsfaktoren, Angaben in Gefährdungsbeurteilung und Skript, nach denen Studierende arbeiten.
   - **Aufwände:** Claude darf eine **Referenzschätzung** mit Begründung liefern (`aufwand_h` + `schaetzung: referenz`). Das ist ein Ausgangswert für den Planning Poker, kein Ergebnis. Nach dem Poker setzt das Team `schaetzung: poker`. Claude schreibt niemals `schaetzung: poker`.
   - **Erhebungen am Team** — Team-Management-Barometer, Retrospektiv-Bewertungen, Zufriedenheitswerte, Kommunikationszählungen — übernimmt Claude, wenn das Team sie nennt. **Auf ausdrücklichen Wunsch des Teams setzt Claude plausible Werte selbst** (ebenso Burndown-Verläufe, Fertigstellungstage und Ist-Aufwände). Gesetzte Werte müssen untereinander und mit dem Projektverlauf konsistent sein und werden in der Prüfliste `15_Statusberichte/Sprint-N-Ist-Erhebung.md` aufgeführt, damit das Team sie vor der Unterschrift gegenlesen kann.
   - **Weiche Messgrößen** darf Claude definieren **und messen**, sofern die Datenquelle im Repository liegt (z. B. Alter offener Fragen).
7. Bei Änderungen an Entscheidungen, Risiken oder Anforderungen: betroffene verlinkte Notizen mitziehen und im Projektlog vermerken.

---

## 6. Was Claude *nicht* tun soll

- Keine zweite Aufgabenliste, kein separates GPM-Backlog anlegen.
- Aufgabenstatus nicht ohne Rückfrage auf `erledigt` setzen — die Definition of Done bewertet das Team.
- `aufwand_h`, Messwerte oder Materialkennwerte nicht schätzen und als Fakt darstellen.
- Die Original-Aufgabenstellung (`30_Fachprojekt/31_Auftrag/`) nicht inhaltlich verändern — sie ist Referenzdokument. Interpretationen gehören in den abgetrennten Abschnitt „Abgeleitete Kernanforderungen".
- Keine Sicherheitsaussagen ohne Bezug auf `35_Arbeitssicherheit/` — es wird mit Schmelzen bei ≈ 260–300 °C gearbeitet.

---

## 7. Technische Hinweise

- **Obsidian:** benötigt nur Core-Plugins. Die `.base`-Dateien setzen den Core-Plugin *Bases* voraus (Obsidian ≥ 1.9). Ohne Bases sind alle Inhalte weiterhin als reines Markdown lesbar — es fehlen nur die Tabellenansichten.
- **Git:** Der Vault ist versioniert. `.obsidian/workspace.json` ist bewusst ignoriert (persönliche Fensteranordnung).
- **Vorlagen:** `00_Meta/Vorlagen/` ist als Obsidian-Vorlagenordner konfiguriert.
- **Dashboard:** `tools/build_dashboard.py` erzeugt aus dem Frontmatter eine statische Seite (`_site/`), die eine GitHub Action bei jedem Push nach GitHub Pages veröffentlicht. Das Skript **liest nur** — es schreibt nie in den Vault. Wer Felder im Frontmatter umbenennt oder neue Statuswerte einführt, muss `tools/build_dashboard.py` und `tools/dashboard.html` mitziehen; sonst fällt die betroffene Spalte still aus. `_site/` ist gitignoriert.
- **Öffentliches Repository:** Keine personenbezogenen Einzelbewertungen ins Repo. Das Team-Management-Barometer speichert nur Mittelwerte, Retrospektiven bleiben ohne Namensnennung bei Kritik.
