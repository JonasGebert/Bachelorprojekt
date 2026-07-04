# Schwindung

> Quellen: gestützt auf Gestaltungsgrundlagen [Q12] und Lehrbuchwissen [Q1]. Konkrete Schwindmaße für Sn/Sn-Bi = [Fachwissen – experimentell im Vorversuch bestimmen, das ist ohnehin sauberer als Literaturwerte].

## Drei Phasen der Volumenkontraktion

| Phase | Bezeichnung | Kompensation |
|---|---|---|
| flüssig (T_Gieß → T_Liquidus) | Flüssigkontraktion | Nachlaufen aus Eingusssystem |
| Erstarrung (Liquidus → Solidus) | **Erstarrungsschwindung** → Lunkergefahr | **Speiser** |
| fest (Solidus → RT) | **Festkörperschwindung** → Maßabweichung | **Schwindmaß am Modell** |

Gesamtschwindung je nach Werkstoff ca. 2–4 Vol.-% (allgemeiner Richtwert für Gusswerkstoffe, [GTR-Glossar/Q12-Umfeld]); lineares Schwindmaß gängiger Werkstoffe ~1–2 %.

**Besonderheit Projekt:** Bi-haltige Legierungen dehnen sich beim Erstarren aus → nahezu schwindungskompensiert (→ `werkstoffe.md`). Konsequenz: Schwindmaß des Modells hängt direkt von der Werkstoffentscheidung ab → **Werkstoff vor finaler Modellfertigung festlegen!**

## Schwindmaß am Modell

```
L_Modell = L_Bauteil · (1 + s)
s = lineares Schwindmaß [-]
Beispielwerte: Gusseisen ~0,01; Al-Leg. ~0,012; Stahl ~0,02
Sn / Sn-Bi: s klein (< 0,005 erwartet) → experimentell bestimmen (V-S1)
```

## Vorversuch V-S1: Schwindmaßbestimmung

- [ ] Stabprobe definierter Länge (z. B. 200 mm) gießen
- [ ] Formmaß vs. Bauteilmaß bei RT messen (Messschieber, 3 Wiederholungen)
- [ ] s = (L_Form − L_Guss)/L_Form berechnen, Streuung angeben
- [ ] Ergebnis fließt in CAD-Modellmaße ein (→ `modellbau.md`)

## Konstruktive Konsequenzen (→ auch `gießfehler.md`)

- Materialanhäufungen vermeiden → dort entstehen Lunker (letzterstarrende Bereiche)
- Gleichmäßige Wandstärken anstreben [Q12]
- Speiser an dickster Stelle, gerichtete Erstarrung zum Speiser hin
- Heuvers'sche Kreismethode zur Kontrolle: einbeschriebene Kreise müssen zum Speiser hin wachsen [Fachwissen – Q1 prüfen]
