---
typ: konstruktion
titel: "Formkasten (Ober- und Unterkasten)"
status: offen
bereich: bp
tags:
  - bp
  - konstruktion
  - form
erstellt: 2026-07-04
aktualisiert: 2026-08-10
---

# Formkasten (Ober- und Unterkasten)

> **Statusänderung 04.07.2026 (E8): Formkästen sind im Labor vorhanden — Eigenkonstruktion entfällt.**
> Achtung Konflikt F17: Aufgabenstellung A4 verlangt wörtlich Konstruktion + Fertigung der Form → mit Prof. Pähler klären. Ersatzleistung anbieten: vorhandene Kästen vermessen, nachkonstruieren (CAD) und Eignung technisch bewerten — damit ist der Kompetenznachweis erbracht.
>
> **Neue Aufgaben:** (F19) Innenmaße, Führungssystem und Zustand der vorhandenen Kästen aufnehmen → begrenzt Bauteilgröße ([[Bauteilkonzept]]). Rest dieser Datei = Bewertungsgrundlage für die Eignungsprüfung. Überwiegend [Fachwissen – Q1 prüfen]; Fehlerbezug: Versatz → [[Giessfehler]].

## Funktion

Der zweiteilige Formkasten nimmt den verdichteten Formsand auf. Der **Unterkasten** enthält i. d. R. die Bauteilkontur unterhalb der Teilungsebene, der **Oberkasten** die obere Kontur plus **Einguss, Speiser und Entlüftung**. Laut Aufgabenstellung (A4) selbst zu konstruieren und zu fertigen.

## Konstruktionsanforderungen

| Anforderung | Begründung | Umsetzung |
|---|---|---|
| Exakte Führung beider Kästen | Versatz vermeiden | Führungsstifte/Buchsen diagonal, Spielpassung |
| Steifigkeit | Verdichtungskräfte beim Aufstampfen | verschraubter/verschweißter Rahmen, ausreichende Wandstärke |
| Sandhaftung | Sandballen darf beim Wenden nicht herausfallen | Innenflächen rau; ggf. umlaufende Leisten/Rippen |
| Handhabbarkeit | Studierende wenden den Kasten von Hand | Masse begrenzen, Griffe anformen |
| Beschwerung/Verklammerung | metallostatischer Auftrieb auf Oberkasten | Auflagefläche für Gewichte oder Spannklammern |
| Temperaturbeständigkeit | Kontakt mit Schmelze nur indirekt | Holz ausreichend bei T < 300 °C; Metall dauerhafter |

## Werkstoffvergleich

| Material | Vorteile | Nachteile | Bewertung |
|---|---|---|---|
| Multiplex/Siebdruckplatte, verschraubt | einfache Fertigung in Hochschulwerkstatt, leicht | Feuchte (Grünsand), Verschleiß | **gut für v1** |
| Stahlprofil geschweißt | dauerhaft, steif — laborüblich (vgl. Foto der Aufgabenstellung: Metallkästen) | Fertigungsaufwand (Schweißen), Masse | **gut für finale Version** |
| Alu-Profil verschraubt | leicht, präzise, kein Schweißen | Kosten Profile | gut |

Empfehlungsrichtung: v1 aus Holz für Vorversuche (schnell, billig, Geometrie iterierbar), finale Laborkästen aus Stahl/Alu — Entscheidung nach Vorversuchen (→ [[Entscheidungsregister]]).

## Vermessung (F19) — Innenmaße vorhandene Kästen

| Größe | Wert | Messmittel | Messunsicherheit |
|---|---|---|---|
| Breite (Ober-/Unterkasten, je Hälfte gleich) | 90 mm | Gliedermaßstab | ± 1 mm [Fachwissen – typische Ableseunsicherheit bei Gliedermaßstab, Gelenkspiel; Q## nachtragen] |
| Länge | 190 mm | Gliedermaßstab | ± 1 mm |
| Höhe (je Hälfte) | 80 mm | Gliedermaßstab | ± 1 mm |

Datum der Messung: nicht angegeben — bitte ergänzen. Gemessen: [Person nachtragen].

> ⚠️ **Konflikt mit [[Bauteilkonzept]]:** Kranz-Außendurchmesser Version O/F = Ø 70 mm. Bei Breite = 90 mm bleibt bei zentrischer Lage nur (90 − 70) / 2 = **10 mm** Sandumhüllung je Seite — deutlich unter der Faustregel von ≥ 30–50 mm (siehe unten). Die Höhe (80 mm/Hälfte) ist mit Kranzradius 35 mm + 45 mm Restsand knapp im Rahmen, die Länge (190 mm) reicht für Nabe/Kernmarken/Gießsystem üppig. **Engpass ist die Breite.** Folgeoptionen: (a) Kranzdurchmesser reduzieren, (b) prüfen ob Gliedermaßstab-Ablesung an dieser Stelle stimmt (mit Messschieber gegenkontrollieren, da die Toleranz hier entscheidungsrelevant ist), oder (c) Rückfalloption Lagerbock (siehe [[Bauteilkonzept]], „Verworfene Alternative") erneut prüfen. Nicht selbst entscheiden — Freigabe/Klärung im nächsten Sprintwechsel mit Prof. Pähler.

## Auslegung Kastengröße (Faustregeln, [Fachwissen])

```
Sandumhüllung um Modell allseitig ≥ 30–50 mm (bei niedriger Gießtemperatur
und kleinen Teilen eher unkritisch, aber Kantenabstand für Festigkeit nötig)
Kastenhöhe ≥ Modellhöhe (je Hälfte) + Eingusshöhe im Oberkasten
Metallostatischer Druck: p = ρ · g · h  → Beschwerungsmasse des Oberkastens:
F_Auftrieb ≈ ρ_Schmelze · g · A_proj · h_über Teilung (konkret rechnen!)
```

## Checkliste

- [ ] Kastengröße aus Bauteil + Gießsystem abgeleitet
- [ ] Führungssystem (Stifte/Buchsen) definiert
- [ ] Wende- und Tragekonzept (Griffe)
- [ ] Beschwerungs-/Klammerkonzept gegen Auftrieb
- [ ] Fertigungszeichnungen für Hochschulwerkstatt
