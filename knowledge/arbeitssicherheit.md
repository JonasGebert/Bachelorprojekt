# Arbeitssicherheit

> Quellen: [Q15] DGUV Regel 109-608 „Branche Gießereien"; [Q16] BGHM PSA-Kompakt 143; [Q17] DGUV-Info 209-006. **Vor Laborbetrieb: Abstimmung mit Laboringenieur/Sicherheitsbeauftragtem der HAW zwingend** (→ `offene_fragen.md` F5).

## Gefährdungsbeurteilung (Entwurf, projektspezifisch)

| Nr. | Gefährdung | Quelle | Schutzmaßnahme (T-O-P) |
|---|---|---|---|
| G1 | Verbrennung an Schmelze/Tiegel (140–300 °C) | Schmelzen, Gießen | T: Tiegel mit Ausgießhilfe/Halterung; O: Gießbereich abgegrenzt, nur 1 Person gießt; P: Hitzeschutzhandschuhe, Schürze, Gesichtsschutz [Q16] |
| G2 | **Dampfschlag/Metallauswurf durch feuchte Form oder feuchtes Einsatzmaterial** | Grünsand, Recyclingmaterial | T: Formen kontrolliert trocknen; **kein feuchtes Metall in die Schmelze**; O: Wassergehaltskontrolle als Skriptschritt; P: Gesichtsschutz. Wichtigste Einzelgefahr trotz niedriger Temperatur! [Q15] |
| G3 | Heiße Oberflächen Kochplatte | Schmelzbetrieb | O: Kennzeichnung, Restwärme-Hinweis; P: Handschuhe |
| G4 | Stolpern/Verschütten beim Transport der Schmelze | Gießen | O: kürzester Gießweg, freie Wege, Gießen nur am Tisch |
| G5 | Staub (Quarzsand, Talkum, Lykopodium) | Formerei | T: staubarme Sande (ölgebunden!); O: kein Aufwirbeln, ggf. Absaugung; P: FFP2 bei Sandaufbereitung. Quarzfeinstaub ist krebserzeugend (A-Staub) [Q15 – Grenzwerte prüfen] |
| G6 | CO₂-Begasung (Kernhärtung) | Kernmacherei | O: belüfteter Raum, kleine Gasmengen [Q14] |
| G7 | Brandgefahr (Holzmodelle, Papier nahe Kochplatte) | Schmelzbereich | O: brennbare Stoffe entfernen, Löschmittel: **kein Wasser auf Metallschmelze** → Löschsand/Metallbrandlöscher bereitstellen |
| G8 | Metalldämpfe/Oxide | Schmelzen | Bei Sn < 300 °C vernachlässigbarer Dampfdruck [Fachwissen – prüfen]; dennoch Lüftung; kein Cd, kein Pb (→ `werkstoffe.md`) |
| G9 | **Rauch/Geruch durch verbrennendes Speiseöl** (Rauchpunkt ~200 °C < T_Gieß 280 °C) | Abguss in Ölsandform (E4) | T: Ölanteil minimieren (V-F1); O: Lüftung/Abzug am Gießplatz, Rauchmelder-Situation im Labor klären; P: bei Bedarf FFP2 |
| G10 | Verbrennung/Handling am Nabertherm-Ofen (E6) | Tiegel einsetzen/entnehmen | T: passende Tiegelzange, Ofenhandschuhe; O: Ofentür-Routine im Skript festlegen, Abstellplatz für heißen Tiegel definieren; P: Hitzeschutz [Q16] |

## PSA-Grundausstattung Laborversuch

- [ ] Schutzbrille/Gesichtsschutz (beim Gießen)
- [ ] Hitzebeständige Handschuhe (Gießen/Handling Tiegel)
- [ ] Baumwollkittel — **keine leichtschmelzenden Synthetikfasern** [Q16]
- [ ] Festes, geschlossenes Schuhwerk (S-Klasse im Labor üblich)
- [ ] FFP2 bei stauberzeugenden Arbeiten

## Organisatorisches für das Versuchsskript

- [ ] Sicherheitsunterweisung als Pflichtteil vor Versuchsbeginn (Vorlage [Q17])
- [ ] Gefährdungsbeurteilung wird vom Projektteam **selbst erstellt** (F5 beantwortet) — HAW-Vorlage besorgen, G1–G10 als Grundlage
- [ ] Fehlerprovokationen (→ `gussfehler_provokation.md`) sicherheitsseitig freigeben: keine Feuchte-Provokation, Beschwerung nie ganz weglassen
- [ ] Betriebsanweisung Schmelzplatz erstellen (Aushang)
- [ ] Gefährdungsbeurteilung formal mit HAW-Vorlage erstellen und freigeben lassen
- [ ] Max. Personenzahl am Gießplatz festlegen
- [ ] Erste-Hilfe: Kaltwasser für Verbrennungen erreichbar

**Merksatz:** Die niedrige Schmelztemperatur reduziert, aber eliminiert die Gefahren nicht — 200 °C flüssiges Metall verursacht schwere Verbrennungen, und die Feuchte-Dampfschlag-Gefahr ist temperaturunabhängig ab T > 100 °C.
