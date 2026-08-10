# -*- coding: utf-8 -*-
"""Stehbuchse mit Fussplatte — Bauteil, Formaufbau, Aushebbarkeitsnachweis. A3 quer."""
import math

W, H = 420.0, 297.0
PL, PB, PT = 110.0, 36.0, 7.0     # Fussplatte L x B x Dicke
DA, DI, NH = 34.0, 18.0, 47.0     # Nabe aussen / Bohrung / Oberkante ueber Teilung
RT, RL, RH = 5.0, 25.0, 25.0      # Rippe Dicke / Fusslaenge / Hoehe
KMU = 15.0                        # untere Kernmarke unter der Teilung
SPA = 38.0                        # Ringspeiser aussen
KL, KB, KHh = 190.0, 90.0, 80.0
dEin, dAns, dWi = 12.0, 6.0, 4.0

out=[]
def add(s): out.append(s)
def line(x1,y1,x2,y2,c="voll"): add(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" class="{c}"/>')
def rect(x,y,w,h,c="voll",e=""):
    if w<=0 or h<=0: return
    add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" class="{c}" {e}/>')
def circ(cx,cy,d,c="voll",e=""): add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{d/2:.2f}" class="{c}" {e}/>')
def poly(pts,c="voll",e=""):
    d="".join(("M " if i==0 else "L ")+f"{x:.2f} {y:.2f} " for i,(x,y) in enumerate(pts))
    add(f'<path d="{d}Z" class="{c}" {e}/>')
def text(x,y,s,sz=3.0,an="start",c="txt",w=None):
    fw=f' font-weight="{w}"' if w else ""
    add(f'<text x="{x:.2f}" y="{y:.2f}" font-size="{sz}" text-anchor="{an}" class="{c}"{fw}>{s}</text>')
def arrow(x,y,ang,l=2.2):
    a=math.radians(ang); dx,dy=math.cos(a)*l,math.sin(a)*l; px,py=-dy*0.35,dx*0.35
    add(f'<path d="M {x:.2f} {y:.2f} L {x-dx+px:.2f} {y-dy+py:.2f} L {x-dx-px:.2f} {y-dy-py:.2f} Z" class="pfeil"/>')
def dimh(x1,x2,y,lab,sz=2.6):
    line(x1,y,x2,y,"masz"); arrow(x1,y,180); arrow(x2,y,0)
    if lab: text((x1+x2)/2,y-1.2,lab,sz,"middle")
def dimv(y1,y2,x,lab,sz=2.6,side="left"):
    line(x,y1,x,y2,"masz"); arrow(x,y1,270); arrow(x,y2,90)
    if lab:
        if side=="left": text(x-1.6,(y1+y2)/2+1.0,lab,sz,"end")
        else: text(x+1.6,(y1+y2)/2+1.0,lab,sz,"start")

add('<?xml version="1.0" encoding="UTF-8"?>')
add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">')
add("""<defs>
<pattern id="metall" width="2.4" height="2.4" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
 <rect width="2.4" height="2.4" fill="#dce6f2"/><line x1="0" y1="0" x2="0" y2="2.4" stroke="#2b5c96" stroke-width="0.28"/></pattern>
<pattern id="sand" width="3.0" height="3.0" patternUnits="userSpaceOnUse">
 <rect width="3.0" height="3.0" fill="#f3ece1"/><circle cx="0.7" cy="0.7" r="0.22" fill="#c2ab8c"/><circle cx="2.2" cy="2.1" r="0.22" fill="#c2ab8c"/></pattern>
<pattern id="kern" width="2.4" height="2.4" patternUnits="userSpaceOnUse">
 <rect width="2.4" height="2.4" fill="#f6e2a8"/><circle cx="0.6" cy="0.6" r="0.24" fill="#c9a63c"/><circle cx="1.8" cy="1.8" r="0.24" fill="#c9a63c"/></pattern>
<style>
 text{font-family:"DejaVu Sans",Arial,sans-serif;fill:#14243a;}
 .voll{stroke:#14243a;stroke-width:0.5;fill:none;}
 .duenn{stroke:#14243a;stroke-width:0.28;fill:none;}
 .verdeckt{stroke:#14243a;stroke-width:0.3;fill:none;stroke-dasharray:2.5 1.5;}
 .kasten{stroke:#14243a;stroke-width:0.7;fill:none;}
 .mitte{stroke:#b03030;stroke-width:0.25;fill:none;stroke-dasharray:7 1.4 1.1 1.4;}
 .teilung{stroke:#0a7a5a;stroke-width:0.8;fill:none;}
 .masz{stroke:#14243a;stroke-width:0.25;fill:none;}
 .hilf{stroke:#14243a;stroke-width:0.18;fill:none;}
 .pfeil{fill:#14243a;stroke:none;}
 .rahmen{stroke:#14243a;stroke-width:0.7;fill:none;}
 .box{stroke:#8fa2bb;stroke-width:0.35;fill:#f7f9fc;}
 .kurveok{stroke:#0a7a5a;stroke-width:1.0;fill:none;}
 .kurvebad{stroke:#b03030;stroke-width:1.0;fill:none;stroke-dasharray:3 1.6;}
 .achse{stroke:#4a5b70;stroke-width:0.4;fill:none;}
 .gruen{fill:#0a7a5a;} .warn{fill:#b03030;} .sub{fill:#4a5b70;}
</style></defs>""")
add(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
rect(10,10,W-20,H-20,"rahmen")
text(16,20,"Stehbuchse mit Fu&#223;platte &#8212; nachgewiesen aushebbar",6.2,w="bold")
text(16,26,"Senkrechte Bohrung &#183; ein stehender Kern &#183; das gesamte Bauteil liegt im Oberkasten &#183; Unterkasten bleibt eben",3.1,c="sub")
text(404,20,"VORSCHLAG zu F33",3.3,"end",c="warn",w="bold")
line(16,29.5,404,29.5,"masz")

# ================= 1) Bauteil, Schnitt durch die Bohrungsachse (1:1)
cx, b0 = 88.0, 122.0
Y = lambda h: b0 - h
text(cx,42,"Bauteil Version O &#183; Schnitt durch die Bohrungsachse &#183; 1:1",3.3,"middle",w="bold")
rect(cx-PL/2, Y(PT), PL, PT, "voll", 'fill="url(#metall)"')
for sg in (-1,1):
    x0 = cx + sg*DI/2 if sg>0 else cx - DA/2
    rect(x0, Y(NH), (DA-DI)/2, NH-PT, "voll", 'fill="url(#metall)"')
    poly([(cx+sg*DA/2, Y(PT)), (cx+sg*(DA/2+RL), Y(PT)), (cx+sg*DA/2, Y(PT+RH))],
         "voll", 'fill="url(#metall)"')
line(cx, Y(NH)+2, cx, Y(0)-3, "mitte")
dimh(cx-PL/2, cx+PL/2, Y(0)+13, f"{PL:g}")
dimh(cx-DA/2, cx+DA/2, Y(NH)-6, f"&#216;{DA:g}")
dimh(cx-DI/2, cx+DI/2, Y(NH)-13, f"&#216;{DI:g} &#8212; vom Kern")
dimv(Y(NH), Y(0), cx-PL/2-9, f"{NH:g}")
dimv(Y(PT+RH), Y(PT), cx+DA/2+RL+5, f"{RH:g}", side="right")
text(cx-PL/2-3, Y(PT/2)+1, f"{PT:g}", 2.6, "end")
text(cx+DA/2+7, Y(PT+8), f"Rippe {RT:g} mm", 2.5)
text(cx-DA/2-7, Y(PT+8), "R4", 2.5, "end")

# ================= 2) Draufsicht (1:1)
dy = 168.0
text(cx,150,"Draufsicht &#183; 1:1",3.3,"middle",w="bold")
rect(cx-PL/2, dy-PB/2, PL, PB, "voll", 'fill="url(#metall)"')
for sg in (-1,1):
    rect(cx+ (0 if sg>0 else -(DA/2+RL)), dy-RT/2, DA/2+RL, RT, "duenn", 'fill="#c8d6e6"')
circ(cx, dy, DA, "voll", 'fill="#c8d6e6"')
circ(cx, dy, DI, "voll", 'fill="url(#kern)"')
line(cx-PL/2-5, dy, cx+PL/2+5, dy, "mitte"); line(cx, dy-PB/2-5, cx, dy+PB/2+5, "mitte")
dimv(dy-PB/2, dy+PB/2, cx-PL/2-9, f"{PB:g}")
text(cx+PL/2+3, dy+1, "2 Rippen", 2.5, c="sub")

# ================= 3) Formaufbau, Schnitt 1:2
s=0.5; fx, fp = 237.0, 96.0
FX = lambda v: fx + v*s
FY = lambda h: fp - h*s
text(fx,42,"Formaufbau &#183; Schnitt &#183; 1:2",3.3,"middle",w="bold")
rect(FX(-KL/2)-4, FY(KHh)-4, KL*s+8, KHh*s+4, "kasten", 'fill="#eef1f5"')
rect(FX(-KL/2)-4, FY(0),     KL*s+8, KHh*s+4, "kasten", 'fill="#eef1f5"')
rect(FX(-KL/2), FY(KHh), KL*s, KHh*s, "duenn", 'fill="url(#sand)"')
rect(FX(-KL/2), FY(0),   KL*s, KHh*s, "duenn", 'fill="url(#sand)"')
# Gussteil
rect(FX(-PL/2), FY(PT), PL*s, PT*s, "voll", 'fill="url(#metall)"')
for sg in (-1,1):
    x0 = FX(DI/2) if sg>0 else FX(-DA/2)
    rect(x0, FY(NH), (DA-DI)/2*s, (NH-PT)*s, "voll", 'fill="url(#metall)"')
    poly([(FX(sg*DA/2), FY(PT)), (FX(sg*(DA/2+RL)), FY(PT)), (FX(sg*DA/2), FY(PT+RH))],
         "voll", 'fill="url(#metall)"')
    # Ringspeiser
    x1 = FX(DI/2) if sg>0 else FX(-SPA/2)
    rect(x1, FY(KHh), (SPA-DI)/2*s, (KHh-NH)*s, "voll", 'fill="url(#metall)"')
# Kern
rect(FX(-DI/2), FY(KHh), DI*s, (KHh+KMU)*s, "voll", 'fill="url(#kern)"')
# Einguss, Querlauf, Anschnitt, Windpfeife
vE=-75.0
rect(FX(vE-dEin/2), FY(KHh), dEin*s, KHh*s, "voll", 'fill="url(#metall)"')
rect(FX(vE), FY(0), (abs(vE)-PL/2)*s, dAns*s, "voll", 'fill="url(#metall)"')
rect(FX(46-dWi/2), FY(KHh), dWi*s, (KHh-PT)*s, "voll", 'fill="url(#metall)"')
line(FX(-KL/2)-8, fp, FX(KL/2)+8, fp, "teilung")
text(FX(-KL/2)-8, fp-1.8, "Teilungsebene = Plattenunterseite", 2.4, c="gruen")
dimh(FX(-KL/2), FX(-PL/2), FY(0)+9, "40")
dimh(FX(PL/2), FX(KL/2), FY(0)+9, "40")
dimv(FY(KHh), FY(NH), FX(SPA/2)+4, "33", side="right")
# Hinweise
def hinw(vx, hx, tx_x, tx_y, label, an="start"):
    line(FX(vx), FY(hx), tx_x, tx_y, "hilf")
    text(tx_x + (1.6 if an=="start" else -1.6), tx_y+0.9, label, 2.4, an, c="sub")
hinw(SPA/2, 62, FX(24), FY(72), "Ringspeiser &#216;38/&#216;18, offen")
hinw(0, -10, FX(14), FY(-26), "Kern &#216;18 &#8212; unten im Kernlager,")
text(FX(14)+1.6, FY(-26)+4.4, "oben im Speiser gef&#252;hrt", 2.4, c="sub")
hinw(-PL/2, 3, FX(-86), FY(-26), "Anschnitt in der")
text(FX(-86)+1.6, FY(-26)+4.4, "Teilungsebene", 2.4, c="sub")
hinw(46, 58, FX(56), FY(44), "Windpfeife &#216;4")

# ================= 4) Aushebbarkeits-Diagramm
gx0, gy0, gw, gh = 316.0, 128.0, 84.0, 74.0     # Ursprung unten links
text(gx0+gw/2, 42, "Nachweis: Aushebbarkeit", 3.3, "middle", w="bold")
text(gx0+gw/2, 46.5, "Querschnittsfl&#228;che &#252;ber dem Abstand von der Teilung", 2.4, "middle", c="sub")
sx, sy = gw/50.0, gh/5000.0
line(gx0, gy0, gx0+gw, gy0, "achse"); line(gx0, gy0, gx0, gy0-gh, "achse")
text(gx0+gw/2, gy0+7.5, "Abstand von der Teilungsebene [mm]", 2.3, "middle", c="sub")
text(gx0-2, gy0-gh-2, "A [mm&#178;]", 2.3, c="sub")
for a in (0,1000,2000,3000,4000,5000):
    line(gx0-1.2, gy0-a*sy, gx0, gy0-a*sy, "achse")
    text(gx0-2, gy0-a*sy+1, f"{a}", 2.1, "end", c="sub")
for d in (0,10,20,30,40,50):
    line(gx0+d*sx, gy0, gx0+d*sx, gy0+1.2, "achse")
    text(gx0+d*sx, gy0+3.4, f"{d}", 2.1, "middle", c="sub")

def kurve(f, hmax, cls, n=300):
    pts=[]
    for i in range(n+1):
        h=hmax*i/n; A=f(h)
        pts.append(f"{gx0+h*sx:.2f},{gy0-min(A,5000)*sy:.2f}")
    add(f'<polyline points="{" ".join(pts)}" class="{cls}"/>')

def A_neu(h):
    if h < PT: return PL*PB
    A = math.pi/4*DA**2
    if h <= PT+RH: A += 2*RT*RL*(1-(h-PT)/RH)
    return A
def A_alt(t):
    h=45.0-t
    if h >= 45.0-20.0: return 2*math.sqrt(max(400-(45.0-h)**2,0))*32
    if h >= 25.0: return 0.0
    if h >= 6.0:  return 5*32
    return 100*44
kurve(A_alt, 45.0, "kurvebad")
kurve(A_neu, 47.0, "kurveok")
lx0 = gx0 + 11*sx
line(lx0, gy0-4500*sy, lx0+6, gy0-4500*sy, "kurveok")
text(lx0+7.5, gy0-4500*sy+1, "neu: monoton fallend &#8658; ziehbar", 2.35, c="gruen", w="bold")
line(lx0, gy0-4000*sy, lx0+6, gy0-4000*sy, "kurvebad")
text(lx0+7.5, gy0-4000*sy+1, "alter Lagerbock: springt am Ende", 2.35, c="warn", w="bold")
text(lx0+7.5, gy0-3550*sy+1, "von 160 auf 4400 mm&#178; &#8658; Sandausbruch", 2.35, c="warn")

# ================= Textbloecke
def block(x,y,w,h,titel,zeilen,sz=2.6,lh=3.85):
    rect(x,y,w,h,"box"); text(x+3.5,y+6.5,titel,3.2,w="bold")
    yy=y+12.5
    for z in zeilen:
        f=z.startswith("*"); text(x+3.5,yy,z[1:] if f else z,sz,w=("bold" if f else None)); yy+=lh

block(20,196,152,42,"Die Regel, die ich vorher falsch hatte",[
 "*Nicht &#8222;keine konkave Fl&#228;che&#8220; &#8212; sondern:",
 "Jeder Schnitt parallel zur Teilungsebene muss in der",
 "Projektion des n&#228;her an der Teilung liegenden Schnitts",
 "liegen. Die Querschnittsfl&#228;che darf mit dem Abstand",
 "von der Teilung nur abnehmen, nie zunehmen.",
 "Sonst muss beim Ziehen ein breiter Modellteil durch",
 "eine engere Sand&#246;ffnung &#8212; der Sand reisst aus.",
 "*Genau daran sind beide Vorentw&#252;rfe gescheitert."])

block(180,146,124,92,"Formfolge (so wird es gemacht)",[
 "*1  Modell auf das Formbrett stellen",
 "Es steht auf dem unteren Kernmarken-Zapfen,",
 "die Plattenunterseite liegt 15 mm &#252;ber dem Brett.",
 "*2  Unterkasten anformen, abstreifen",
 "Ergebnis: eine ebene Sandfl&#228;che mit einem",
 "einzigen Loch &#8212; dem Kernlager &#216;18 &#215; 15.",
 "*3  Querlauf und Anschnitt einschneiden",
 "beides liegt in der ebenen Teilungsfl&#228;che.",
 "*4  Oberkasten &#252;ber das Modell anformen",
 "mit Einguss-, Speiser- und Windpfeifenstift.",
 "*5  Oberkasten abheben, Modell abnehmen",
 "Das Modell wandert dabei relativ zum Ober-",
 "kasten nach unten &#8212; jeder Querschnitt wird",
 "kleiner, nichts reisst aus.",
 "*6  Kern einsetzen, schliessen, giessen",
 "Der Kern sitzt unten im Kernlager und wird",
 "oben im Speiser gef&#252;hrt &#8212; gegen Auftrieb."])

block(312,146,93,92,"Zahlen zum Vorschlag",[
 "*Bauteil",
 "Fu&#223;platte 110 &#215; 36 &#215; 7",
 "Nabe &#216;34 / Bohrung &#216;18, h = 7 &#8230; 47",
 "2 Rippen 5 mm, 25 &#215; 25",
 "Kehlen R4, Formschr&#228;gen 2&#176;",
 "V = 57 cm&#179; &#8594; m &#8776; 415 g Sn",
 "*Kasten 190 &#215; 90 (vorhanden)",
 "40 mm Sand stirnseitig, 27 mm seitlich",
 "*Speisung",
 "Modul Nabe 3,64 &#183; Platte 3,06 mm",
 "Ringspeiser &#216;38/&#216;18: M = 5,00 mm",
 "gefordert &#8805; 1,2 &#183; 3,64 = 4,36 mm &#10003;",
 "*Kern",
 "&#216;18, Auftrieb F = 0,65 N (66 g)",
 "unten Kernlager 15 mm, oben im Speiser",
 "*Anforderungen",
 "A2 Stehbuchse = reales Maschinenelement",
 "A3 Bohrung nur mit Kern herstellbar",
 "A4 Modell einteilig &#8594; 3D-Druck einfach"])

block(20,244,385,41,"Version F gegen&#252;ber Version O &#8212; E7 bleibt unver&#228;ndert g&#252;ltig",[
 "*Rippe 5 &#8594; 2,5 mm  &#183;  Kehlen R4 &#8594; R0 scharf  &#183;  Nabe &#216;34 &#8594; &#216;42 (gr&#246;&#223;ere Anh&#228;ufung)  &#183;  Speiser vorhanden &#8594; keiner  &#183;  Anschnitt in der Teilung &#8594; von oben  &#183;  280 &#176;C &#8594; 240 &#176;C",
 "Erwartete Fehlerbilder an V-F: Sauglunker in der Nabe und im Knoten Nabe/Platte &#183; Kaltlauf in der 2,5-mm-Rippe &#183; Warmriss an der scharfen Kehle &#183; Gasblasen ohne Entl&#252;ftung.",
 "*Offen und ehrlich benannt: Die Fu&#223;platte (M = 3,06 mm) h&#228;ngt speisungstechnisch am Knoten zur Nabe. Ob der Ringspeiser sie mitspeist, ist im Vorversuch zu messen, nicht zu behaupten.",
 "Ebenfalls offen: Schwindma&#223; (V-S1 / F10), Kernmarkenspiel, Formschr&#228;genrichtung im CAD, Freigabe durch Team (F33) und Prof. P&#228;hler."], sz=2.55, lh=4.6)

add("</svg>")
open("../../90_Assets/Bilder/Stehbuchse_Vorschlag.svg","w",encoding="utf-8").write("\n".join(out))
print("ok")
