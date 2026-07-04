# Kernkasten

> Normbezug: DIN EN 12890 (Modelle, Modelleinrichtungen und Kernkästen) [Q18]. Rest [Fachwissen].

## Funktion

Der Kernkasten ist das „Negativ" des Kerns: In ihn wird der Kernsand eingefüllt und verdichtet; nach dem Härten wird der Kern entnommen. Er gehört laut Aufgabenstellung (A4) zu den selbst zu konstruierenden und zu fertigenden Betriebsmitteln.

## Bauarten

| Bauart | Beschreibung | Eignung |
|---|---|---|
| Geteilter Kernkasten (2 Hälften, liegend) | Standard für zylindrische/prismatische Kerne; Hälften verstiftet | **hoch** |
| Ungeteilter Kasten (Füllöffnung oben) | nur für einfache konische Kerne | begrenzt |
| Mehrteilig mit Losteilen | komplexe Kerne | vermeiden (v1 einfach halten) |

## Konstruktionsanforderungen

- Kernkontur inkl. **Kernmarken** (Lagerzapfen) abbilden — Maßbezug: Kernlager im Modell (gemeinsame Passungsdefinition!)
- Konizität/Formschrägen zur Entnahme des ungehärteten bzw. gehärteten Kerns
- Passstifte + Spannmöglichkeit (Schraubzwinge/Klammern) für die Hälften
- Einfüllöffnung mit Trichteransatz; Überstand zum Abstreifen
- Bei CO₂-Härtung: Begasungsöffnung(en) vorsehen [Q14]
- Material: 3D-Druck analog Modell (→ `modellbau.md`) → identische Fertigungskette, parametrische Anpassung

## Merksatz

**Kern, Kernkasten und Kernlager im Modell sind EIN Passungssystem.** Änderung an einer Stelle erfordert Prüfung der anderen beiden → im CAD als Baugruppe mit verknüpften Parametern aufbauen.

## Checkliste

- [ ] Kerngeometrie aus Bauteil-CAD abgeleitet (ohne Schwindmaß? → Kern schwindet nicht, aber Gussteil um den Kern: Maßkette sauber definieren!)
- [ ] Teilungsebene Kernkasten = Symmetrieebene Kern
- [ ] Formschrägen + Radien
- [ ] Verstiftung + Spannkonzept
- [ ] Begasungs-/Entlüftungskonzept
- [ ] Zeichnung nach DIN EN 12890 [Q18]
