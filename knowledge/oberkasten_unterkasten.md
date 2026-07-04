# Formkasten (Ober- und Unterkasten)

> **Statusänderung 04.07.2026 (E8): Formkästen sind im Labor vorhanden — Eigenkonstruktion entfällt.**
> Achtung Konflikt F17: Aufgabenstellung A4 verlangt wörtlich Konstruktion + Fertigung der Form → mit Prof. Pähler klären. Ersatzleistung anbieten: vorhandene Kästen vermessen, nachkonstruieren (CAD) und Eignung technisch bewerten — damit ist der Kompetenznachweis erbracht.
>
> **Neue Aufgaben:** (F19) Innenmaße, Führungssystem und Zustand der vorhandenen Kästen aufnehmen → begrenzt Bauteilgröße (`bauteil_konzept.md`). Rest dieser Datei = Bewertungsgrundlage für die Eignungsprüfung. Überwiegend [Fachwissen – Q1 prüfen]; Fehlerbezug: Versatz → `gießfehler.md`.

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

Empfehlungsrichtung: v1 aus Holz für Vorversuche (schnell, billig, Geometrie iterierbar), finale Laborkästen aus Stahl/Alu — Entscheidung nach Vorversuchen (→ `entscheidungen.md`).

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
