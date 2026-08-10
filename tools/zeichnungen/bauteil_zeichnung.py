# -*- coding: utf-8 -*-
"""
Erzeugt eine bemasste Prinzipskizze (A3 quer, SVG) der Miniatur-Riemenscheibe
gemaess 30_Fachprojekt/32_Konstruktion/Bauteilkonzept.md.
Alle Masse in mm. Zeichnungsmassstab 1:1 (1 SVG-Einheit = 1 mm).
"""
import math

W, H = 420.0, 297.0   # A3 quer

class Geo:
    def __init__(self, name, d_kranz, b_kranz, s_kranz, d_nabe, l_nabe,
                 t_steg, r_uebergang, d_bohrung, l_kern_marke):
        self.name = name
        self.D, self.B, self.S = d_kranz, b_kranz, s_kranz
        self.Di = d_kranz - 2*s_kranz
        self.dN, self.lN = d_nabe, l_nabe
        self.t, self.r = t_steg, r_uebergang
        self.dB, self.lKM = d_bohrung, l_kern_marke

VO = Geo("Version O  —  optimiert", 70, 20, 8, 28, 24, 5.0, 3.0, 14, 12)
VF = Geo("Version F  —  fehlerprovozierend", 70, 20, 8, 36, 24, 2.5, 0.0, 14, 12)

out = []
def add(s): out.append(s)

def line(x1, y1, x2, y2, cls="voll"):
    add(f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" class="{cls}"/>')

def rect(x, y, w, h, cls="voll", extra=""):
    add(f'<rect x="{x:.3f}" y="{y:.3f}" width="{w:.3f}" height="{h:.3f}" class="{cls}" {extra}/>')

def circ(cx, cy, d, cls="voll"):
    add(f'<circle cx="{cx:.3f}" cy="{cy:.3f}" r="{d/2:.3f}" class="{cls}"/>')

def path(d, cls="voll", extra=""):
    add(f'<path d="{d}" class="{cls}" {extra}/>')

def text(x, y, s, size=3.0, anchor="start", cls="txt", rot=None, weight=None):
    tr = f' transform="rotate({rot} {x:.3f} {y:.3f})"' if rot is not None else ""
    fw = f' font-weight="{weight}"' if weight else ""
    add(f'<text x="{x:.3f}" y="{y:.3f}" font-size="{size}" text-anchor="{anchor}" '
        f'class="{cls}"{fw}{tr}>{s}</text>')

def arrow(x, y, ang, l=2.4):
    """Pfeilspitze an (x,y), zeigt in Richtung ang (Grad)."""
    a = math.radians(ang)
    dx, dy = math.cos(a)*l, math.sin(a)*l
    px, py = -dy*0.35, dx*0.35
    add(f'<path d="M {x:.3f} {y:.3f} L {x-dx+px:.3f} {y-dy+py:.3f} '
        f'L {x-dx-px:.3f} {y-dy-py:.3f} Z" class="pfeil"/>')

def dim_h(x1, x2, y, label, size=2.8):
    line(x1, y, x2, y, "masz")
    arrow(x1, y, 180); arrow(x2, y, 0)
    if label:
        text((x1+x2)/2, y-1.3, label, size, "middle")

def dim_v(y1, y2, x, label, size=2.8):
    line(x, y1, x, y2, "masz")
    arrow(x, y1, 270); arrow(x, y2, 90)
    if label:
        text(x-1.3, (y1+y2)/2, label, size, "middle", rot=-90)

def hilf(x1, y1, x2, y2):
    line(x1, y1, x2, y2, "hilf")

def dim_dia(cx, cy, d, ang, label, ext=9.0, size=2.9):
    """Durchmesserbemassung in der Ansicht: Masslinie durch den Mittelpunkt."""
    a = math.radians(ang)
    ux, uy = math.cos(a), -math.sin(a)
    x1, y1 = cx - ux*d/2, cy - uy*d/2
    x2, y2 = cx + ux*d/2, cy + uy*d/2
    xe, ye = cx + ux*(d/2 + ext), cy + uy*(d/2 + ext)
    line(x1, y1, xe, ye, "masz")
    arrow(x1, y1, math.degrees(math.atan2(-uy, -ux)) % 360)
    arrow(x2, y2, math.degrees(math.atan2(uy, ux)) % 360)
    anchor = "start" if ux >= 0 else "end"
    off = 1.6 if ux >= 0 else -1.6
    text(xe + off, ye + (1.0 if uy >= 0 else -0.6), label, size, anchor)

# ---------------------------------------------------------------- Schnitt A-A
def schnitt(ox, oy, g):
    """Vollschnitt durch die Rotationsachse. x = axial, y = radial."""
    X = lambda a: ox + a
    Y = lambda r: oy - r
    B, D, S, Di = g.B, g.D, g.S, g.Di
    rN, lN, t = g.dN/2, g.lN, g.t
    rB, rKi, rKa = g.dB/2, Di/2, D/2
    lk = lN + 2*g.lKM

    pts = [(-lN/2, rB), (-lN/2, rN), (-t/2, rN), (-t/2, rKi),
           (-B/2, rKi), (-B/2, rKa), (B/2, rKa), (B/2, rKi),
           (t/2, rKi), (t/2, rN), (lN/2, rN), (lN/2, rB)]

    def poly(mirror):
        d = ""
        for i, (a, rr) in enumerate(pts):
            yy = (oy + rr) if mirror else Y(rr)
            d += ("M " if i == 0 else "L ") + f"{X(a):.3f} {yy:.3f} "
        return d + "Z"
    path(poly(False), "voll", 'fill="url(#hatch)"')
    path(poly(True),  "voll", 'fill="url(#hatch)"')

    # Kern (nicht geschnitten dargestellt, farbig abgesetzt)
    rect(X(-lk/2), Y(rB), lk, 2*rB, "kern")
    line(X(-lN/2), Y(rB), X(-lN/2), oy + rB, "kern_d")
    line(X( lN/2), Y(rB), X( lN/2), oy + rB, "kern_d")
    text(X(0), oy + rB - 2.2, "Kern", 2.7, "middle", cls="txt_kern")
    text(X(-(lN/2 + g.lKM/2)), oy + rB + 4.6, "Kernmarke", 2.3, "middle", cls="txt_kern")
    text(X( (lN/2 + g.lKM/2)), oy + rB + 4.6, "Kernmarke", 2.3, "middle", cls="txt_kern")

    # Achse + Teilungsebene (Formteilung liegt in der Achsebene)
    line(X(-lk/2 - 10), oy, X(lk/2 + 10), oy, "mitte")
    line(X(-D/2 - 26), oy, X(-lk/2 - 10), oy, "teilung")
    line(X(lk/2 + 10), oy, X(D/2 + 26), oy, "teilung")
    text(X(-D/2 - 26), oy - 2.0, "Teilungsebene", 2.5, "start", cls="txt_te")

    # ---- axiale Bemassung oben
    yb = Y(rKa)
    hilf(X(-B/2), yb, X(-B/2), yb - 10);  hilf(X(B/2), yb, X(B/2), yb - 10)
    dim_h(X(-B/2), X(B/2), yb - 8, f"{B:g}")
    hilf(X(-lN/2), Y(rN), X(-lN/2), yb - 18); hilf(X(lN/2), Y(rN), X(lN/2), yb - 18)
    dim_h(X(-lN/2), X(lN/2), yb - 16, f"{lN:g}")
    hilf(X(-lk/2), Y(rB), X(-lk/2), yb - 26); hilf(X(lk/2), Y(rB), X(lk/2), yb - 26)
    dim_h(X(-lk/2), X(lk/2), yb - 24, f"Kern L = {lk:g}")

    # ---- Steg
    ys = Y((rKi + rN)/2)
    dim_h(X(-t/2), X(t/2), ys, "")
    text(X(t/2 + 4), ys + 1.0, f"Steg {str(t).replace('.', ',')}", 2.8, "start")

    # ---- Kranzdicke links
    xk = X(-B/2 - 7)
    hilf(X(-B/2), Y(rKa), xk - 2, Y(rKa)); hilf(X(-B/2), Y(rKi), xk - 2, Y(rKi))
    dim_v(Y(rKa), Y(rKi), xk, "")
    text(xk - 2.0, (Y(rKa) + Y(rKi))/2 + 1.0, f"{S:g}", 2.8, "end")
    text(xk - 2.0, (Y(rKa) + Y(rKi))/2 + 4.6, "Kranz", 2.4, "end", cls="txt_sub")

# ---------------------------------------------------------------- Ansicht
def ansicht(ox, oy, g):
    circ(ox, oy, g.D, "voll")
    circ(ox, oy, g.Di, "verdeckt")
    circ(ox, oy, g.dN, "voll")
    circ(ox, oy, g.dB, "voll")
    R = g.D/2 + 8
    line(ox - R, oy, ox + R, oy, "mitte")
    line(ox, oy - R, ox, oy + R, "mitte")

    dim_dia(ox, oy, g.D,  128, f"&#216;{g.D:g}")
    dim_dia(ox, oy, g.dN,  52, f"&#216;{g.dN:g}", ext=26)
    dim_dia(ox, oy, g.dB, -52, f"&#216;{g.dB:g} (Kern)", ext=32)
    dim_dia(ox, oy, g.Di, 205, f"&#216;{g.Di:g}", ext=14)

    # Schnittverlauf A-A
    line(ox - R - 5, oy, ox + R + 5, oy, "schnittlinie")
    for sx in (-1, 1):
        x = ox + sx*(R + 5)
        arrow(x, oy, 0 if sx < 0 else 180, 4.0)
        text(x + sx*4.5, oy - 3.8, "A", 4.2, "middle", weight="bold")
    text(ox, oy + g.D/2 + 16, "Ansicht (Blick in Achsrichtung)", 2.8, "middle", cls="txt_sub")

# ---------------------------------------------------------------- Blatt
add('<?xml version="1.0" encoding="UTF-8"?>')
add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">')
add("""<defs>
<pattern id="hatch" width="2.6" height="2.6" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
  <line x1="0" y1="0" x2="0" y2="2.6" stroke="#2b5c96" stroke-width="0.22"/>
</pattern>
<style>
  text { font-family: "DejaVu Sans", Arial, Helvetica, sans-serif; fill:#14243a; }
  .voll   { stroke:#14243a; stroke-width:0.5; fill:none; }
  .verdeckt { stroke:#14243a; stroke-width:0.3; fill:none; stroke-dasharray:2.5 1.5; }
  .mitte  { stroke:#b03030; stroke-width:0.25; fill:none; stroke-dasharray:8 1.5 1.2 1.5; }
  .teilung{ stroke:#0a7a5a; stroke-width:0.5; fill:none; stroke-dasharray:5 1.8 1 1.8; }
  .schnittlinie { stroke:#b03030; stroke-width:0.7; fill:none; stroke-dasharray:10 2 3 2; }
  .masz   { stroke:#14243a; stroke-width:0.25; fill:none; }
  .hilf   { stroke:#14243a; stroke-width:0.18; fill:none; }
  .pfeil  { fill:#14243a; stroke:none; }
  .kern   { stroke:#8a6d1a; stroke-width:0.4; fill:#f6e6b0; }
  .kern_d { stroke:#8a6d1a; stroke-width:0.3; fill:none; stroke-dasharray:2 1.5; }
  .txt_kern { fill:#7a5f10; }
  .txt_te { fill:#0a7a5a; }
  .txt_sub { fill:#4a5b70; }
  .rahmen { stroke:#14243a; stroke-width:0.7; fill:none; }
  .box    { stroke:#8fa2bb; stroke-width:0.35; fill:#f7f9fc; }
</style></defs>""")
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')
rect(10, 10, W-20, H-20, "rahmen")

text(16, 20, "Miniatur-Riemenscheibe &#8212; Prinzipskizze / Vorentwurf", 6.4, "start", weight="bold")
text(16, 26, "Bachelorprojekt Metallguss &#183; Laborversuch Handformen mit Kern &#183; Gie&#223;werkstoff Zinn (Sn)",
     3.1, cls="txt_sub")
line(16, 29, 276, 29, "masz")

# Zeile 1: Version O
text(16, 41, VO.name, 4.6, "start", weight="bold")
ansicht(72, 100, VO)
schnitt(200, 100, VO)
text(200, 148, "Schnitt A&#8211;A  (Vollschnitt durch die Achse)", 2.8, "middle", cls="txt_sub")

# Zeile 2: Version F
text(16, 167, VF.name, 4.6, "start", weight="bold")
ansicht(72, 226, VF)
schnitt(200, 226, VF)
text(200, 274, "Schnitt A&#8211;A", 2.8, "middle", cls="txt_sub")

# ---- Kasten 1: Unterschiede
dx, dy, dw, dh = 288, 36, 118, 104
rect(dx, dy, dw, dh, "box")
text(dx+4, dy+7, "Unterschied V-O &#8594; V-F", 3.5, "start", weight="bold")
text(dx+4, dy+12, "gleiche Au&#223;enkontur, gleicher Kern", 2.6, cls="txt_sub")
rows = [("Merkmal", "V-O", "V-F", True),
        ("Steg", "5 mm", "2,5 mm", False),
        ("Kehlen", "R3", "R0 (scharf)", False),
        ("Nabe", "&#216;28", "&#216;36", False),
        ("Anschnitt", "seitl. Kranz", "oben a. Steg", False),
        ("Speiser", "&#252;ber Nabe", "keiner", False),
        ("Entl&#252;ftung", "Windpfeife", "keine", False),
        ("Gie&#223;temperatur", "ca. 280 &#176;C", "ca. 240 &#176;C", False)]
yy = dy + 20
for a, b, c, fett in rows:
    w = "bold" if fett else None
    text(dx+4, yy, a, 2.7, "start", weight=w)
    text(dx+46, yy, b, 2.7, "start", weight=w)
    text(dx+80, yy, c, 2.7, "start", weight=w)
    yy += 5.0
line(dx+3, dy+21.5, dx+dw-3, dy+21.5, "masz")
text(dx+4, dy+68, "Erwartete Fehlerbilder an V-F", 3.0, "start", weight="bold")
for i, s in enumerate(["Sauglunker in der Nabe (keine Speisung)",
                       "Kaltlauf im 2,5-mm-Steg",
                       "Warmriss an den scharfen Kehlen",
                       "Gasblasen / Erosion durch oben liegenden",
                       "Anschnitt und fehlende Entl&#252;ftung"]):
    text(dx+4, dy+74 + i*4.6, ("&#8226; " + s) if i < 4 else "&#160;&#160;&#160;" + s, 2.65)

# ---- Kasten 2: Hinweise
bx, by, bw, bh = 288, 148, 118, 108
rect(bx, by, bw, bh, "box")
text(bx+4, by+7, "Hinweise / offene Punkte", 3.5, "start", weight="bold")
zeilen = [("Was diese Zeichnung ist", 1),
          ("Prinzipskizze aus den Konzeptma&#223;en des Bau-", 0),
          ("teilkonzepts (F14). Keine fertigungsreife", 0),
          ("Zeichnung nach DIN EN 12890 [Q18].", 0),
          ("", 0),
          ("Noch NICHT enthalten", 1),
          ("&#8226; Schwindma&#223; (Ergebnis V-S1 offen)", 0),
          ("&#8226; Formschr&#228;gen 1&#8211;3&#176; in Ausheberichtung", 0),
          ("&#8226; Kernmarkenspiel / Passung Kernlager", 0),
          ("&#8226; Radien an allen Kanten (nur R3 notiert)", 0),
          ("&#8226; Anschnitt, Speiser, Windpfeife", 0),
          ("&#8226; Toleranzen, Rauheit, Normschriftfeld", 0),
          ("", 0),
          ("Zu kl&#228;ren (Widerspruch im Konzept)", 1),
          ("Kernl&#228;nge dort &#8222;ca. 50 mm&#8220;; aus Nabe 24 +", 0),
          ("2 &#215; 12 mm Kernmarke folgen 48 mm.", 0),
          ("Nabe (24) ist axial breiter als der Kranz (20)", 0),
          ("&#8594; Nabe steht je Seite 2 mm vor. Gewollt?", 0)]
yy = by + 13.5
for s, fett in zeilen:
    if s:
        text(bx+4, yy, s, 2.65, "start", weight=("bold" if fett else None))
        yy += 4.3
    else:
        yy += 2.2

# ---- Schriftfeld
sx, sy, sw, sh = 240, 262, 166, 25
rect(sx, sy, sw, sh, "rahmen")
line(sx, sy+9, sx+sw, sy+9, "voll")
line(sx+98, sy, sx+98, sy+sh, "voll")
text(sx+3, sy+6.2, "Miniatur-Riemenscheibe, Version O / F", 3.5, "start", weight="bold")
text(sx+101, sy+6.2, "Ma&#223;stab 1:1 &#183; Ma&#223;e in mm", 3.1, weight="bold")
text(sx+3, sy+15, "Bachelorprojekt Metallguss &#183; HAW Hamburg", 2.7)
text(sx+3, sy+20.5, "Gebert / Barmwater / Wettering &#183; 10.08.2026", 2.7)
text(sx+101, sy+15, "Status: Konzeptvorschlag, nicht freigegeben", 2.7)
text(sx+101, sy+20.5, "Quelle der Ma&#223;e: Bauteilkonzept.md", 2.7)

add("</svg>")
open("../../90_Assets/Bilder/Bauteil-Riemenscheibe_Skizze.svg", "w",
     encoding="utf-8").write("\n".join(out))
print("ok")
