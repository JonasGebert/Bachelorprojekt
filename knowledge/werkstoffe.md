# Werkstoffauswahl (Gusswerkstoff)

> Quellen: [Q21]–[Q25] gemäß `literatur.md`. Schmelzpunkte reiner Metalle = etabliertes Stoffdatenwissen [Fachwissen – Standardtabellenwerk zitieren, z. B. Q1 Anhang].

## ✅ ENTSCHIEDEN (E3, 04.07.2026): Reinzinn

Begründung: Budget unkritisch (F2); Nabertherm-Ofen 5,5 kW verfügbar (E6) → Temperaturreserve; Einstoffsystem → problemloses Recycling durch Folgegruppen; ungiftig; **sichtbare Erstarrungsschwindung** ist für das Zwei-Teile-Didaktikkonzept (E7, Lunkerprovokation) erwünscht — genau der Grund, warum Sn-Bi (schwindungskompensiert) verworfen wurde.

Prozessfenster: T_S = 232 °C; Gießtemperatur Version O ~280 °C, Version F bewusst ~240 °C (→ `gussfehler_provokation.md`). Temperaturkontrolle: Thermoelement/Pyrometer (E9, F18).

**Beschaffungshinweis:** Reinzinn ≥ 99,9 % (bleifrei) beschaffen, z. B. [Q23][Q24]; kein Lötzinn (Flussmittelkern, Legierungszusätze!).

---

## Archiv: ursprüngliche Auswahlanalyse (Kochplatten-Randbedingung, überholt durch E6)

Ursprüngliche Anforderung: Erschmelzen auf **einfacher Kochplatte** (A5) → Obergrenze Gießtemperatur ~250–300 °C. Mit dem Nabertherm-Ofen entfällt diese Grenze; die Werkstoffanforderung „niedrigschmelzend" (A5) bleibt durch Reinzinn erfüllt. Abweichung dokumentiert in E6.

## Kandidaten

| Werkstoff | Schmelzpunkt/-bereich | Gießtemp. (ca.) | Kosten | Arbeitsschutz | Bewertung |
|---|---|---|---|---|---|
| Reinzinn Sn | 232 °C | 260–300 °C | hoch (~30–40 €/kg) [prüfen] | unkritisch (bleifrei) | **gut**, grenzwertig für Kochplatte |
| Sn-Bi eutektisch (Bi57Sn43) | 138 °C [Q21][Q22] | 170–200 °C | mittel–hoch | unkritisch | **sehr gut**: große Sicherheitsreserve |
| Sn-Bi untereutektisch (z. B. Sn60Bi40) | ~138–170 °C Bereich [Q22] | ~200 °C | mittel–hoch | unkritisch | gut |
| Woodsches Metall | ~70 °C | ~100 °C | hoch | **Cadmium → toxisch, ausgeschlossen** | nein |
| Field'sches Metall (Bi-In-Sn) | ~62 °C | ~90 °C | sehr hoch (Indium) | unkritisch | nein (Kosten) |
| Blei/Pb-Legierungen | 327 °C | 380 °C | gering | **toxisch für Lehrbetrieb, ausgeschlossen** | nein |
| Zamak (Zn-Al) | ~380–390 °C | 420–440 °C | gering | Zinkdampf | nein: Kochplatte unzureichend |
| Al-Legierungen | ~660 °C | 700–750 °C | gering | hohe Temp. | nein (A5 verletzt) |

## Analyse Sn-Bi

Bi-Sn-Legierungen schmelzen je nach Zusammensetzung zwischen 138 °C und ca. 170 °C [Q22]. Besonderheit: Bismut **dehnt sich beim Erstarren aus**; in Sn-Bi-Legierungen kompensiert das die Schwindung teilweise → scharfe Konturabbildung, geringe Lunkerneigung [Q21 – für Bericht Primärquelle nachtragen]. Das ist didaktisch ein Nachteil für das Thema „Schwindung erleben", aber ein Vorteil für Prozesssicherheit.

Reines Zinn ist auf Haushaltsherd gießbar (Praxisindiz [Q25]), liegt aber mit T_Gieß ≈ 280 °C nahe der Kochplattengrenze.

## Bewertung und Empfehlungsrichtung

**Zielkonflikt:** Prozesssicherheit + niedrige Temperatur (→ Sn-Bi) vs. Kosten bei ~4 Studierendengruppen und Materialkreislauf (Bi ist teuer, aber Recycling minimiert Bedarf) vs. didaktischer Wert sichtbarer Schwindung (→ Sn).

Empfehlung [vorläufig, durch Vorversuch V-W1 zu bestätigen]: **Sn-Bi nahe Eutektikum** als Primärkandidat, Reinzinn als Referenz mitprüfen. Benötigte Menge = f(Bauteilvolumen + Gießsystem) → Berechnung nach Bauteilentwurf.

## Vorversuch V-W1 (Checkliste, aktualisiert für Ofen + Reinzinn)

- [ ] Nabertherm-Ofen: Typenschild dokumentieren (F15); Aufheizkurve auf 300 °C aufnehmen
- [ ] Aufschmelzzeit für Versuchsmenge (~1 kg Sn im Tiegel) messen → Taktung im 3-h-Fenster; Ofen ggf. vor Versuchsbeginn starten
- [ ] Temperaturmessung validieren: Thermoelement vs. Pyrometer an derselben Schmelze (Emissionsgradproblem quantifizieren → E9)
- [ ] Probeguss: Formfüllung bei 240 °C vs. 280 °C (Datenbasis für Kaltlauf-Provokation V-G2)
- [ ] Recyclingzyklen: Oxid-/Krätzeverlust nach n Zyklen wiegen → Nachkaufbedarf pro Semester abschätzen
- [ ] Tiegel- und Handlingkonzept festlegen (Zange, Handschuhe, Gießweg)
