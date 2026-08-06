---
typ: journal
titel: "Projektlog"
bereich: beide
tags:
  - journal
erstellt: 2026-07-04
aktualisiert: 2026-08-06
---

# Projektlog

> Chronologisch, neueste Einträge oben. Jeder Arbeitstag/Meilenstein ein Eintrag.

## 2026-08-06 — Hausaufgaben GPM Teil 2 fertiggestellt: Projektauftrag und Ablaufplan

- **Fertigstellungstermin auf 04.10.2026 gesetzt** (vorher 05.10.2026, dort noch mit dem Vorbehalt „zu bestätigen über F7b"). Ein Unterschriftsdokument mit Terminvorbehalt ist wertlos — Folie 30 sagt ausdrücklich, dass Aufgabenstellungen ohne Fertigstellungstermin nicht akzeptiert werden. Das Datum wurde in 14 Notizen nachgezogen (Konventionen, Dashboard, README, R07, Offene-Fragen F7, F7b, TASK-012, TASK-014, Statusbericht-Vorlage, Rollen, Risikoregister, CLAUDE.md, Abgaben-Tracker). Historische Log-Einträge blieben unverändert.
- **Sprinttage festgelegt: Mo, Mi, Fr.** Das war der letzte offene Punkt aus GPM Teil 2, Folie 12. Die Kapazitätsrechnung geht damit auf: 24,3 h je Person und Woche / 3 Sprinttage = **8,1 h je Sprinttag**. Die Weeklys wurden von Di/Do auf **Mo und Fr** verlegt, damit an projektfreien Tagen kein Termin liegt.
- **Nicht-Ziele N1–N7 ergänzt.** Vorher stand dort nur ein Platzhalter. Jedes Nicht-Ziel ist aus der Original-Aufgabenstellung oder einer bestehenden Entscheidung hergeleitet, keines frei erfunden.
- **Neuer Abschnitt 5 „Abweichungen von der Original-Aufgabenstellung".** Das ist die inhaltlich wichtigste Änderung: Der Projektauftrag ist das einzige Dokument, das Prof. Pähler unterschreibt. Zwei Abweichungen waren bisher nur in Nebenbemerkungen versteckt und wären damit nie formal freigegeben worden:
  - **Ab-1** — Nabertherm-Ofen statt Kochplatte (A5) → [[E06]], unkritisch, erfüllt die Absicht der Anforderung besser.
  - **Ab-2** — Nutzung vorhandener Formkästen statt Eigenfertigung (A4) → [[E08]], **bewertungsrelevant, F17 offen.** Als Ersatzleistung wurde Vermessung und Dokumentation der vorhandenen Kästen vorgeschlagen.
- **Abgabefristen der Statusberichte** im Ablaufplan aus den Sprintenden abgeleitet und tabelliert — laut Folie 30 ist der eingereichte Ablaufplan genau dafür die Basis.
- Beide Dokumente als PDF nach `90_Assets/Abgaben/` exportiert, Mailtext-Entwurf an Prof. Koeppen erstellt.

**Nächster Schritt:** F17 (Formkästen) vor der Unterschrift mit Prof. Pähler klären — sie ist die einzige Abweichung, die den Projektaufwand verändert. Danach Unterschriften einholen und beide PDFs bis 12.08.2026 an Prof. Koeppen senden.

## 2026-08-05 (6) — Burndown: Chart.js gegen Inline-SVG getauscht

- **Symptom:** Die Seite wurde fortlaufend laenger und flackerte.
- **Ursache:** Chart.js mit `responsive: true` und `maintainAspectRatio: false` in einem Container **ohne feste Hoehe**. Das Canvas fuellt den Container, dadurch waechst der Container, das loest ein Resize aus — eine Rueckkopplungsschleife, die bei jedem Frame ein paar Pixel zulegt. Kein Reload, sondern Dauer-Reflow.
- **Behebung:** Chart.js ersetzt durch einen eigenen Inline-SVG-Renderer (ca. 40 Zeilen in `tools/dashboard.html`). Ein SVG mit `viewBox` skaliert rein rechnerisch und kann die Groesse seines Containers nicht beeinflussen — die Schleife ist damit ausgeschlossen, nicht nur gedaempft.
- **Nebeneffekte, die den Tausch ohnehin rechtfertigen:** keine externe CDN-Abhaengigkeit mehr (die Seite laeuft vollstaendig offline als lokale Datei), und das Diagramm bleibt beim Zoomen scharf — relevant, weil der Burndown als Screenshot in jeden Statusbericht wandert.
- Die Ist-Kurve wird als **Treppe** gezeichnet. Das ist keine Kosmetik: Arbeitspakete werden ganz oder gar nicht abgebaut, eine schraege Linie wuerde einen kontinuierlichen Fortschritt suggerieren, den es in Scrum nicht gibt.

**Naechster Schritt:** committen und pushen.

## 2026-08-05 (5) — Dashboard-Seite blieb leer: Namenskollision im JavaScript

- **Symptom:** Die veroeffentlichte Seite zeigte nur die Ueberschriften, kein Inhalt.
- **Ursache:** Im Skript war `const top = ...` deklariert. `top` ist im Browser bereits als globales Objekt (`window.top`) belegt; die Neudeklaration wirft einen `SyntaxError`, wodurch das **gesamte** Skript nicht geparst wird. Kein Teilausfall, sondern Totalausfall — und ohne Fehlermeldung auf der Seite selbst.
- **Behebung:** Variable in `topRisiko` umbenannt. Zusaetzlich ist das gesamte Skript jetzt in eine gekapselte Funktion (`IIFE`) gepackt, sodass es keinen globalen Namensraum mehr beruehrt und diese Fehlerklasse strukturell ausgeschlossen ist.
- **Verifikation:** Rendering mit jsdom geprueft — keine JS-Fehler, 5 Kennzahlen, 4 Board-Spalten, 16 Karten, alle Tabellen gefuellt.
- `build_dashboard.py` bricht jetzt ab, wenn der Daten-Platzhalter in der Vorlage fehlt.
- **README korrigiert:** Die Schritte „Core plugins aktivieren" und „Vorlagenordner setzen" waren ueberfluessig — die Vault-Konfiguration liegt versioniert in `.obsidian/` und kommt mit dem Clone mit. Die englischen Menuebezeichnungen entsprachen ausserdem nicht der deutschen Oberflaeche.

**Naechster Schritt:** committen und pushen, dann baut die Action die Seite neu.

## 2026-08-05 (4) — Dashboard live, Tagesnotizen geordnet

- Dashboard ist unter **https://jonasgebert.github.io/Bachelorprojekt/** erreichbar. Erster Workflow-Lauf erfolgreich (Build 9 s, Deploy 10 s).
- Drei Streudateien aus dem Wurzelverzeichnis entfernt (leere Tagesnotiz, `Unbenannt.base`, `Unbenannt.canvas`).
- **Daily Notes konfiguriert:** Zielordner `70_Journal/Tagesnotizen/`, Vorlage [[Vorlage-Tagesnotiz]]. Vorher landeten Tagesnotizen im Wurzelverzeichnis und wären zu einem zweiten, ungepflegten Journal neben [[Projektlog]] geworden.
- **Abgrenzung dokumentiert** (in [[Inbox]] und [[Ordnerstruktur]]): Inbox = Gedanke zwischendurch, Verfall bis zum Weekly · Tagesnotiz = Mitschrift während der Arbeit, Verfall bis zum Tagesende · Projektlog = kuratiertes Archiv. Nur der Projektlog wird dauerhaft gelesen. Die Tagesnotiz-Vorlage enthält eine Verteil-Checkliste, damit Messwerte von Versuchstagen noch am selben Tag in die Versuchsnotiz wandern.

**Nächster Schritt:** unverändert — Planning Poker und Barometer-Erstmessung bis Fr 07.08.

## 2026-08-05 (3) — Statisches Web-Dashboard auf GitHub Pages

- `tools/build_dashboard.py` liest das YAML-Frontmatter von Aufgaben, Sprints, Risiken, Burndown-Datenblatt, weichem Kriterium und Abgaben-Tracker und erzeugt `_site/index.html`. Eine GitHub Action baut und veröffentlicht die Seite bei jedem Push (Latenz ca. 1 min).
- **Bewusste Entscheidung gegen Interaktivität:** Die Seite ist read-only. Ein Klick auf eine Aufgabenkarte öffnet die zugehörige Markdown-Datei auf GitHub. Damit bleibt es bei **einer** Datenquelle — eine Weboberfläche mit Schreibzugriff hätte den Vault und den Browser-Zustand auseinanderlaufen lassen und den Burndown entwertet.
- Verworfen: GitHub Issue Forms als Eingabemaske (Issues würden faktisch zur zweiten Wahrheit) und externe Tools wie Trello oder Notion (zweite Aufgabenliste, verstößt gegen das Grundprinzip in [[Ordnerstruktur]]).
- **Folge aus dem öffentlichen Repository:** [[Team-Management-Barometer]] speichert ab sofort **nur Mittelwerte**. Namentlich zuordenbare Einzelbewertungen von Teammitgliedern gehören nicht in ein öffentlich einsehbares Repository; für den Barograph im Statusbericht genügt der Mittelwert. Einzelwerte werden verdeckt erhoben, im Meeting diskutiert und nicht archiviert. Abweichungen über 2 Punkte werden ohne Namensnennung als Maßnahme festgehalten.
- Neues Frontmatter-Feld `aelteste_offene_frage_seit` in [[Weiches-Kriterium]] — steuert die Ampel auf dem Dashboard und ist der einzige Handgriff, den die Kennzahl braucht.

**Nächster Schritt:** In den Repository-Einstellungen unter Pages die Quelle auf „GitHub Actions" stellen, dann pushen.

## 2026-08-05 (2) — Rollen besetzt, Sprint 1 geplant, Standortentscheidung E10

- **Rollen festgelegt:** Jonas Gebert Scrum Master, Fynn Barmwater Product Owner, Paul Wettering Teammitglied. Methodenverantwortung mit Begründung verteilt: Task Board → Fynn (PO priorisiert), Burndown → Paul (Vier-Augen-Prinzip gegenüber der Priorisierung), Barometer → Paul (bewusst nicht der Scrum Master, dessen Stellung mitbewertet wird), weiches Kriterium + One Pager → Jonas.
- **[[E10]] Versuchsort:** Vorversuche bei der Firma Göpfert in Heide, Generalprobe und Laborbetrieb an der HAW. Zugang jederzeit möglich, damit entfällt das Terminrisiko für den Laborzugang.
- **Drei neue Risiken aus E10:** [[R13]] Transferrisiko (W×H = **9**, damit höchstes Risiko im Projekt), [[R14]] Fahrzeit Heide, [[R15]] Arbeitssicherheit im Fremdbetrieb. Neue Aufgaben [[TASK-041]] und [[TASK-042]].
- **Top-5-Risiken für den Statusbericht festgelegt:** R13, R10, R09, R07, R02 — je mit konkreter Maßnahme, Typ, Wirkung und Verantwortlicher. R14 und R15 bewusst nicht in den Top 5, Begründung im [[Risikoregister]].
- **User Stories INVEST-geprüft.** US-01, US-03 und US-05 verletzen „Small" bewusst; US-05 ist die Definition of Done des Gesamtprojekts und wird nie einem Sprint zugeordnet.
- **[[Sprint-1]] geplant:** 12 Aufgaben, 143 h gegenüber 146 h Kapazität (98 %). Kritischer Pfad: Bestellung Thermoelement ([[TASK-018]]) muss am 10.08. raus, sonst ist V-W1 nicht auswertbar.
- **[[TASK-012]] gebündelt** aus vier Einzelfragen an Prof. Pähler (F14, F16, F17, F7b + neu F25, F27); TASK-013 bis TASK-015 auf `entfallen` gesetzt, IDs bleiben vergeben. Neuer Statuswert `entfallen` in [[Konventionen]] aufgenommen, aus allen Board-Ansichten gefiltert.
- **[[Weiches-Kriterium]] definiert und erstmals gemessen:** Alter der ältesten offenen Hoch-Prio-Frage, gerechnet ab dem späteren Zeitpunkt aus Erfassung und **Projektstart 03.08.2026**. Ergebnis **2 Tage → grün**. Prognose: gelb ab 11.08., rot ab 18.08., falls der Abstimmungstermin mit Prof. Pähler nicht in der ersten Sprintwoche stattfindet.
- **Korrektur der Messvorschrift:** Ein erster Entwurf rechnete ab dem Erfassungsdatum 04.07.2026 und ergab 32 Tage / rot. Das war falsch — das Modul startete erst am 03.08.2026, die Arbeit davor war freiwillige Vorleistung. Eine Kennzahl darf keine Zeit vor ihrem eigenen Nullpunkt zählen und keine Eigeninitiative als Versäumnis ausweisen. Der Nullpunkt liegt jetzt auf dem Projektstart, die Schwellen bleiben unverändert.
- **Vorleistung gekennzeichnet:** Die sechs am 04.07.2026 erledigten Aufgaben (TASK-034 bis TASK-039) tragen `vorleistung: true`, sind keinem Sprint zugeordnet und gehen nicht in den Burndown ein. Im Statusbericht erscheinen sie als Ausgangsbasis, nicht als Sprintleistung.
- **Nicht vorausgefüllt:** Planning Poker und Team-Management-Barometer. Beides sind Erhebungen am Team; erfundene Werte würden den Burndown und den Statusbericht entwerten. Erhebungsbögen liegen bereit, Aufwand zusammen ca. 25 Minuten.

**Nächster Schritt:** Bis Fr 07.08. Planning Poker über die 12 Sprint-1-Aufgaben und Barometer-Erstmessung. Am 10.08. als Erstes die Bestellung aus TASK-018 auslösen und den Termin bei Prof. Pähler anfragen.

## 2026-08-05 — Repository auf Second-Brain-Struktur umgebaut, GPM integriert

- Vault neu strukturiert: `00_Meta` … `90_Assets`. Leitprinzip: **zwei Sichten (BP/GPM), eine Datenbasis**. Begründung und Ordnerlogik in [[Ordnerstruktur]], Feldwerte in [[Konventionen]].
- Bisherige `knowledge/`-Dateien vollständig übernommen, Dateipfad-Referenzen in Wikilinks überführt, YAML-Frontmatter ergänzt. Dateinamen ohne Umlaute/ß (NFC/NFD-Problem in Git).
- Register zerlegt: 9 Entscheidungsnotizen (E01–E09), 10 Risikonotizen (R02–R12, jetzt mit `wahrscheinlichkeit`/`schadenshoehe`/`zone` für die Risikomatrix), 40 Aufgabennotizen (TASK-001…040).
- Aufgabenstatus auf die vier Scrum-Spalten umgestellt (`product-backlog`, `sprint-backlog`, `in-arbeit`, `erledigt`); die frühere Spalte „Blockiert" ist jetzt das Feld `blockiert_durch` — Scrum kennt keine Blockiert-Spalte.
- GPM-Ebene neu aufgebaut: Methodenreferenz aus den drei Foliensätzen Koeppen, Abgaben-Tracker, Projektauftrag, Ablaufplan (zwei Varianten), Rollen, 5 User-Story-Entwürfe, Sprints 1–4, Statusbericht-Vorlage, Burndown, Team-Management-Barometer, weiches Kriterium.
- **Neue offene Fragen:** F20 (Teammitglieder), F21 (Termine GPM Teil 3/4), F22 (Product Owner), F23 (Verfügbarkeit Prof. Pähler), F24 (Laborzugang).
- **Kritisch:** Abgaben Projektauftrag und Ablaufplan sind ca. **12.08.2026** fällig; beide sind bisher nur Entwurf.
- Konflikt erkannt: Ein Ablaufplan mit 4 Sprints à 2 Wochen (10.08.–04.10.) lässt **keinen Puffer** vor der Deadline 05.10.2026 — widerspricht der Maßnahme zu [[R07]]. Variante B in [[Ablaufplan]] empfohlen.

- **Team steht:** Jonas Gebert, Fynn Barmwater (Product Owner, teamintern), Paul Wettering. Folge: Fynn kann laut GPM nicht Scrum Master sein — Rolle offen zwischen Jonas und Paul.
- **Termine fixiert:** GPM Teil 3 Fr 07.08.2026, GPM Teil 4 Mi 30.09.2026. Damit F21 beantwortet.
- **Ablaufplan-Variante B beschlossen:** Sprint 1–3 à 2 Wochen (ab 10.08., 24.08., 07.09.), Sprint 4 à 1 Woche (21.–27.09.), Pufferwoche 28.09.–05.10. GPM Teil 4 fällt in die Pufferwoche. Wochenarbeitszeit ≈ 24,3 h je Person.
- Statusbericht-Fristen daraus abgeleitet: ≈ 30.08. · 13.09. · 27.09. · 04.10.2026 (Bestätigung durch Prof. Koeppen steht aus).
- **Inbox eingeführt:** `00_Inbox/` mit je einer Datei pro Person (Merge-Konflikte vermeiden). Geleert wird im Weekly, nicht in einem separaten Wochenritual. Harte Regel: aus der Inbox geht nichts direkt in den laufenden Sprint.

**Nächster Schritt:** Bis Fr 07.08. Scrum Master wählen, PM-Methoden verteilen, Sprint 1 füllen und Planning Poker durchführen — die Übungen in GPM Teil 3 setzen einen geschätzten Sprint Backlog voraus. Danach Projektauftrag unterschreiben lassen und mit dem Ablaufplan bis 12.08. einreichen.

## 2026-07-04 (2) — Rahmenbedingungen geklärt, Konzept konkretisiert

- Antworten von Jonas eingearbeitet: Laborviertel = 1,5 h (3 h gesamt); Budget unkritisch; Nabertherm-Ofen 5,5 kW statt Kochplatte; Formkästen vorhanden; 3D-Drucker privat; keine FT-Skript-Vorlage; Gefährdungsbeurteilung in Eigenleistung; Deadline **05.10.2026**
- **Entscheidungen:** E3 Reinzinn (Sn-Bi verworfen — Schwindungskompensation didaktisch unerwünscht); E4 Vogelsand + Speiseöl (Auflagen: sieben, Rezeptur via V-F1); E5 3D-Druck Modell/Kernkasten; E6 Ofen; E7 Zwei-Teile-Didaktik (Version F fehlerprovoziert / Version O optimiert); E8 vorhandene Kästen (Vorbehalt F17)
- **Neue Dateien:** [[Bauteilkonzept]] (Vorschlag Miniatur-Riemenscheibe mit Nabenbohrung, 2 Varianten), [[Gussfehler-Provokation]] (9 Provokationsmethoden, 3 für Version F ausgewählt, Sicherheitsausschlüsse)
- Risikoregister überarbeitet: R1/R3 entfallen; neu R10 (Vogelsand-Eignung), R11 (IR-Pyrometer auf Sn-Schmelze unzuverlässig → Thermoelement empfohlen, E9), R12 (A4-Abweichung Formkästen)
- **Kritische offene Punkte:** F15 (Ofen-Typenschild — „Tmax 3000 °C" unmöglich), F17 (A4-Konflikt mit Prof. Pähler klären), F19 (Kästen vermessen)

**Nächster Schritt:** F17/F14 mit Prof. Pähler klären; Formkästen + Ofen-Typenschild dokumentieren; V-F1 (Sandrezeptur) als ersten Vorversuch planen.

## 2026-07-04 — Projektaufsatz Wissensbasis

- Aufgabenstellung.pdf vollständig nach [[Aufgabenstellung]] überführt (inkl. abgeleiteter Anforderungsliste A1–A10)
- Online-Literaturrecherche durchgeführt (6 Suchläufe); 25 Quellen verifiziert und in [[Literatur]] katalogisiert
- Wissensdatenbank `/knowledge` mit 22 Dateien angelegt
- Quellensystem festgelegt: `[Q##]` vs. `[Fachwissen – Quelle nachtragen]` (→ E2)
- Entscheidung E1 dokumentiert (Handformverfahren, durch Aufgabenstellung determiniert)
- Vorläufige Empfehlungen: Sn-Bi nahe Eutektikum (E3), Grünsand/Ölsand + Wasserglas-Kern (E4), 3D-Druck-Modelle (E5) — alle blockiert durch offene Fragen/Vorversuche
- Offene Fragen F1–F14 erfasst; wichtigste organisatorische Klärungen: Laborviertel-Dauer, Budget, Kochplatte, vorhandene Formkästen (F8!), Freigabeprozess Sicherheit
- Risikoregister R1–R9 angelegt

**Nächster Schritt:** E-Mail an Prof. Pähler mit F1–F8; parallel Q1 (Fritz: Fertigungstechnik) aus Bibliothek beschaffen.
