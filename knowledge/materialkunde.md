# Materialkunde (werkstofftechnische Grundlagen)

> Grundlagenwissen zur Einordnung; für den Bericht gegen [Q1] (Kap. Werkstofftechnik/Urformen) belegen. Projektspezifische Werkstoffauswahl → `werkstoffe.md`.

## Erstarrung metallischer Schmelzen

- **Reine Metalle** (z. B. Sn): erstarren bei konstanter Temperatur (Haltepunkt) — glatte Erstarrungsfront.
- **Legierungen**: erstarren im Intervall Liquidus–Solidus; im Zweiphasengebiet breiiger Zustand → Neigung zu Mikrolunkern/Speisungsproblemen wächst mit Intervallbreite.
- **Eutektische Legierungen** (z. B. Bi57Sn43, 138 °C [Q22]): erstarren wie reine Metalle bei konstanter Temperatur → gute Gießbarkeit, gute Formfüllung. **Deshalb sind eutektische/nahe-eutektische Legierungen klassische Gusslegierungen.**

```
Gießbarkeit ~ f(Erstarrungsintervall, Viskosität, Oberflächenspannung,
               Überhitzung ΔT = T_Gieß − T_Liquidus)
Faustregel Überhitzung: ΔT ≈ 50–100 K [Fachwissen – prüfen]
```

## Für das Projekt relevante Stoffdaten (zu verifizieren/vermessen)

| Größe | Sn | Bi57Sn43 | Quelle |
|---|---|---|---|
| Schmelzpunkt | 232 °C | 138 °C | [Q21][Q22] |
| Dichte (fest) | 7,3 g/cm³ | ~8,6 g/cm³ | [Fachwissen/Q22 – prüfen] |
| Volumenverhalten bei Erstarrung | Kontraktion | nahezu neutral bis Expansion (Bi-Anteil) | [Q21 – Primärquelle nachtragen] |
| Wärmekapazität/Schmelzenthalpie | — | — | [nachschlagen; für Aufschmelzzeit-Abschätzung] |

## Abschätzung Aufschmelzenergie (Beispielrechnung, Struktur)

```
Q = m · [c_p,fest · (T_S − T_0) + ΔH_S + c_p,fl · (T_Gieß − T_S)]
P_Kochplatte,eff = η · P_nenn   (η unbekannt → V-W1 messen)
t_Aufschmelz ≈ Q / P_eff
```

Zahlenwerte erst nach Stoffdatenrecherche + Kochplattenmessung einsetzen — **keine Scheinpräzision**.

## Gefügehinweis

Langsame Abkühlung im Sand → grobes Gefüge; für Funktionsbauteile relevant, für den Laborversuch sekundär. Interessanter didaktischer Nebenaspekt: Schliffprobe eines Gussteils als Zusatzaufgabe (falls Metallografie-Labor verfügbar).
