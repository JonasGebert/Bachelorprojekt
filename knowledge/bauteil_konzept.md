# Bauteilkonzept — zwei Werkstücke (Version F „Fehlerteil" / Version O „optimiert")

> Umsetzung von E7. Status: **Konzeptvorschlag zur Diskussion** (F14). Maße vorläufig — Obergrenze durch Innenmaße der vorhandenen Formkästen (F19) verifizieren!

## Grundprinzip

**Gleiche Bauteilgeometrie, zwei Ausführungen des Gießprozesses/Gießsystems.** Didaktischer Vorteil: Die Studierenden sehen, dass die Fehler nicht „im Bauteil", sondern in Gestaltung und Prozess entstehen — exakt die Lehre des gießgerechten Konstruierens [Q12]. Zusätzlich enthält Version F zwei bewusst schlechte Geometriedetails (dünner Steg, scharfe Kehle), Version O die korrigierten.

## Vorgeschlagenes Bauteil: Miniatur-Riemenscheibe mit Nabenbohrung

Klassisches Handform-Lehrbeispiel (Riemenscheibe liegend eingeformt, geteiltes Modell, horizontaler Kern — Standardbeispiel der FT-Lehrbücher [Q1 – Kapitel Urformen prüfen]). Erfüllt alle Anforderungen: reales Maschinenelement (A2), zwingend ein Kern für die Nabenbohrung (A3), eine ebene Teilungsebene durch die Rotationsachse, didaktisch reich (Kranz = Materialanhäufung, Steg = Dünnstelle, Nabe = Kernumguss).

### Geometrie (vorläufig, CAD folgt)

| Element | Version O (optimiert) | Version F (fehlerprovozierend) |
|---|---|---|
| Außendurchmesser Kranz | Ø 70 mm | Ø 70 mm |
| Kranzbreite × -dicke | 20 × 8 mm | 20 × 8 mm |
| Steg (Scheibe zwischen Nabe und Kranz) | 5 mm, Übergangsradien R3 | **2,5 mm, scharfe Kehlen R0** → Kaltlauf-/Rissprovokation |
| Nabe | Ø 28 mm × 24 mm | Ø 36 mm × 24 mm → **größere Materialanhäufung** → Lunker |
| Nabenbohrung (Kern) | Ø 14 mm | Ø 14 mm |
| Kern | Ø 14 × ~50 mm inkl. beidseitiger Kernmarken Ø 14 × 12 mm | identisch |
| Masse (Sn, ρ = 7,3 g/cm³) | grob 0,4–0,5 kg | ähnlich |

### Gießsystem

| Element | Version O | Version F |
|---|---|---|
| Anschnitt | seitlich in den Kranz, turbulenzarm | von oben direkt auf den Steg (Erosion, Spritzer) |
| Speiser | über der Nabe (dickste Stelle, erstarrt zuletzt) | **kein Speiser** → Sauglunker in der Nabe |
| Entlüftung | Windpfeife am Kranz gegenüber Anschnitt | keine |
| Gießtemperatur | ~280 °C (gemessen, Thermoelement) | ~240 °C (knapp über Liquidus) → Kaltlauf |

### Skizze (Prinzip, Schnitt durch Achse; Teilung = Achsebene)

```
            Speiser (nur V-O)
               ┌──┐
   ╔═══════════╪══╪═══════════╗   ← Kranz 20×8
   ║   ┌───────┴──┴───────┐   ║
   ╚═══╡      Steg        ╞═══╝   ← Steg 5 (O) / 2,5 (F)
       │  ┌────────────┐  │
═══════╪══╡####Kern####╞══╪═══════ ← Kernmarken beidseitig
       │  └────────────┘  │
       └──────Nabe────────┘
─────────────────────────────────  Teilungsebene (durch Achse)
```

## Verworfene Alternative (dokumentiert)

**Lagerbock mit Durchgangsbohrung:** ebenfalls geeignet (ebene Teilung, ein Kern), aber weniger Fehler-„Bühnen" (kein Kranz/Steg-Kontrast) und als Zinnteil funktional unplausibler. Bleibt Rückfalloption, falls Riemenscheibe nicht in die vorhandenen Formkästen passt (F19).

## Konsequenzen für Modell/Kernkasten

- Geteiltes Modell (2 Hälften, verstiftet), Teilung durch Achse → `modellbau.md`
- Bei zwei Geometrievarianten (Steg/Nabe): **zwei Modellvarianten drucken** — Mehraufwand beim 3D-Druck gering, da parametrisches CAD (eine Datei, zwei Parametersätze)
- Ein Kernkasten für beide Versionen (Kern identisch) → `kernkasten.md`
- Schwindmaß aus V-S1 vor finalem Druck einpflegen

## Offene Punkte

- [ ] F19: Innenmaße Formkästen vermessen → Ø 70 mm + Gießsystem prüfen
- [ ] Abkühlzeit 0,5 kg Sn in Ölsandform messen (Zeitbudget 3 h!) → V-Z1
- [ ] Freigabe des Konzepts durch Prof. Pähler
