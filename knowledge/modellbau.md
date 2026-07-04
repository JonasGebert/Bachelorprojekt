# Modellbau

> Quellen: [Q12] gießgerechtes Konstruieren, [Q18] DIN EN 12890 (Modelle/Kernkästen), GTR-Glossar. Rest [Fachwissen – Q1 prüfen].

## Anforderungen an das Modell

Das Modell bildet die Außenkontur des Bauteils ab, **vergrößert um das Schwindmaß** (→ `schwindung.md`) und ggf. Bearbeitungszugaben (DIN EN ISO 8062-3 [Q19]). Anforderungen an Modelle und Kernkästen regelt DIN EN 12890 [Q18].

| Anforderung | Umsetzung |
|---|---|
| Formschrägen | in Ausheberichtung; Angabe in Grad in der Zeichnung nach DIN EN 12890 [Q18]; für Handformen typ. 1–3° [Fachwissen] |
| Teilungsebene | möglichst eben, größter Querschnitt in Teilung; bei geteiltem Modell: Passstifte |
| Kernlager (Kernmarken) | Am Modell mit anformen; Kern eindeutig positioniert, gegen Auftrieb gesichert |
| Radien | keine scharfen Kanten → Sandausbrüche, Spannungen |
| Oberfläche | glatt (lackiert/versiegelt) → Aushebbarkeit, Abdruckqualität |
| Dauerhaltbarkeit | Laboreinsatz über Jahre → robustes Material, ersetzbar (CAD + 3D-Druck!) |

## Werkstoffvergleich Modell

| Material | Vorteile | Nachteile | Bewertung |
|---|---|---|---|
| Holz (klassisch) | Werkstatt-Standard, leicht nacharbeitbar | Feuchteempfindlich (Grünsand!), Handarbeit | gut |
| **3D-Druck PLA/PETG** | direkt aus CAD, reproduzierbar, Schwindmaß parametrisch änderbar, bei Verschleiß neu druckbar | Schichtrillen (schleifen/füllern), Kriechen bei Wärme (nur Formkontakt, unkritisch) | **sehr gut** |
| Aluminium (gefräst) | dauerhaft, präzise | Fertigungsaufwand/Kosten | Overkill für v1 |
| Kunststoff gegossen (PU) | glatt | Urmodell nötig | unnötig |

**✅ ENTSCHIEDEN (E5, 04.07.2026):** Modell und Kernkasten als 3D-Druck (privater Drucker vorhanden, Druck zulässig), Oberflächen gefüllert und geschliffen. Wegen E7 werden **zwei Modellvarianten** gedruckt (Version F/O, gleiches parametrisches CAD, → `bauteil_konzept.md`); der Kernkasten ist für beide identisch. Begründung: Reproduzierbarkeit (Labor braucht ggf. Ersatz), parametrisches Schwindmaß, geringe Kosten, moderne durchgängige CAD-CAM-Kette als didaktischer Mehrwert. Risiko: Schichthaftung der Trennflächen, Verzug beim Druck großer Flächen → Probedruck.

## Checkliste Modellkonstruktion (CAD)

- [ ] Bauteilgeometrie + Schwindmaß s (Werkstoffentscheidung abwarten!)
- [ ] Formschrägen an allen aushebeparallelen Flächen
- [ ] Teilungsebene definiert, Modellhälften mit Passstiften
- [ ] Kernlager beidseitig, Spielpassung zum Kern definiert
- [ ] Radien an allen Kanten
- [ ] Eingusssystem/Speiser als separate Modellteile oder mit einformbar
- [ ] Zeichnungssatz nach DIN EN 12890 [Q18]
