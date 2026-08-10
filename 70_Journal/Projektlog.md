---
typ: journal
titel: "Projektlog"
bereich: beide
tags:
  - journal
erstellt: 2026-07-04
aktualisiert: 2026-08-10
---

# Projektlog

> Chronologisch, neueste Einträge oben. Jeder Arbeitstag/Meilenstein ein Eintrag.

## 2026-08-10 (6) — Aushebbarkeit: Regel korrigiert, Bauteil neu (Stehbuchse)

Jonas hat auch den Lagerbock widerlegt: Die Grundplatte liegt 39 mm unter der Teilungsebene und ist breiter als alles darüber — beim Ziehen müsste eine 100 × 44 mm große Platte durch eine 32 × 5 mm große Sandöffnung. Beide Vorentwürfe sind an derselben Regel gescheitert, die ich zweimal falsch formuliert hatte.

**Richtige Regel:** Jeder Schnitt parallel zur Teilungsebene muss in der Projektion des näher an der Teilung liegenden Schnitts liegen; die Querschnittsfläche darf mit dem Abstand von der Teilung nur abnehmen. „Keine konkave Fläche" war eine notwendige, aber keine hinreichende Bedingung.

Der Nachweis ist jetzt als Skript hinterlegt: `tools/zeichnungen/check_aushebbarkeit.py` prüft alle drei Entwürfe numerisch. Ergebnis: Riemenscheibe ✗, Lagerbock ✗, Stehbuchse ✓.

**Neuer Vorschlag: Stehbuchse mit Fußplatte** (110 × 36 × 7, Nabe Ø 34 / Bohrung Ø 18, h = 7…47, zwei Rippen 5 mm, ≈ 415 g Sn). Senkrechte Bohrung, stehender Kern, das gesamte Bauteil liegt im Oberkasten, der Unterkasten ist eine ebene Fläche mit einem einzigen Loch. Modell einteilig — für den 3D-Druck einfacher als jedes geteilte Modell. Zeichnung `Stehbuchse_Vorschlag.svg` mit Bauteil, Formaufbau, Formfolge und dem Aushebbarkeitsdiagramm.

**Nächster Schritt:** F33 entscheiden. Danach CAD; offen bleibt die Speisung der Fußplatte über den Knoten zur Nabe — das wird im Vorversuch gemessen.

## 2026-08-10 (5) — Bauteilwechsel vorgeschlagen: Lagerbock statt Riemenscheibe

Konsequenz aus dem Hinterschnitt (F33). Statt die Riemenscheibe zu reparieren, wird die im [[Bauteilkonzept]] bereits dokumentierte Rückfalloption aktiviert: **Lagerbock (Stehlager) mit Durchgangsbohrung**. Zeichnung `Lagerbock_Vorschlag.svg` (A3): Bauteil 1:1 in Vorderansicht und Schnitt, Formaufbau im Querschnitt und Draufsicht auf die Teilungsebene, jeweils 1:2, plus Anforderungscheck.

Maße Version O: Grundplatte 100 × 44 × 6 · Rippe 5 × 32, h = 6…25 · Lagerauge Ø 40 / Bohrung Ø 20, Breite 32 · Achshöhe 45 · Kern Ø 20 × 60 · ≈ 0,43 kg Sn.

Warum es trägt:

- **hinterschnittfrei** — Teilung durch die Bohrungsachse, keine zur Ausheberichtung konkave Modellfläche; die einzige konkave Fläche ist die Bohrung, und die macht der Kern
- **A3 erfüllt** — die Bohrung ist ohne Kern nicht herstellbar
- **passt in die vorhandenen Kästen** — 25 mm Sand seitlich, 35 mm unter der Platte, 45 mm an den Stirnseiten
- **E7 bleibt gültig** — Version F/O über Rippendicke, Kehlenradius, Lageraugendurchmesser und Gießsystem
- **Speisung funktioniert** — Moduln Lagerauge 3,9 > Platte 2,6 > Rippe 2,2 mm, dickste Stelle oben unter dem Speiser

Der frühere Einwand gegen den Lagerbock („weniger Fehlerbühnen") trägt nicht mehr: Der Knotenpunkt Rippe/Grundplatte ist das Lehrbuchbeispiel für Materialanhäufung und liefert Warmriss und Lunker an einer Stelle.

**Nächster Schritt:** F33 im Weekly entscheiden. Erst danach CAD. Offen bleibt, ob die Grundplatte durch die Rippe hindurch ausreichend gespeist wird — das ist im Vorversuch zu messen, nicht zu behaupten.

## 2026-08-10 (4) — Hinterschnitt: Einformlage aus dem Bauteilkonzept ist nicht ausführbar (F33)

Jonas hat am gezeichneten Formaufbau den entscheidenden Fehler gefunden: Bei Teilung **durch** die Achse ist die Ringnut zwischen Nabe (Ø 28) und Kranz (Ø 54 innen) ein Hinterschnitt. Die Kranz-Innenfläche umschließt den Nutsand unterhalb der Teilungsebene über die volle Nuttiefe von 13 mm; beim senkrechten Ausheben der Modellhälfte würde dieser Sand ausreißen. Die frühere Aussage „größter Querschnitt in der Teilung, beide Hälften ziehen gerade" war falsch — hinterschnittfrei ist nur, was in Ausheberichtung keine zur Achse konkave Fläche hat.

Folgen:

- Die Teilungsebene muss **senkrecht zur Rotationsachse** liegen (Stegebene). Damit steht der Kern — die ursprüngliche Rückfrage von Jonas war richtig.
- Damit ist die Antwort zu F29 hinfällig: Ø 70 liegt dann in der 190 × 90 mm-Grundfläche, die 90-mm-Breite lässt nur 10 mm Sandumhüllung.
- `Formaufbau_Schnitt.svg` ist als nicht ausführbar gekennzeichnet, nicht gelöscht (Dokumentation des Denkwegs).
- Auch die Formulierung im Bauteilkonzept war von Anfang an mehrdeutig: „Riemenscheibe liegend eingeformt" (= Achse senkrecht) und „horizontaler Kern" im selben Satz schließen sich aus.

**Nächster Schritt:** F33 entscheiden, bevor irgendein CAD-Modell entsteht. Vier Optionen stehen im Register; Vorzugsvariante ist der Bau eigener Formkästen, weil A4 das ohnehin verlangt (F17) und damit Kastenmaß und Bauteil gemeinsam ausgelegt werden können.

## 2026-08-10 (3) — Formaufbau gezeichnet, Speiserlage als F32 aufgeworfen

Zeichnung `Formaufbau_Schnitt.svg` (A3, 1:1): zwei senkrecht zueinander stehende Schnitte durch den geschlossenen Formkasten mit Kern, Kernmarken, Einguss, Querlauf, Anschnitt, Speiser, Windpfeife und Kühleisen; Sandumhüllung bemaßt (60/45 mm radial, 21 mm axial hinter den Kernmarken).

Zwei Punkte sind dabei aufgefallen:

1. **Speisung (neu als F32):** „Speiser über der Nabe" aus dem [[Bauteilkonzept]] ist bei liegender Achse nicht ausführbar — der Kranz steht darüber, es bliebe ein Speiser Ø 6 mm (M = 1,5 mm), nötig wären M ≥ 1,2 · 2,7 = 3,2 mm. Vorschlag: Speiser Ø 14 mm auf den Kranz (M = 3,5 mm) und die Nabe mit Kühleisen (Alu-Ring Ø 40/Ø 14 × 8 mm) zuerst erstarren lassen. Erstarrungsmoduln aus den Konzeptmaßen: Nabe 2,7 · Kranz 2,6 · Steg 2,5 mm — sehr dicht beieinander, also kein natürlicher Speisungsweg.
2. **Formulierungskorrektur F29 / [[Formkasten]]:** Der Satz „Achse entlang der 190-mm-Länge" widersprach den eigenen Zahlen. Richtig und gemeint: die Scheibenebene (Ø 70) liegt in der 190-mm-Länge, die **Rotationsachse liegt quer, entlang der 90-mm-Breite**. Die Zahlen 60/45/20 mm waren immer richtig, nur die Richtungsangabe war falsch benannt.

**Nächster Schritt:** F32 im Weekly entscheiden (Speiser auf dem Kranz + Kühleisen ja/nein), erst danach Modell- und Kernkasten-CAD beginnen — die Speiserlage bestimmt, ob der Speiser mit eingeformt oder separat aufgesetzt wird.

## 2026-08-10 — Prinzipskizze des Bauteils erstellt

Aus den Konzeptmaßen des [[Bauteilkonzept]]s wurde eine maßstäbliche Prinzipskizze (A3, Ansicht + Vollschnitt A–A, Version O und F) sowie eine 3D-Ansicht mit Viertelausschnitt erzeugt. Beides liegt in `90_Assets/Bilder/`, die erzeugenden Skripte in `tools/zeichnungen/` (parametrisch, damit Tabelle und Skizze nicht auseinanderlaufen). Es ist ausdrücklich **keine** fertigungsreife Zeichnung nach DIN EN 12890 [Q18] — Schwindmaß, Formschrägen, Kernmarkenpassung, Radien, Anschnitt/Speiser und Toleranzen fehlen bewusst.

Beim Aufmaßen sind zwei Widersprüche im Konzept aufgefallen und als [[Offene-Fragen|F30]] (Kernlänge 50 vs. 48 mm) und F31 (Nabe 24 mm breiter als Kranz 20 mm) erfasst.

**Nächster Schritt:** F30/F31 im nächsten Weekly klären, danach parametrisches CAD aufsetzen; Schwindmaß aus V-S1 erst vor dem finalen Druck einpflegen.

## 2026-08-10 (2) — F29-Konflikt aufgelöst: Orientierungsfrage statt Ø70-Redesign

- Nachtrag zu F19: gemessen hat **Fynn Barmwater**, heute. Führungssystem = **Stifte**. Zustand = **gut**.
- F29 (Ø 70 mm Kranz vs. 90 mm Kastenbreite) war kein Konflikt mit der Aufgabenstellung, sondern eine unausgesprochene Orientierungsannahme: Die 10-mm-Sandumhüllung galt nur, wenn die Rotationsachse entlang der 90-mm-Breite liegt. Legt man die Achse stattdessen entlang der **190-mm-Länge**, ergeben sich 60 mm radiale Umhüllung — komfortabel im Rahmen der Faustregel. Team-Entscheidung, **keine Rücksprache mit Prof. Pähler nötig** — anders als F17, das eine echte Abweichung von A4 betrifft.
- Restpunkt bleibt: axiale Umhüllung an den Kernmarken in dieser Orientierung ≈ 20 mm/Seite, unter der 30–50-mm-Faustregel. Rechnerisch plausibel für kleines Sn-Teil bei niedriger Gießtemperatur, aber noch nicht praktisch verifiziert → in V-F1/V-Z1 prüfen.
- F19 und F29 im Fragenregister als beantwortet verschoben. TASK-016 bleibt `in-arbeit` (Skizze/Foto und Messschieber-Kontrolle noch offen).

## 2026-08-10 — Innenmaße Formkästen vermessen (F19, teilweise): Konflikt mit Bauteilkonzept aufgedeckt

- Innenmaße je Kastenhälfte gemessen (Gliedermaßstab, ± 1 mm): **Breite 90 mm, Länge 190 mm, Höhe 80 mm**. Eingetragen in [[Formkasten]]. Führungssystem und Zustand der Kästen (Rest von F19/TASK-016) noch offen.
- **Konflikt entdeckt:** Bauteilkonzept sieht Ø 70 mm Kranzdurchmesser vor. Bei 90 mm Breite bleiben nur 10 mm Sandumhüllung je Seite — unter der Faustregel ≥ 30–50 mm. Höhe und Länge unkritisch. In [[Bauteilkonzept]] als offener Punkt vermerkt.
- Datum der Messung und messende Person nicht mitgeteilt — in [[Formkasten]] als offen markiert, bitte ergänzen.
- Neue Frage **F29** im Offene-Fragen-Register angelegt (Konflikt Ø70 mm vs. Kastenbreite, mit Prof. Pähler zu klären). F19 mit Teilantwort versehen, bleibt offen. **TASK-016** DoD-Checkliste ergänzt und Status auf `in-arbeit` gesetzt (Messung begonnen, Führung/Zustand/Kontrollmessung fehlen noch) — nicht auf `erledigt` gesetzt, da Definition of Done nicht vollständig erfüllt.

**Nächster Schritt:** Konflikt Ø 70 mm vs. Kastenbreite (F29) mit Prof. Pähler klären; Rest von TASK-016 (Führung, Zustand, Messdatum/Person, Kontrollmessung Breite) erledigen.

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

- **Rollen festgelegt:** Paul Wettering Scrum Master, Fynn Barmwater Product Owner, Jonas Gebert Teammitglied. Methodenverantwortung mit Begründung verteilt: Task Board → Fynn (PO priorisiert), Burndown → Paul (Vier-Augen-Prinzip gegenüber der Priorisierung), Barometer → Paul, weiches Kriterium + One Pager → Jonas. **Zielkonflikt dokumentiert:** Barometer und Scrum-Master-Rolle liegen bei derselben Person; kompensierende Kontrolle ist die verdeckte Abgabe mit Auszählung durch Fynn → [[Rollen-und-Verantwortlichkeiten]].
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
