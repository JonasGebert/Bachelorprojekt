---
typ: register
titel: "Offene Fragen"
bereich: beide
tags:
  - register
  - offene-frage
erstellt: 2026-07-04
aktualisiert: 2026-08-10
---

# Offene Fragen

> Neue Frage anlegen: Zeile in der Tabelle „Offen" ergänzen, ID fortlaufend, nie wiederverwenden. Beantwortete Fragen wandern mit Datum und Antwort nach unten.
> Vor technischen Entscheidungen prüfen, ob die zugehörige Frage beantwortet ist. Beantwortete Fragen mit Datum + Antwort unten.

## Offen

| ID | Frage | Blockiert | Priorität |
|---|---|---|---|
| F23 | Verfügbarkeit von Prof. Pähler für Abstimmungstermine (Vorschlag: alle 2 Wochen) | Ablaufplan | hoch |
| F24 | Zugangszeiten FtT-Labor für Vorversuche und Generalprobe | Sprintplanung, V-Z1 | hoch |
| F25 | Steht der Nabertherm-Ofen (5,5 kW) bei Göpfert oder an der HAW? Welcher Ofen steht im FtT-Labor zur Verfügung? Präzisiert [[E06]] | V-W1, Gefährdungsbeurteilung, Transferbewertung | **hoch** |
| F26 | Unterweisung, Betriebsanweisung, PSA und Versicherungsstatus bei Göpfert | erster Schmelzversuch | **hoch** |
| F27 | Wo befinden sich die vorhandenen Formkästen — HAW oder Göpfert? | V-F1, Vermessung F19 | hoch |
| F28 | Anfahrtszeit nach Heide je Versuchstag und wie sie im Planning Poker angerechnet wird | Kapazitätsplanung aller Sprints | mittel |
| F7b | Kolloquiums-/Abgabemodalitäten (Bericht, Präsentation)? Deadline 04.10.2026 bestätigt? | Projektplan | hoch |
| F12 | Kernbinder: gebackener Ölsandkern (Ofen vorhanden!) vs. Wasserglas-CO₂? | V-K1 | hoch |
| F14 | Finale Bauteilgeometrie (Konzeptvorschlag liegt vor → [[Bauteilkonzept]]) | CAD, Modellbau | **hoch** |
| F15 | Exakte Typenbezeichnung Nabertherm-Ofen (5,5 kW). **Teilantwort 07.08.2026 (Jonas, Inbox, unbelegt):** T<sub>max</sub> = 1280 °C — damit ist die 1300-°C-Klasse bestätigt und die Lesart „300 °C" widerlegt. **Weiterhin offen:** Typenbezeichnung und Beleg (Foto Typenschild). Relevant für Gefährdungsbeurteilung + Aufheizkurve | Gefährdungsbeurteilung, V-W1 | **hoch** |
| F16 | Gruppengröße im FtT-L? | Versuchsskript, Rollenverteilung | mittel |
| F17 | **Konflikt A4:** Aufgabenstellung verlangt Konstruktion+Fertigung der Formkästen — vorhandene Kästen nutzen = Abweichung. Mit Prof. Pähler klären (ggf. „Nachkonstruktion/Dokumentation der vorhandenen Kästen" als Ersatzleistung) | Bewertung des Projekts | **hoch** |
| F18 | Temperaturmessung: Einstech-Thermoelement statt IR-Pyrometer? (Emissionsgrad blanker Sn-Schmelze niedrig/instabil → IR unzuverlässig [Fachwissen – prüfen]) | Beschaffung | hoch |
| F10 | Schwindmaß Reinzinn real | V-S1 | mittel |
| F13 | Zeitbedarf Gesamtdurchlauf ≤ 3 h inkl. Theorie/Nachbesprechung? | V-Z1 Generalprobe | hoch |
| F30 | Kernlänge: [[Bauteilkonzept]] nennt „ca. 50 mm", aus Nabe 24 mm + 2 × 12 mm Kernmarke folgen aber 48 mm. Sollmaß festlegen (bestimmt Kernkasten und Kernlager gemeinsam) | CAD, [[Kernkasten]], [[Modellbau]] | mittel |
| F33 | **Bauteilentscheidung.** Riemenscheibe und Lagerbock sind beide nicht aushebbar (Querschnittsfläche nimmt mit dem Abstand von der Teilung zu → Sandausbruch, Nachweis in `tools/zeichnungen/check_aushebbarkeit.py`). Vorschlag: **Stehbuchse mit Fußplatte**, senkrechte Bohrung, stehender Kern, Bauteil komplett im Oberkasten, einteiliges Modell → [[Bauteilkonzept]]. **Blockiert das gesamte CAD** | Modellbau, Kernkasten, Vorversuche | **sehr hoch** |
| F32 | Speiserlage Version O: „über der Nabe" war bei liegender Achse geometrisch nicht speisungsfähig (nur Ø 6 → M = 1,5 mm statt ≥ 3,2 mm). **Wird mit F33 gegenstandslos**, sobald die Stehbuchse beschlossen ist — dort sitzt der Ringspeiser Ø 38/Ø 18 direkt über der Nabe (M = 5,00 mm ✓) | hängt an F33 | niedrig |
| F31 | Nabenlänge 24 mm > Kranzbreite 20 mm → Nabe steht je Seite 2 mm vor. Konstruktiv gewollt (Nabenauflage) oder soll der Kranz auf 24 mm verbreitert werden? | CAD, Massen-/Speiserabschätzung | mittel |

## Beantwortet (10.08.2026, Team)

| ID | Frage | Antwort |
|---|---|---|
| F19 | Innenmaße/Führung/Zustand der vorhandenen Formkästen | Je Hälfte: Breite 90 mm, Länge 190 mm, Höhe 80 mm (Gliedermaßstab, ± 1 mm, gemessen 10.08.2026, Fynn Barmwater). Führung: Stifte. Zustand: gut. Skizze/Foto und Messschieber-Kontrolle der Breite stehen in TASK-016 noch aus |
| F29 | Passt Ø 70 mm Kranz ([[Bauteilkonzept]]) in den vermessenen Kasten (F19)? | **Ja, bei richtiger Orientierung:** Scheibenebene (Ø 70) in die 190-mm-Länge legen, die **Rotationsachse also quer, entlang der 90-mm-Breite** → radial 60 mm (Länge) bzw. 45 mm (Höhe) Sandumhüllung statt 10 mm. *(Formulierungskorrektur 10.08.2026: die ursprüngliche Fassung „Achse entlang der 190-mm-Länge" widersprach den eigenen Zahlen; die Zahlen 60/45/20 mm waren und sind richtig.)* Kein Durchmesser-Redesign nötig. Reine Auslegungsentscheidung des Teams, keine Abweichung von der Aufgabenstellung → keine Rücksprache mit Prof. Pähler nötig (anders als F17). Axiale Umhüllung an den Kernmarken (≈ 20 mm/Seite) bleibt unter der 30–50-mm-Faustregel — im ersten Vorversuch praktisch verifizieren |

## Beantwortet (05.08.2026, Team)

| ID | Frage | Antwort |
|---|---|---|
| F20 | Teammitglieder | **Jonas Gebert, Fynn Barmwater, Paul Wettering** (3 Personen → ca. 510 h Gesamtaufwand) |
| F21 | Termine GPM Teil 3 und Teil 4 | **Teil 3: Fr 07.08.2026 · Teil 4: Mi 30.09.2026** → in [[Ablaufplan]] eingetragen |
| F22 | Product Owner | **Fynn Barmwater** (teamintern, laut GPM zulässig). Auftraggeber bleibt Prof. Pähler. Folge: Fynn kann **nicht** Scrum Master sein |
| — | Ablaufplan-Variante | **Variante B**: 3 Sprints à 2 Wochen + 1 Sprint à 1 Woche + Pufferwoche (28.09.–04.10.) |

## Beantwortet (04.07.2026, Jonas)

| ID | Frage | Antwort |
|---|---|---|
| F1 | Dauer Laborviertel | **1,5 h** → 2 Viertel = 3 h Gesamtversuch inkl. Theorie, Vorbereitung, Durchführung, Nachbesprechung |
| F2 | Budget | vorerst unkritisch; dennoch bewusst kostengünstig/nachhaltig gewählt (Vogelsand, Speiseöl, Recycling) |
| F3/F9 | Wärmequelle | **Nabertherm-Ofen, 5,5 kW**, T<sub>max</sub> ≈ 1280 °C (Typenbezeichnung weiterhin offen → F15); ersetzt „Kochplatte" aus Aufgabenstellung → E6 |
| F4 | Fertigungszugang | 3D-Drucker **privat vorhanden**; Modell + Kernkasten dürfen gedruckt werden → E5 entschieden |
| F5 | Gefährdungsbeurteilung | wird später **selbst angefertigt** (Aufgabe in [[Product-Backlog]]) |
| F6 | FT-Skript | existiert nicht → Theorieteil des Versuchsskripts eigenständig auf Basis [Q1] erstellen |
| F7 | Projektende | **04.10.2026** |
| F8 | Formkästen | **vorhanden** → eigene Kastenfertigung entfällt (aber F17, F19!) |
| F11 | Formsand | **Vogelsand + Speiseöl** (ölgebundener Sand, Budget/Nachhaltigkeit) → E4; Rezeptur über V-F1 |
| — | Werkstoff | **Reinzinn** → E3 entschieden |
| — | Didaktikkonzept | **2 Werkstücke: 1× Gussfehler provoziert, 1× optimiert** → E7, [[Bauteilkonzept]], [[Gussfehler-Provokation]] |
| — | Temperaturüberwachung | Messgerät wird gekauft (Pyrometer o. ä. — Empfehlung siehe F18) |
| — | Recycling | Gussteile werden von Folgegruppen wieder eingeschmolzen (geschlossener Materialkreislauf) |
