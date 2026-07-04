# Gussfehler gezielt provozieren (Version F des Versuchsbauteils)

> Umsetzung von E7. Fehlerdefinitionen und Ursachen → `gießfehler.md` ([Q9][Q10][Q11]). Provokationsmethoden = ingenieurmäßige Umkehrung der Abhilfemaßnahmen; Wirksamkeit je Methode in Vorversuchen verifizieren (Spalte „V-G#").
>
> **Sicherheitsgrundsatz:** Es werden nur Fehler provoziert, die das Bauteil betreffen — **niemals** solche, die Personen gefährden. Insbesondere: **keine Provokation über nasse/feuchte Formen oder feuchtes Einsatzmaterial** (Dampfschlag/Metallauswurf, → `arbeitssicherheit.md` G2). Porosität wird über Ölüberschuss erzeugt, nicht über Wasser.

## Provokationskatalog

| Fehler | Provokation (Version F) | Erwartetes Bild am Bauteil | Didaktische Kernaussage | Sicherheit | Vorversuch |
|---|---|---|---|---|---|
| **Lunker** | Kein Speiser + vergrößerte Nabe (Materialanhäufung); Anschnitt erstarrt früh | Trichterförmiger Einfallhohlraum/Sauglunker oben in der Nabe, ggf. Einfallstelle | Erstarrungsschwindung braucht Nachspeisung; dickste Stelle erstarrt zuletzt [Q9] | unkritisch | V-G1 |
| **Kaltlauf / nicht ausgelaufene Form** | Gießtemperatur nur ~240 °C (knapp über T_S 232 °C) + dünner Steg 2,5 mm + zögerliches Gießen | Unvollständig gefüllter Steg, verrundete Konturen, „Fließhaut" | Mindestwandstärke + Überhitzung ΔT bestimmen die Formfüllung | unkritisch | V-G2 |
| **Kaltschweiße** | Wie V-G2; ggf. zweiter Anschnitt gegenüber → zwei kalte Fließfronten treffen sich am Kranz | Sichtbare Naht/Kerbe an der Zusammenflussstelle | Fließweglänge und Anschnittlage planen | unkritisch | V-G3 |
| **Gasporosität** | Ölanteil im Formsand deutlich erhöht (z. B. 2× Rezeptur) + keine Entlüftung | Runde, glattwandige Poren nahe Oberfläche; ggf. Blasen unter Gusshaut | Formgase müssen entweichen (Gasdurchlässigkeit, Entlüftung) [Q10] | **Rauchentwicklung → Abzug/Lüftung, kleiner Ölüberschuss, kein Wasser!** | V-G4 |
| **Sandeinschlüsse / Erosion** | Anschnitt direkt von oben auf den Steg (turbulent); Form vor dem Zulegen nicht ausblasen; lokal schwach verdichtet | Raue Stellen, eingebettete Sandkörner, „verwaschene" Kontur am Auftreffpunkt | Turbulenzarmes Gießsystem + Formfestigkeit [Q11] | unkritisch | V-G5 |
| **Versatz** | Führungsstifte der Formkästen bewusst nicht/falsch gesetzt (definiert um ~1–2 mm versetzt zulegen) | Kontursprung an der Teilungsebene, umlaufend | Führung Ober-/Unterkasten = Maßhaltigkeit | unkritisch, reversibel | V-G6 |
| **Grat / Schwimmhaut** | Oberkasten nur minimal beschwert; Teilungsflächen nicht sauber abgezogen | Dünne Metallhaut entlang Teilung und Kernmarken | Metallostatischer Auftrieb → Beschweren/Verklammern | **nur minimal dosieren** — zu wenig Beschwerung kann Schmelzaustritt verursachen → Beschwerung nur reduzieren, nicht weglassen; Auffangblech unterlegen | V-G7 |
| **Kernversatz/Kernauftrieb** (optional) | Kernmarkenspiel im Modell F vergrößern (Kern „schwimmt") | Exzentrische, verschobene Bohrung, einseitige Wandstärke | Kernlager = Passungssystem (→ `kernkasten.md`) | unkritisch | V-G8 |
| **Oberflächenrauheit** | Version F mit ungesiebtem, grobem Vogelsand einformen | Grobe, körnige Abdruckoberfläche | Körnung ↔ Oberflächengüte (Zielkonflikt zu Gasdurchlässigkeit) | unkritisch | V-G9 |

## Nicht provozierte Fehler (bewusst ausgeschlossen — Begründung)

| Fehler | Grund des Ausschlusses |
|---|---|
| Schülpen / Dampfblasen durch Formfeuchte | Sicherheitsrisiko Dampfschlag — Wasser hat am Gießplatz nichts zu suchen (G2) |
| Penetration/Vererzung | Bei 280 °C Gießtemperatur physikalisch kaum erreichbar |
| Warmrisse | Bei Sn und freier Schwindung unwahrscheinlich; scharfe Kehle in Version F kann Ansätze zeigen (Beobachtung dokumentieren) |
| Gefügefehler (Seigerung etc.) | Ohne Metallografie im Versuch nicht sichtbar → allenfalls Theorieteil |

## Auswahlempfehlung für den Laborversuch

Nicht alle 9 Provokationen in ein Bauteil packen — **Fehlerüberlagerung verwischt die Zuordnung** (mehrere Ursachen → ein Bild, didaktisch kontraproduktiv). Empfehlung: Version F kombiniert genau **drei gut trennbare Fehler**:

1. Lunker (kein Speiser, dicke Nabe) — Ort: Nabe
2. Kaltlauf (kalte Schmelze, dünner Steg) — Ort: Steg
3. Sandeinschluss/raue Oberfläche (Falleingus, grober Sand) — Ort: Kranz/Oberfläche

→ Jeder Fehler hat einen eigenen, vorhersagbaren Ort am Bauteil. Die übrigen Provokationen (V-G4, V-G6–V-G9) werden in den **Vorversuchen** durchgespielt und liefern Referenzfotos für den Fehlerkatalog im Versuchsskript.

## Auswertungsaufgabe für Studierende (Skript-Baustein)

- [ ] Version F und O nebeneinander: Fehler finden, benennen, Ursache zuordnen (Tabelle aus `gießfehler.md`)
- [ ] Je Fehler die konstruktive/prozessuale Gegenmaßnahme an Version O identifizieren
- [ ] Transferfrage: „Welche drei Änderungen würden Version F retten?"
- [ ] Maßvergleich Bohrung/Außenmaß beider Versionen (Schwindmaß, Kernlage)
