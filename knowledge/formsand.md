# Form- und Kernsande

> Quellen: [Q5] [Q6] [Q8] Gießereilexikon; [Q4] Praxishandbuch bentonitgebundener Formstoff. Ungetaggte Zahlenwerte = [Fachwissen – vor Berichtsübernahme gegen Q1/Q4 prüfen].

## Aufbau synthetischer Formstoffe [Q5]

| Komponente | Funktion | Typischer Anteil |
|---|---|---|
| Quarzsand (Formgrundstoff) | Feuerfestes Gerüst | ~85–95 Ma.-% |
| Binder (Bentonit, Harz, Wasserglas …) | Zusammenhalt | Bentonit: ~6–10 Ma.-% |
| Wasser | Aktiviert Bentonit | ~2–4 Ma.-% |
| Zusatzstoffe (z. B. Glanzkohlenstoffbildner) | Oberflächengüte | gering |

Bei den niedrigen Gießtemperaturen des Projekts (< 300 °C, → `werkstoffe.md`) sind die thermischen Anforderungen an den Sand unkritisch; entscheidend sind **Formbarkeit, Festigkeit und Gasdurchlässigkeit**.

## Wichtige Formstoffeigenschaften und Prüfverfahren

| Eigenschaft | Bedeutung | Prüfung (VDG-Merkblätter P-Reihe [Q20]) |
|---|---|---|
| Verdichtbarkeit | Verarbeitbarkeit beim Aufstampfen | Verdichtbarkeitsprüfung |
| Grünfestigkeit (Druck/Scher) | Formstabilität nach Modellentnahme | Prüfkörper 50 mm, Druckversuch |
| Gasdurchlässigkeit | Abführen von Wasserdampf/Gasen → verhindert Gasblasen | Durchströmungsprüfung |
| Wassergehalt | Zu nass → Dampf, zu trocken → bröckelig | Darrprobe |
| Körnung/Kornverteilung | Oberflächengüte vs. Gasdurchlässigkeit | Siebanalyse |

**Zielkonflikt (Merksatz):** Feiner Sand → bessere Oberfläche, aber geringere Gasdurchlässigkeit. Für die Vorversuche beide Größen bewerten.

## ✅ ENTSCHIEDEN (E4, 04.07.2026): Vogelsand + Speiseöl (ölgebundener Formsand)

Begründung: Hochschulbudget + Nachhaltigkeit (Jonas/Team). Ölgebundener Sand ist lagerfähig, fehlerverzeihend, **wasserfrei** (→ keine Dampfschlaggefahr aus der Formfeuchte, großer Sicherheitsvorteil) und mehrfach wiederverwendbar.

**Kritische Auflagen (in V-F1 nachweisen, sonst Entscheidung revidieren):**

| Punkt | Problem | Maßnahme |
|---|---|---|
| Vogelsand-Zusätze | enthält oft Muschelgrit/Kalk (grobe Partikel) und Anisöl | **sieben** (z. B. < 0,5 mm), Charge dokumentieren; Kalkanteil bei 280 °C chemisch unkritisch, aber Kornstörer |
| Chargenkonstanz | „Vogelsand" ist kein genormter Formstoff — Körnung schwankt je Hersteller | eine Marke festlegen, Siebanalyse dokumentieren, im Skript vorschreiben |
| Ölanteil | zu viel → Rauch beim Abguss (Rauchpunkt Speiseöl ~200 °C < T_Gieß) + Gasporen; zu wenig → bröckelige Form | Rezepturreihe in V-F1 (z. B. 3/5/8 Ma.-%), Rauchentwicklung bewerten (→ `arbeitssicherheit.md` G9) |
| Ölalterung | Speiseöl verharzt/ranzt über Semester | Lagerung dicht, Sichtprüfung je Semester; ggf. Leinölfirnis testen (trocknet definiert, ebenfalls „Lebensmittel-nah") |

## Rezepturbestimmung V-F1 (ersetzt den früheren Sandtyp-Vergleich)

- [ ] Vogelsand sieben, Siebanalyse (grob) dokumentieren
- [ ] Rezepturreihe Ölanteil 3/5/8 Ma.-% — je: Formbarkeit, Kantenfestigkeit (Auszugversuch am Testmodell), Ballenhaftung beim Wenden
- [ ] Probeabguss je Rezeptur: Oberflächengüte, Gasporen, Rauchentwicklung
- [ ] Wiederverwendbarkeit: gleiche Charge n-mal nutzen, Festigkeitsverlust/Ölverlust bewerten, Auffrischregel ableiten
- [ ] Referenz mitlaufen lassen: 1 Abguss in gekauftem Ölsand (Vergleichsmaßstab, falls Budget es hergibt)
- [ ] Ergebnis-Rezeptur in `entscheidungen.md` E4 nachtragen (Ma.-%, Marke, Siebweite)

**Warnhinweis (bleibt gültig):** Auch bei ölgebundenem Sand gilt — **kein Wasser am Gießplatz**, kein feuchtes Einsatzmaterial in die Schmelze (→ `arbeitssicherheit.md` G2).

## Archiv: ursprünglicher Kandidatenvergleich (vor E4)

| Sandtyp | Bindung | Vorteile | Nachteile |
|---|---|---|---|
| Grünsand (bentonitgebunden) | Ton + Wasser | sofort wiederverwendbar, billig | Feuchte → Dampfblasen; Übung nötig |
| Ölgebundener Sand | Öl | lagerfähig, fehlerverzeihend, wasserfrei | Geruch/Rauch beim Guss |
| Wasserglas-CO₂-Sand | Na-Silikat + CO₂ | hohe Festigkeit → Kerne | Zerfall schlechter; CO₂-Handling |
| Furanharz o. ä. | Harz + Härter | sehr fest | Arbeitsschutz, Kosten, Overkill |
