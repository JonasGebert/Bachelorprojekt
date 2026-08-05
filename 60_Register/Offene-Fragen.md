---
typ: register
titel: "Offene Fragen"
bereich: beide
tags:
  - register
  - offene-frage
erstellt: 2026-07-04
aktualisiert: 2026-08-05
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
| F7b | Kolloquiums-/Abgabemodalitäten (Bericht, Präsentation)? Deadline 05.10.2026 bestätigt? | Projektplan | hoch |
| F12 | Kernbinder: gebackener Ölsandkern (Ofen vorhanden!) vs. Wasserglas-CO₂? | V-K1 | hoch |
| F14 | Finale Bauteilgeometrie (Konzeptvorschlag liegt vor → [[Bauteilkonzept]]) | CAD, Modellbau | **hoch** |
| F15 | Exakte Typenbezeichnung Nabertherm-Ofen (5,5 kW; „Tmax 3000 °C" ist technisch unmöglich — vermutlich 300 °C oder 1300 °C). Relevant für Gefährdungsbeurteilung + Aufheizkurve | Gefährdungsbeurteilung, V-W1 | **hoch** |
| F16 | Gruppengröße im FtT-L? | Versuchsskript, Rollenverteilung | mittel |
| F17 | **Konflikt A4:** Aufgabenstellung verlangt Konstruktion+Fertigung der Formkästen — vorhandene Kästen nutzen = Abweichung. Mit Prof. Pähler klären (ggf. „Nachkonstruktion/Dokumentation der vorhandenen Kästen" als Ersatzleistung) | Bewertung des Projekts | **hoch** |
| F18 | Temperaturmessung: Einstech-Thermoelement statt IR-Pyrometer? (Emissionsgrad blanker Sn-Schmelze niedrig/instabil → IR unzuverlässig [Fachwissen – prüfen]) | Beschaffung | hoch |
| F19 | Innenmaße/Zustand der vorhandenen Formkästen (vermessen!) → begrenzt Bauteil- und Gießsystemgröße | bauteil_konzept, CAD | **hoch** |
| F10 | Schwindmaß Reinzinn real | V-S1 | mittel |
| F13 | Zeitbedarf Gesamtdurchlauf ≤ 3 h inkl. Theorie/Nachbesprechung? | V-Z1 Generalprobe | hoch |

## Beantwortet (05.08.2026, Team)

| ID | Frage | Antwort |
|---|---|---|
| F20 | Teammitglieder | **Jonas Gebert, Fynn Barmwater, Paul Wettering** (3 Personen → ca. 510 h Gesamtaufwand) |
| F21 | Termine GPM Teil 3 und Teil 4 | **Teil 3: Fr 07.08.2026 · Teil 4: Mi 30.09.2026** → in [[Ablaufplan]] eingetragen |
| F22 | Product Owner | **Fynn Barmwater** (teamintern, laut GPM zulässig). Auftraggeber bleibt Prof. Pähler. Folge: Fynn kann **nicht** Scrum Master sein |
| — | Ablaufplan-Variante | **Variante B**: 3 Sprints à 2 Wochen + 1 Sprint à 1 Woche + Pufferwoche (28.09.–05.10.) |

## Beantwortet (04.07.2026, Jonas)

| ID | Frage | Antwort |
|---|---|---|
| F1 | Dauer Laborviertel | **1,5 h** → 2 Viertel = 3 h Gesamtversuch inkl. Theorie, Vorbereitung, Durchführung, Nachbesprechung |
| F2 | Budget | vorerst unkritisch; dennoch bewusst kostengünstig/nachhaltig gewählt (Vogelsand, Speiseöl, Recycling) |
| F3/F9 | Wärmequelle | **Nabertherm-Ofen, 5,5 kW** (Tmax klären → F15); ersetzt „Kochplatte" aus Aufgabenstellung → E6 |
| F4 | Fertigungszugang | 3D-Drucker **privat vorhanden**; Modell + Kernkasten dürfen gedruckt werden → E5 entschieden |
| F5 | Gefährdungsbeurteilung | wird später **selbst angefertigt** (Aufgabe in [[Product-Backlog]]) |
| F6 | FT-Skript | existiert nicht → Theorieteil des Versuchsskripts eigenständig auf Basis [Q1] erstellen |
| F7 | Projektende | **05.10.2026** |
| F8 | Formkästen | **vorhanden** → eigene Kastenfertigung entfällt (aber F17, F19!) |
| F11 | Formsand | **Vogelsand + Speiseöl** (ölgebundener Sand, Budget/Nachhaltigkeit) → E4; Rezeptur über V-F1 |
| — | Werkstoff | **Reinzinn** → E3 entschieden |
| — | Didaktikkonzept | **2 Werkstücke: 1× Gussfehler provoziert, 1× optimiert** → E7, [[Bauteilkonzept]], [[Gussfehler-Provokation]] |
| — | Temperaturüberwachung | Messgerät wird gekauft (Pyrometer o. ä. — Empfehlung siehe F18) |
| — | Recycling | Gussteile werden von Folgegruppen wieder eingeschmolzen (geschlossener Materialkreislauf) |
