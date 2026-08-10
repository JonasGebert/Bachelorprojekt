---
typ: konstruktion
titel: "Bauteilkonzept — zwei Werkstücke (Version F „Fehlerteil' / Version O „optimiert')"
status: in-arbeit
bereich: bp
tags:
  - bp
  - konstruktion
erstellt: 2026-07-04
aktualisiert: 2026-08-10
---

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

### Formaufbau (Vorschlag — **formtechnisch widerlegt, siehe F33**)

> ⛔ **Diese Darstellung ist nicht ausführbar.** Bei Teilung durch die Achse ist die Ringnut zwischen Nabe und Kranz ein **Hinterschnitt**: Die Kranz-Innenfläche Ø 54 umschließt den Nutsand unterhalb der Teilungsebene; beim senkrechten Ausheben der Modellhälfte reißt dieser Sand aus. Konsequenz: Die Teilungsebene muss **senkrecht zur Rotationsachse** liegen (Achse senkrecht, Kern steht). Damit ist auch die Antwort zu F29 hinfällig, weil Ø 70 in der 90-mm-Kastenbreite nur 10 mm Sandumhüllung lässt. → **F33**, entschieden wird vor jedem weiteren CAD-Schritt.

![[Formaufbau_Schnitt.svg]]

Zwei zueinander senkrechte Schnitte durch den geschlossenen Formkasten: Kernlagerung, Gießsystem, Speiser, Kühleisen, Sandumhüllung. **Abweichung von der Gießsystem-Tabelle oben:** Der Speiser sitzt dort „über der Nabe" — bei liegender Achse steht der Kranz im Weg, es bliebe nur Ø 6 mm (Modul 1,5 mm), nötig wären ≥ 3,2 mm. Vorschlag daher: Speiser Ø 14 mm oben auf den Kranz, Nabe über Kühleisen an den Stirnflächen zuerst erstarren lassen → offene Frage F32.

Erstarrungsmoduln aus den Konzeptmaßen (M = V/A, ohne Anschnitt/Speiser): Nabe 2,7 mm · Kranz 2,6 mm · Steg 2,5 mm. Die Moduln liegen dicht beieinander — es gibt **keinen ausgeprägten Speisungsweg**; genau das ist zu diskutieren.

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

### Prinzipskizze (maßstäblich, aus den obigen Konzeptmaßen erzeugt)

![[Bauteil-Riemenscheibe_Skizze.svg]]

![[Bauteil-Riemenscheibe_3D.png]]

> **Status der Skizze:** Prinzipdarstellung, **keine fertigungsreife Zeichnung** nach DIN EN 12890 [Q18]. Nicht enthalten: Schwindmaß (offen, → V-S1 / F10), Formschrägen 1–3°, Kernmarkenspiel/Passung, durchgängige Radien, Anschnitt/Speiser/Windpfeife, Toleranzen und Rauheiten.
> Erzeugt aus `tools/zeichnungen/bauteil_zeichnung.py` und `tools/zeichnungen/bauteil_3d.py` — Maßänderungen dort im Kopf der Datei (Objekte `VO`/`VF`) ändern und neu erzeugen, damit Tabelle und Skizze nicht auseinanderlaufen.

## Bauteilvorschlag 10.08.2026: **Stehbuchse mit Fußplatte** (zu F33)

> Zwei Entwürfe sind vorher an derselben Regel gescheitert. Der Nachweis wird deshalb hier explizit geführt und ist in `tools/zeichnungen/check_aushebbarkeit.py` nachrechenbar.

![[Stehbuchse_Vorschlag.svg]]

### Die maßgebende Regel (Aushebbarkeit)

Ein Modellteil lässt sich nur ziehen, wenn **jeder Schnitt parallel zur Teilungsebene in der Projektion des näher an der Teilung liegenden Schnitts liegt** — die Querschnittsfläche darf mit wachsendem Abstand von der Teilung nur **abnehmen**, nie zunehmen. Sonst müsste beim Ziehen ein breiterer Modellteil durch eine engere Sandöffnung; der Sand reißt aus.

| Entwurf | Ergebnis | Ort des Verstoßes |
|---|---|---|
| Riemenscheibe, Teilung durch die Achse | ✗ | Ringnut hinter der Kranz-Innenfläche Ø 54 |
| Lagerbock, waagerechte Bohrung | ✗ | Grundplatte springt von 160 auf 4400 mm² |
| **Stehbuchse, senkrechte Bohrung** | **✓** | monoton fallend über die gesamte Höhe |

### Geometrie Version O

| Element | Maß |
|---|---|
| Fußplatte | 110 × 36 × 7 mm, Unterseite = Teilungsebene |
| Nabe | Ø 34 außen, Bohrung Ø 18, h = 7 … 47 mm |
| Rippen | 2 × 5 mm dick, Fußlänge 25 mm, Höhe 25 mm |
| Kehlen / Formschrägen | R4 / 2° |
| Kern | Ø 18, stehend; unten Kernlager 15 mm, oben im Ringspeiser geführt |
| Volumen / Masse | 57 cm³ → ≈ 415 g Sn |
| Kastenpassung (190 × 90) | 40 mm Sand stirnseitig, 27 mm seitlich |

### Warum der Aufbau zusätzlich einfach ist

Das gesamte Bauteil liegt **im Oberkasten**; der Unterkasten ist eine ebene Sandfläche mit einem einzigen Loch — dem Kernlager. Querlauf und Anschnitt werden in diese ebene Fläche eingeschnitten. Das Modell ist **einteilig** (keine Teilung, keine Passstifte) und damit als 3D-Druck deutlich einfacher als ein geteiltes Modell → stützt E5.

### Gießtechnik

Moduln: Nabe 3,64 mm · Fußplatte 3,06 mm. Ringspeiser Ø 38/Ø 18 über der Nabe: M = 5,00 mm ≥ 1,2 · 3,64 = 4,36 mm ✓. Kernauftrieb F = V · Δρ · g = 0,65 N (≈ 66 g) — der Kern wird nach oben gedrückt und liegt damit sicher an seiner oberen Führung an.

### Offen

- [ ] Ob der Ringspeiser die Fußplatte über den Knoten mitspeist, ist im Vorversuch zu **messen**
- [ ] Schwindmaß (V-S1 / F10), Kernmarkenspiel, Formschrägenrichtung im CAD
- [ ] Freigabe durch Team (F33) und Prof. Pähler

---

## Verworfen: Lagerbock mit waagerechter Bohrung (10.08.2026)

Zwischenentwurf, ebenfalls nicht aushebbar: Die Grundplatte liegt 39 mm unter der Teilungsebene und ist breiter als alles darüber — beim Ziehen müsste die 100 × 44 mm große Platte durch die 32 × 5 mm große Rippenöffnung im Sand. Zeichnung `Lagerbock_Vorschlag.svg` bleibt zur Dokumentation des Denkwegs erhalten, ist aber **ungültig**.

