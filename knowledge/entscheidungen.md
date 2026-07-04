# Entscheidungslog

> Jede technische Entscheidung: Kontext, Alternativen, Kriterien, Begründung, Status. Vorläufige Empfehlungen sind KEINE Entscheidungen.

## Vorlage

```
### E## — Titel (Datum)
Status: vorgeschlagen | entschieden | revidiert
Kontext:
Alternativen:
Kriterien:
Entscheidung + Begründung:
Konsequenzen / betroffene Dokumente:
Quellen:
```

---

### E1 — Gießverfahren: Handformverfahren, zweiteiliger Formkasten, verlorene Sandform (04.07.2026)

Status: **entschieden** (durch Aufgabenstellung determiniert)
Kontext: Aufgabenstellung fordert Form aus Ober-/Unterkasten, Kernkasten, Modell (A4).
Alternativen: keine echten — Kokille/Feinguss würden A4 verletzen.
Konsequenzen: Prozesskette gemäß `gießverfahren.md`.
Quellen: `Aufgabenstellung/aufgabenstellung.md`

### E2 — Dokumentations-/Quellensystem (04.07.2026)

Status: **entschieden**
Kontext: Wissensbasis wurde vor Beschaffung der Primärliteratur aufgebaut.
Entscheidung: Zwei-Stufen-Kennzeichnung `[Q##]` (geprüft) vs. `[Fachwissen – Quelle nachtragen]`; nichts davon ungeprüft in den Bericht.
Konsequenzen: Vor Berichtsschreiben Q1 beschaffen und alle Fachwissen-Tags auflösen.

### E3 — Werkstoff: Reinzinn (04.07.2026)

Status: **entschieden** (Jonas/Team)
Kontext: Budget vorerst unkritisch; Nabertherm-Ofen statt Kochplatte verfügbar → Temperaturreserve groß.
Alternativen: Sn-Bi eutektisch (138 °C) — verworfen: teurer, Bi kompensiert Schwindung (didaktisch unerwünscht, da Lunker/Schwindung gelehrt werden sollen).
Begründung: Einstoffsystem (einfaches Recycling ohne Entmischungsfragen), ungiftig, T_S = 232 °C, sichtbare Erstarrungsschwindung → passt zum Zwei-Teile-Didaktikkonzept (E7).
Konsequenzen: Gießtemperatur ~260–300 °C; Schwindmaß über V-S1 bestimmen; `werkstoffe.md`, `materialkunde.md`.

### E4 — Formsand: Vogelsand + Speiseöl (04.07.2026)

Status: **entschieden** (Form); Kernbinder **offen** (F12)
Begründung: Hochschulbudget + Nachhaltigkeit; ölgebundener Sand ist lagerfähig, fehlerverzeihend, wiederverwendbar.
Risiken/Auflagen: Vogelsand enthält oft Kalk-/Muschelgrit und Anisöl → **sieben und Eignung in V-F1 nachweisen**; Ölanteil begrenzen (Rauchentwicklung beim Abguss, → `arbeitssicherheit.md` G9). Rezeptur (Ölanteil, Verdichtung) über V-F1.
Details: `formsand.md`, `binder.md`

### E5 — Modell + Kernkasten: 3D-Druck (04.07.2026)

Status: **entschieden** — privater 3D-Drucker vorhanden, Druck ausdrücklich zulässig.
Konsequenzen: Oberflächen füllern/schleifen; Probedruck vor Serienfertigung; `modellbau.md`, `kernkasten.md`.

### E6 — Wärmequelle: Nabertherm-Ofen 5,5 kW statt Kochplatte (04.07.2026)

Status: **entschieden** (Randbedingung Labor)
Kontext: Aufgabenstellung nennt „einfache Kochplatte" (A5). Der Ofen übererfüllt dies; Werkstoffanforderung „niedrigschmelzend" bleibt durch Reinzinn gewahrt. Abweichung im Bericht dokumentieren.
Offen: exakter Ofentyp/Tmax (F15); Tiegel-/Handlingkonzept (Zange, PSA).

### E7 — Didaktikkonzept: zwei Werkstücke (04.07.2026)

Status: **entschieden**
Ein Bauteil, zwei Abgüsse: Version F mit **gezielt provozierten Gussfehlern**, Version O **optimiert** (fehlerfrei). Studierende vergleichen, klassifizieren Fehler und begründen die Optimierungen.
Konsequenzen: `bauteil_konzept.md`, `gussfehler_provokation.md`; ggf. zwei Modellvarianten bzw. wechselbare Gießsystem-Einsätze.

### E8 — Formkästen: vorhandene Kästen nutzen (04.07.2026)

Status: **entschieden, unter Vorbehalt F17**
Konflikt mit Wortlaut A4 („Sie konstruieren und fertigen … die Form") → mit Prof. Pähler klären; Ersatzleistung ggf. Vermessung/Nachdokumentation (F19).

### E9 — Temperaturmessung (offen)

Status: **vorgeschlagen** — Einstech-Thermoelement Typ K als Primärmessmittel; IR-Pyrometer nur ergänzend (niedriger/instabiler Emissionsgrad blanker Sn-Schmelze → Fehlmessung [Fachwissen – prüfen]).
Blockiert durch: F18 (Beschaffungsentscheidung).
