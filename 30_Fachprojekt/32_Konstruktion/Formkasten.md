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

Datum der Messung: 10.08.2026. Gemessen: Fynn Barmwater.

**Führungssystem:** Stifte (Ausführung/Anzahl/Position nicht weiter spezifiziert — bei Bedarf für Fertigungszeichnung nachtragen, ob zusätzlich Buchsen vorhanden sind).
**Zustand:** gut (keine Beschädigungen berichtet — Detailkriterien wie Dichtheit der Teilungsebene und Verzug wurden nicht einzeln abgefragt).

> **Auslegungsfrage (kein Konflikt mit der Aufgabenstellung, Team-Entscheidung 10.08.2026):** Bei Kranz-Außendurchmesser Ø 70 mm ([[Bauteilkonzept]]) hängt die Sandumhüllung von der **Orientierung des Modells im Kasten** ab. Wird die Rotationsachse entlang der 90-mm-Breite gelegt, bleiben nur (90 − 70) / 2 = 10 mm je Seite — unter der Faustregel ≥ 30–50 mm. **Legt man das Modell stattdessen so ein, dass die Scheibenebene (Ø 70) in die 190-mm-Länge fällt — die Rotationsachse also quer, entlang der 90-mm-Breite —**, ergibt sich radial (190 − 70) / 2 = **60 mm je Seite** — komfortabel im Rahmen. In dieser Orientierung liegt die Achsrichtung in der 90-mm-Breite: Kernlänge inkl. Kernmarken ≈ 50 mm (Ø14×~50 mm) → (90 − 50) / 2 = **20 mm je Seite**, unter der 30–50-mm-Faustregel, aber laut Faustregeltext bei kleinen Teilen/niedriger Gießtemperatur (Sn-Gießtemperatur ≈ 240–280 °C) tendenziell unkritisch [Fachwissen – Q1 prüfen]. Höhe (80 mm/Hälfte) ist mit Kranzradius 35 mm + 45 mm Restsand ausreichend.
> **Empfehlung:** Modell mit Achse entlang der 190-mm-Länge einformen, keine Anpassung des Kranzdurchmessers nötig. **Zu verifizieren:** ob 20 mm axiale Sandumhüllung an den Kernmarken beim Abguss ausreicht — im ersten Vorversuch (V-F1/V-Z1) praktisch prüfen, nicht nur rechnerisch annehmen. Reine Auslegungsentscheidung des Teams, keine Abweichung von der Aufgabenstellung → keine Rücksprache mit Prof. Pähler nötig (anders als F17).

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
