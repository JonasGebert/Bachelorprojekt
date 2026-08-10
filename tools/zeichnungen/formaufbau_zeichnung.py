# -*- coding: utf-8 -*-
"""
Formaufbau-Zeichnung (A3 quer, SVG, 1:1):
Gussteil im geschlossenen Formkasten mit Kern, Gießsystem, Speiser und Kühleisen.
Zwei zueinander senkrechte Schnitte. Alle Maße in mm.
"""
import math

W, H = 420.0, 297.0

# ---- Bauteil (Version O, aus Bauteilkonzept.md)
D, B, S = 70.0, 20.0, 8.0          # Kranz: Aussen-Ø, Breite, Dicke
Di = D - 2*S                        # 54
dN, lN = 28.0, 24.0                 # Nabe
tS = 5.0                            # Steg
dB, lKM = 14.0, 12.0                # Bohrung / Kernmarke
lK = lN + 2*lKM                     # 48 Kernlaenge
rB, rN, rKi, rKa = dB/2, dN/2, Di/2, D/2

# ---- Formkasten (F19, gemessen 10.08.2026)
KL, KB, KHh = 190.0, 90.0, 80.0     # Laenge, Breite, Hoehe je Haelfte
WD = 8.0                            # Wandstaerke (Darstellung)

# ---- Giesssystem (Vorschlag)
dSpeiser, dEinguss, dAnschnitt, dWind = 14.0, 10.0, 5.0, 4.0
dKuehl_a, tKuehl = 40.0, 8.0        # Kuehleisen-Ring aussen-Ø, Dicke

out = []
def add(s): out.append(s)
def line(x1,y1,x2,y2,cls="voll"):
    add(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" class="{cls}"/>')
def rect(x,y,w,h,cls="voll",extra=""):
    add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" class="{cls}" {extra}/>')
def circ(cx,cy,d,cls="voll",extra=""):
    add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{d/2:.2f}" class="{cls}" {extra}/>')
def path(d,cls="voll",extra=""):
    add(f'<path d="{d}" class="{cls}" {extra}/>')
def text(x,y,s,size=3.0,anchor="start",cls="txt",weight=None,rot=None):
    fw = f' font-weight="{weight}"' if weight else ""
    tr = f' transform="rotate({rot} {x:.2f} {y:.2f})"' if rot is not None else ""
    add(f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" text-anchor="{anchor}" class="{cls}"{fw}{tr}>{s}</text>')
def arrow(x,y,ang,l=2.4):
    a=math.radians(ang); dx,dy=math.cos(a)*l,math.sin(a)*l; px,py=-dy*0.35,dx*0.35
    add(f'<path d="M {x:.2f} {y:.2f} L {x-dx+px:.2f} {y-dy+py:.2f} L {x-dx-px:.2f} {y-dy-py:.2f} Z" class="pfeil"/>')
def dim_h(x1,x2,y,label,size=2.6):
    line(x1,y,x2,y,"masz"); arrow(x1,y,180); arrow(x2,y,0)
    if label: text((x1+x2)/2,y-1.2,label,size,"middle")
def dim_v(y1,y2,x,label,size=2.6):
    line(x,y1,x,y2,"masz"); arrow(x,y1,270); arrow(x,y2,90)
    if label: text(x-1.6,(y1+y2)/2+1.0,label,size,"end")

# ---- Positionsnummern
def pos(x, y, n, lx, ly):
    """Kreis mit Nummer bei (x,y), Hinweislinie zum Punkt (lx,ly)."""
    line(x, y, lx, ly, "hinweis")
    add(f'<circle cx="{lx:.2f}" cy="{ly:.2f}" r="0.7" class="pfeil2"/>')
    add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="3.1" fill="#ffffff" stroke="#14243a" stroke-width="0.4"/>')
    text(x, y+1.05, str(n), 3.2, "middle", weight="bold")

# =================================================================== Blatt
add('<?xml version="1.0" encoding="UTF-8"?>')
add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">')
add("""<defs>
<pattern id="metall" width="2.4" height="2.4" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
  <rect width="2.4" height="2.4" fill="#dce6f2"/>
  <line x1="0" y1="0" x2="0" y2="2.4" stroke="#2b5c96" stroke-width="0.28"/>
</pattern>
<pattern id="sand" width="3.2" height="3.2" patternUnits="userSpaceOnUse">
  <rect width="3.2" height="3.2" fill="#f3ece1"/>
  <circle cx="0.8" cy="0.8" r="0.24" fill="#c2ab8c"/>
  <circle cx="2.4" cy="2.2" r="0.24" fill="#c2ab8c"/>
</pattern>
<pattern id="kern" width="2.6" height="2.6" patternUnits="userSpaceOnUse">
  <rect width="2.6" height="2.6" fill="#f6e2a8"/>
  <circle cx="0.7" cy="0.7" r="0.26" fill="#c9a63c"/>
  <circle cx="2.0" cy="1.9" r="0.26" fill="#c9a63c"/>
</pattern>
<pattern id="kuehl" width="2.0" height="2.0" patternTransform="rotate(-45)" patternUnits="userSpaceOnUse">
  <rect width="2.0" height="2.0" fill="#c3c8ce"/>
  <line x1="0" y1="0" x2="0" y2="2" stroke="#5b6570" stroke-width="0.4"/>
</pattern>
<style>
  text { font-family:"DejaVu Sans",Arial,sans-serif; fill:#14243a; }
  .voll{stroke:#14243a;stroke-width:0.5;fill:none;}
  .duenn{stroke:#14243a;stroke-width:0.28;fill:none;}
  .verdeckt{stroke:#14243a;stroke-width:0.3;fill:none;stroke-dasharray:2.5 1.5;}
  .kasten{stroke:#14243a;stroke-width:0.8;fill:none;}
  .mitte{stroke:#b03030;stroke-width:0.28;fill:none;stroke-dasharray:8 1.5 1.2 1.5;}
  .teilung{stroke:#0a7a5a;stroke-width:0.8;fill:none;}
  .masz{stroke:#14243a;stroke-width:0.25;fill:none;}
  .hilf{stroke:#14243a;stroke-width:0.18;fill:none;}
  .hinweis{stroke:#14243a;stroke-width:0.25;fill:none;}
  .pfeil{fill:#14243a;stroke:none;}
  .pfeil2{fill:#14243a;stroke:none;}
  .rahmen{stroke:#14243a;stroke-width:0.7;fill:none;}
  .box{stroke:#8fa2bb;stroke-width:0.35;fill:#f7f9fc;}
  .warn{fill:#b03030;}
  .sub{fill:#4a5b70;}
  .fluss{stroke:#b03030;stroke-width:0.9;fill:none;}
</style></defs>""")
add(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
rect(10,10,W-20,H-20,"rahmen")

text(16,20,"Formaufbau &#8212; Gussteil im geschlossenen Formkasten (Version O)",6.2,weight="bold")
text(16,26,"Bachelorprojekt Metallguss &#183; Handformen mit liegendem Kern &#183; Zinn &#183; Ma&#223;stab 1:1, Ma&#223;e in mm",3.1,cls="sub")
text(404,20,"VORSCHLAG &#8212; nicht freigegeben",3.4,"end",cls="warn",weight="bold")
text(404,25.5,"Gie&#223;system weicht bewusst vom Bauteilkonzept ab, siehe Kasten unten rechts",2.6,"end",cls="sub")
line(16,29.5,404,29.5,"masz")

# =================================================================== Ansicht 1
cx1, cy1 = 76.0, 142.0     # Achse: x = axial (z), y = radial
X1 = lambda z: cx1 + z
Y1 = lambda r: cy1 - r

# Formkasten
rect(X1(-KB/2)-WD, Y1(KHh)-WD, KB+2*WD, KHh+WD, "kasten", 'fill="#eef1f5"')       # Oberkasten
rect(X1(-KB/2)-WD, Y1(0),      KB+2*WD, KHh+WD, "kasten", 'fill="#eef1f5"')       # Unterkasten
rect(X1(-KB/2), Y1(KHh), KB, KHh, "duenn", 'fill="url(#sand)"')
rect(X1(-KB/2), Y1(0),   KB, KHh, "duenn", 'fill="url(#sand)"')

# Gussteil (Schnitt, beide Haelften)
pts = [(-lN/2,rB),(-lN/2,rN),(-tS/2,rN),(-tS/2,rKi),(-B/2,rKi),(-B/2,rKa),
       (B/2,rKa),(B/2,rKi),(tS/2,rKi),(tS/2,rN),(lN/2,rN),(lN/2,rB)]
for mirror in (False,True):
    d = ""
    for i,(z,r) in enumerate(pts):
        yy = (cy1+r) if mirror else Y1(r)
        d += ("M " if i==0 else "L ") + f"{X1(z):.2f} {yy:.2f} "
    path(d+"Z","voll",'fill="url(#metall)"')

# Speiser auf dem Kranz (oben), bis zur Sandoberflaeche
rect(X1(-dSpeiser/2), Y1(KHh), dSpeiser, KHh-rKa, "voll", 'fill="url(#metall)"')
# Kuehleisen (Ringe an den Nabenstirnflaechen)
for sgn in (-1,1):
    z0 = sgn*lN/2 if sgn>0 else sgn*lN/2 - tKuehl
    for r0,r1 in ((rB,dKuehl_a/2),):
        rect(X1(z0 if sgn>0 else z0), Y1(r1), tKuehl, r1-r0, "duenn", 'fill="url(#kuehl)"')
        rect(X1(z0 if sgn>0 else z0), cy1+r0, tKuehl, r1-r0, "duenn", 'fill="url(#kuehl)"')
# Kern
rect(X1(-lK/2), Y1(rB), lK, 2*rB, "voll", 'fill="url(#kern)"')
line(X1(-lN/2), Y1(rB), X1(-lN/2), cy1+rB, "verdeckt")
line(X1( lN/2), Y1(rB), X1( lN/2), cy1+rB, "verdeckt")

# Teilungsebene + Achse
line(X1(-KB/2)-WD-6, cy1, X1(KB/2)+WD+6, cy1, "teilung")
text(X1(-KB/2)-WD-6, cy1-2.2, "Teilungsebene = Achsebene", 2.6, cls="sub")

# Fuehrungsstifte
for sgn in (-1,1):
    xs = X1(sgn*(KB/2+WD/2))
    rect(xs-1.4, cy1-9, 2.8, 18, "duenn", 'fill="#9aa7b6"')

# Bemassung Sandumhuellung
dim_h(X1(-KB/2), X1(-lK/2), Y1(rKa)+8, "21")
dim_h(X1(lK/2), X1(KB/2), Y1(rKa)+8, "21")
dim_v(Y1(KHh), Y1(rKa), X1(-B/2)-16, "45")
dim_v(cy1+rKa, cy1+KHh, X1(-B/2)-16, "45")
dim_h(X1(-KB/2), X1(KB/2), Y1(KHh)+9, "Kasten-Innenbreite 90")
text(cx1, Y1(KHh)+16, "Gie&#223;system siehe Schnitt B&#8211;B", 2.6, "middle", cls="sub")

text(cx1, Y1(KHh)-14, "Schnitt A&#8211;A  &#183;  durch die Achse", 3.6, "middle", weight="bold")
text(cx1, Y1(KHh)-10, "zeigt Kernlagerung, Speiser, K&#252;hleisen", 2.7, "middle", cls="sub")

pos(X1(-38), Y1(58), 1, X1(-30), Y1(48))
pos(X1(-38), cy1+58, 2, X1(-30), cy1+48)
pos(X1(-KB/2)-WD-11, cy1+7, 3, X1(-KB/2)-4, cy1)
pos(X1(30), Y1(52), 4, X1(6), Y1(rKa))
pos(X1(0), cy1+22, 5, X1(0), cy1+rB-1)
pos(X1(-32), cy1+20, 6, X1(-18), cy1+rB-1)
pos(X1(24), Y1(66), 11, X1(dSpeiser/2-2), Y1(60))
pos(X1(30), cy1+34, 13, X1(lN/2+tKuehl/2), cy1+14)
pos(X1(KB/2)+WD+9, Y1(24), 14, X1(KB/2+WD/2), Y1(8))

# =================================================================== Ansicht 2
cx2, cy2 = 258.0, 142.0    # u = Kastenlaenge, r = radial
X2 = lambda u: cx2 + u
Y2 = lambda r: cy2 - r

rect(X2(-KL/2)-WD, Y2(KHh)-WD, KL+2*WD, KHh+WD, "kasten", 'fill="#eef1f5"')
rect(X2(-KL/2)-WD, Y2(0),      KL+2*WD, KHh+WD, "kasten", 'fill="#eef1f5"')
rect(X2(-KL/2), Y2(KHh), KL, KHh, "duenn", 'fill="url(#sand)"')
rect(X2(-KL/2), Y2(0),   KL, KHh, "duenn", 'fill="url(#sand)"')

# Gussteil im Schnitt: Ringflaeche Ø14 ... Ø70
path(f"M {X2(-rKa):.2f} {cy2:.2f} a {rKa} {rKa} 0 1 0 {2*rKa} 0 a {rKa} {rKa} 0 1 0 {-2*rKa} 0 "
     f"M {X2(-rB):.2f} {cy2:.2f} a {rB} {rB} 0 1 0 {2*rB} 0 a {rB} {rB} 0 1 0 {-2*rB} 0 Z",
     "voll", 'fill="url(#metall)" fill-rule="evenodd"')
circ(cx2, cy2, Di, "duenn"); circ(cx2, cy2, dN, "duenn")
circ(cx2, cy2, dB, "voll", 'fill="url(#kern)"')

# Einguss + Trichter
uE = -70.0
rect(X2(uE-dEinguss/2), Y2(KHh), dEinguss, KHh, "voll", 'fill="url(#metall)"')
path(f"M {X2(uE-9):.2f} {Y2(KHh):.2f} L {X2(uE-dEinguss/2):.2f} {Y2(KHh-9):.2f} "
     f"L {X2(uE+dEinguss/2):.2f} {Y2(KHh-9):.2f} L {X2(uE+9):.2f} {Y2(KHh):.2f} Z",
     "voll", 'fill="url(#metall)"')
# Querlauf in der Teilungsebene + Anschnitt
rect(X2(uE), cy2-4.0, 25.0, 8.0, "voll", 'fill="url(#metall)"')
rect(X2(-45), cy2-dAnschnitt/2, 10.0, dAnschnitt, "voll", 'fill="url(#metall)"')
# Speiser oben auf dem Kranz
rect(X2(-dSpeiser/2), Y2(KHh), dSpeiser, KHh-rKa, "voll", 'fill="url(#metall)"')
# Windpfeife
uw = 25.0; rw = math.sqrt(rKa**2 - uw**2)
rect(X2(uw-dWind/2), Y2(KHh), dWind, KHh-rw, "voll", 'fill="url(#metall)"')

line(X2(-KL/2)-WD-6, cy2, X2(KL/2)+WD+6, cy2, "teilung")
line(cx2, Y2(KHh)-4, cx2, cy2+KHh+4, "mitte")

# Giessrichtung
line(X2(uE), Y2(KHh)-13, X2(uE), Y2(KHh)-3, "fluss")
arrow(X2(uE), Y2(KHh)-3, 90, 3.2)
text(X2(uE)+4, Y2(KHh)-9, "Gie&#223;richtung", 2.6, cls="warn")

# Bemassung
dim_h(X2(-KL/2), X2(-rKa), cy2+55, "60")
dim_h(X2(rKa), X2(KL/2), cy2+55, "60")
dim_v(Y2(KHh), Y2(rKa), X2(-58), "45")
dim_v(cy2+rKa, cy2+KHh, X2(-58), "45")
dim_h(X2(-KL/2), X2(KL/2), cy2+KHh-6, "Kasten-Innenl&#228;nge 190")

text(cx2, Y2(KHh)-14, "Schnitt B&#8211;B  &#183;  senkrecht zur Achse", 3.6, "middle", weight="bold")
text(cx2, Y2(KHh)-10, "zeigt das Gie&#223;system in der Teilungsebene", 2.7, "middle", cls="sub")

pos(X2(uE-22), Y2(KHh-6), 7, X2(uE-6), Y2(KHh-4))
pos(X2(uE-22), Y2(46), 8, X2(uE-dEinguss/2), Y2(40))
pos(X2(uE+8), cy2+15, 9, X2(uE+14), cy2+3)
pos(X2(-42), cy2+16, 10, X2(-40+cx2-cx2), cy2+2) if False else pos(X2(-46), cy2+16, 10, X2(-40), cy2+2)
pos(X2(-16), Y2(56), 11, X2(-dSpeiser/2), Y2(50))
pos(X2(36), Y2(52), 12, X2(uw+dWind/2), Y2(46))
pos(X2(0), cy2+18, 5, X2(0), cy2+rB-1)
pos(X2(46), cy2+30, 4, X2(30), cy2+18)

# =================================================================== Legende
ly = 236.0
rect(22, ly, 388, 51, "box")
text(26, ly+6.5, "Legende", 3.5, weight="bold")
eintraege = [
 (1,"Oberkasten, verdichteter Formsand"),
 (2,"Unterkasten, verdichteter Formsand"),
 (3,"Teilungsebene = Achsebene (gr&#252;n)"),
 (4,"Formhohlraum = Gussteil, Kranz &#216;70 / Steg 5 / Nabe &#216;28"),
 (5,"Sandkern &#216;14, liegend &#8212; steht nicht!"),
 (6,"Kernmarke &#216;14 &#215; 12, dahinter 21 mm Sand"),
 (7,"Gie&#223;trichter"),
 (8,"Einguss &#216;10, senkrecht"),
 (9,"Querlauf in der Teilungsebene (Unterkasten)"),
 (10,"Anschnitt &#216;5, seitlich in den Kranz"),
 (11,"Speiser &#216;14 oben auf dem Kranz (h&#246;chster Punkt)"),
 (12,"Windpfeife &#216;4, versetzt zum Anschnitt"),
 (13,"K&#252;hleisen: Alu-Ring &#216;40/&#216;14 &#215; 8, je Nabenstirnseite (Vorschlag)"),
 (14,"F&#252;hrungsstifte des Formkastens"),
]
spalten = [(26, 0, 5), (140, 5, 10), (254, 10, 14)]
for x0, a, b in spalten:
    yy = ly + 13
    for n, s in eintraege[a:b]:
        add(f'<circle cx="{x0+2.6:.2f}" cy="{yy-1.0:.2f}" r="2.6" fill="#ffffff" stroke="#14243a" stroke-width="0.35"/>')
        text(x0+2.6, yy+0.05, str(n), 2.7, "middle", weight="bold")
        text(x0+7.5, yy, s, 2.7)
        yy += 7.0

# Begruendungskasten
rect(360, ly+9, 46, 40, "box")
text(362, ly+14, "Warum kein Speiser", 2.7, weight="bold")
text(362, ly+18, "&#252;ber der Nabe?", 2.7, weight="bold")
zeilen = ["Der Kranz steht dar&#252;ber im Weg;",
          "es bliebe nur &#216;6 &#8594; M = 1,5 mm.",
          "N&#246;tig: M &#8805; 1,2 &#183; 2,7 = 3,2 mm.",
          "Deshalb Speiser &#216;14 auf den",
          "Kranz (M = 3,5 mm), Nabe mit",
          "K&#252;hleisen zuerst erstarren lassen.",
          "Moduln: Nabe 2,7 &#183; Kranz 2,6 &#183;",
          "Steg 2,5 mm."]
for i, s in enumerate(zeilen):
    text(362, ly+22.5 + i*3.4, s, 2.35)

add("</svg>")
open("../../90_Assets/Bilder/Formaufbau_Schnitt.svg","w",encoding="utf-8").write("\n".join(out))
print("ok")
