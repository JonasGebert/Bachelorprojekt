# -*- coding: utf-8 -*-
"""
Lagerbock (Stehlager) — Bauteilvorschlag + Formaufbau, A3 quer, SVG.
Bauteil 1:1, Formansichten 1:2. Alle Masse in mm.
"""
import math

W, H = 420.0, 297.0

# ---------------- Bauteil Version O
PL, PB, PT = 100.0, 44.0, 6.0      # Grundplatte L x B x Dicke
RB, RL = 5.0, 32.0                 # Rippe: Dicke, Laenge (in Achsrichtung)
RH0, RH1 = PT, 25.0                # Rippe von h=6 bis h=25
DA, DI, LA = 40.0, 20.0, 32.0      # Lagerauge: Aussen-Ø, Bohrung, Breite
HA = 45.0                          # Achshoehe ueber Plattenunterseite
KM = 14.0                          # Kernmarke je Seite
LKERN = LA + 2*KM                  # 60
HG = HA + DA/2                     # 65 Gesamthoehe

# ---------------- Formkasten (vorhanden, F19)
KL, KB, KHh = 190.0, 90.0, 80.0
WDs = 4.0                          # Wandstaerke in der 1:2-Darstellung
dSp, dEin, dAns, dWi = 20.0, 10.0, 6.0, 4.0

out=[]
def add(s): out.append(s)
def line(x1,y1,x2,y2,c="voll"): add(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" class="{c}"/>')
def rect(x,y,w,h,c="voll",e=""): add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" class="{c}" {e}/>')
def circ(cx,cy,d,c="voll",e=""): add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{d/2:.2f}" class="{c}" {e}/>')
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
def hilf(x1,y1,x2,y2): line(x1,y1,x2,y2,"hilf")

add('<?xml version="1.0" encoding="UTF-8"?>')
add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">')
add("""<defs>
<pattern id="metall" width="2.4" height="2.4" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
  <rect width="2.4" height="2.4" fill="#dce6f2"/><line x1="0" y1="0" x2="0" y2="2.4" stroke="#2b5c96" stroke-width="0.28"/>
</pattern>
<pattern id="sand" width="3.0" height="3.0" patternUnits="userSpaceOnUse">
  <rect width="3.0" height="3.0" fill="#f3ece1"/>
  <circle cx="0.7" cy="0.7" r="0.22" fill="#c2ab8c"/><circle cx="2.2" cy="2.1" r="0.22" fill="#c2ab8c"/>
</pattern>
<pattern id="kern" width="2.4" height="2.4" patternUnits="userSpaceOnUse">
  <rect width="2.4" height="2.4" fill="#f6e2a8"/>
  <circle cx="0.6" cy="0.6" r="0.24" fill="#c9a63c"/><circle cx="1.8" cy="1.8" r="0.24" fill="#c9a63c"/>
</pattern>
<style>
 text{font-family:"DejaVu Sans",Arial,sans-serif;fill:#14243a;}
 .voll{stroke:#14243a;stroke-width:0.5;fill:none;}
 .duenn{stroke:#14243a;stroke-width:0.28;fill:none;}
 .verdeckt{stroke:#14243a;stroke-width:0.3;fill:none;stroke-dasharray:2.5 1.5;}
 .kasten{stroke:#14243a;stroke-width:0.7;fill:none;}
 .mitte{stroke:#b03030;stroke-width:0.25;fill:none;stroke-dasharray:7 1.4 1.1 1.4;}
 .teilung{stroke:#0a7a5a;stroke-width:0.7;fill:none;}
 .masz{stroke:#14243a;stroke-width:0.25;fill:none;}
 .hilf{stroke:#14243a;stroke-width:0.18;fill:none;}
 .pfeil{fill:#14243a;stroke:none;}
 .rahmen{stroke:#14243a;stroke-width:0.7;fill:none;}
 .box{stroke:#8fa2bb;stroke-width:0.35;fill:#f7f9fc;}
 .gruen{fill:#0a7a5a;} .warn{fill:#b03030;} .sub{fill:#4a5b70;}
</style></defs>""")
add(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
rect(10,10,W-20,H-20,"rahmen")
text(16,20,"Lagerbock (Stehlager) &#8212; Bauteilvorschlag statt Riemenscheibe",6.2,w="bold")
text(16,26,"Hinterschnittfrei bei ebener Teilung &#183; ein Kern &#183; passt in die vorhandenen Formk&#228;sten 190 &#215; 90 &#215; 80/80 mm",3.1,c="sub")
text(404,20,"VORSCHLAG zu F33 &#8212; Team entscheidet",3.3,"end",c="warn",w="bold")
line(16,29.5,404,29.5,"masz")

# =============================================== 1) Bauteil, Vorderansicht 1:1
cx, base = 62.0, 122.0                      # base = h=0
Y = lambda h: base - h
text(cx, 44, "Bauteil Version O &#183; Vorderansicht", 3.4, "middle", w="bold")
text(cx, 48.5, "Blick in Richtung der Bohrungsachse &#183; 1:1", 2.6, "middle", c="sub")
rect(cx-PB/2, Y(PT), PB, PT, "voll", 'fill="url(#metall)"')
rect(cx-RB/2, Y(RH1), RB, RH1-RH0, "voll", 'fill="url(#metall)"')
circ(cx, Y(HA), DA, "voll", 'fill="url(#metall)"')
circ(cx, Y(HA), DI, "voll", 'fill="#ffffff"')
line(cx-DA/2-7, Y(HA), cx+DA/2+7, Y(HA), "mitte")
line(cx, Y(HG)-7, cx, Y(0)+7, "mitte")
dimh(cx-PB/2, cx+PB/2, Y(0)+11, f"{PB:g}")
dimv(Y(HG), Y(0), cx-PB/2-13, f"{HG:g}")
dimv(Y(HA), Y(0), cx-PB/2-6, f"{HA:g}")
line(cx+14.1, Y(HA)-14.1, cx+27, Y(HA)-25, "hilf")
text(cx+28, Y(HA)-25.5, f"&#216;{DA:g}", 2.8)
line(cx+7.1, Y(HA)+7.1, cx+27, Y(HA)+16, "hilf")
text(cx+28, Y(HA)+17, f"&#216;{DI:g} &#8212; vom Kern", 2.8)
text(cx+RB/2+3, Y(15)+1, f"Rippe {RB:g}", 2.6)
text(cx+PB/2+3, Y(PT/2)+1, f"Platte {PT:g}", 2.6)

# =============================================== 2) Bauteil, Schnitt A-A 1:1
cx2, base2 = 96.0, 240.0
Y2 = lambda h: base2 - h
text(cx2, 150, "Schnitt A&#8211;A &#183; durch die Bohrungsachse", 3.4, "middle", w="bold")
text(cx2, 154.5, "Kern eingezeichnet, mit Kernmarken &#183; 1:1", 2.6, "middle", c="sub")
rect(cx2-PL/2, Y2(PT), PL, PT, "voll", 'fill="url(#metall)"')
rect(cx2-RL/2, Y2(RH1), RL, RH1-RH0, "voll", 'fill="url(#metall)"')
rect(cx2-LA/2, Y2(HG), LA, (HG-(HA+DI/2)), "voll", 'fill="url(#metall)"')
rect(cx2-LA/2, Y2(HA-DI/2), LA, ((HA-DI/2)-RH1), "voll", 'fill="url(#metall)"')
rect(cx2-LKERN/2, Y2(HA+DI/2), LKERN, DI, "voll", 'fill="url(#kern)"')
line(cx2-LA/2, Y2(HA+DI/2), cx2-LA/2, Y2(HA-DI/2), "verdeckt")
line(cx2+LA/2, Y2(HA+DI/2), cx2+LA/2, Y2(HA-DI/2), "verdeckt")
line(cx2-LKERN/2-7, Y2(HA), cx2+LKERN/2+7, Y2(HA), "mitte")
dimh(cx2-PL/2, cx2+PL/2, Y2(0)+11, f"{PL:g}")
dimh(cx2-LA/2, cx2+LA/2, Y2(HG)-6, f"{LA:g}")
dimh(cx2-LKERN/2, cx2+LKERN/2, Y2(HG)-13, f"Kern {LKERN:g}")
dimh(cx2-LKERN/2, cx2-LA/2, Y2(HA)-13, f"{KM:g}")
text(cx2+LKERN/2+3, Y2(HA)+1, "Kernmarke", 2.4, c="sub")
text(cx2-PL/2-3, Y2(PT/2)+1, f"{PT:g}", 2.6, "end")

# =============================================== 3) Formaufbau, Schnitt quer 1:2
s = 0.5
fx, fp = 210.0, 96.0                      # fp = Hoehe der Teilungsebene auf dem Blatt
FX = lambda u: fx + u*s
FY = lambda h: fp - (h-HA)*s              # h=HA liegt auf der Teilung
text(fx, 44, "Formaufbau &#183; Schnitt quer zur Achse", 3.4, "middle", w="bold")
text(fx, 48.5, "Ma&#223;stab 1:2", 2.6, "middle", c="sub")
rect(FX(-KB/2)-WDs, FY(HA+KHh)-WDs, KB*s+2*WDs, KHh*s+WDs, "kasten", 'fill="#eef1f5"')
rect(FX(-KB/2)-WDs, FY(HA),         KB*s+2*WDs, KHh*s+WDs, "kasten", 'fill="#eef1f5"')
rect(FX(-KB/2), FY(HA+KHh), KB*s, KHh*s, "duenn", 'fill="url(#sand)"')
rect(FX(-KB/2), FY(HA),     KB*s, KHh*s, "duenn", 'fill="url(#sand)"')
rect(FX(-PB/2), FY(PT), PB*s, PT*s, "voll", 'fill="url(#metall)"')
rect(FX(-RB/2), FY(RH1), RB*s, (RH1-RH0)*s, "voll", 'fill="url(#metall)"')
circ(fx, FY(HA), DA*s, "voll", 'fill="url(#metall)"')
circ(fx, FY(HA), DI*s, "voll", 'fill="url(#kern)"')
rect(FX(-dSp/2), FY(HA+KHh), dSp*s, (KHh-(HG-HA))*s, "voll", 'fill="url(#metall)"')
rect(FX(DA/2), FY(HA+dAns/2), 9*s, dAns*s, "voll", 'fill="url(#metall)"')
line(FX(-KB/2)-WDs-4, FY(HA), FX(KB/2)+WDs+4, FY(HA), "teilung")
text(FX(-KB/2)-WDs-4, FY(HA)-1.8, "Teilungsebene", 2.4, c="gruen")
dimv(FY(HA+KHh), FY(HG), FX(-PB/2)-7, "60")
dimv(FY(0), FY(HA-KHh), FX(-PB/2)-7, "35")
dimh(FX(-KB/2), FX(-DA/2), FY(HA)+16, "25")
text(fx, FY(HA+KHh)-3, "Speiser &#216;20, offen", 2.4, "middle", c="sub")
rect(FX(-DA/2-9), FY(HA+dWi/2), 9*s, dWi*s, "voll", 'fill="url(#metall)"')
text(FX(DA/2+11), FY(HA)-1.5, "Anschnitt", 2.4, c="sub")
text(FX(-DA/2-11), FY(HA)-1.5, "Windpfeife", 2.4, "end", c="sub")

# =============================================== 4) Draufsicht Teilungsebene 1:2
gx, gy = 320.0, 96.0
GX = lambda v: gx + v*s
GY = lambda u: gy + u*s
text(gx, 44, "Draufsicht auf die Teilungsebene", 3.4, "middle", w="bold")
text(gx, 48.5, "Unterkasten, Gie&#223;system &#183; 1:2", 2.6, "middle", c="sub")
rect(GX(-KL/2)-WDs, GY(-KB/2)-WDs, KL*s+2*WDs, KB*s+2*WDs, "kasten", 'fill="#eef1f5"')
rect(GX(-KL/2), GY(-KB/2), KL*s, KB*s, "duenn", 'fill="url(#sand)"')
rect(GX(-PL/2), GY(-PB/2), PL*s, PB*s, "verdeckt")          # Platte darunter
rect(GX(-LA/2), GY(-DA/2), LA*s, DA*s, "voll", 'fill="url(#metall)"')
for sgn in (-1,1):
    x0 = GX(sgn*LA/2) if sgn>0 else GX(-LA/2-KM)
    rect(x0, GY(-DI/2), KM*s, DI*s, "voll", 'fill="url(#kern)"')
uE, uQ = -70.0, 29.0
rect(GX(uE), GY(uQ-4), (abs(uE))*s, 8*s, "voll", 'fill="url(#metall)"')   # Querlauf
rect(GX(-3), GY(DA/2), 6*s, (uQ-DA/2)*s, "voll", 'fill="url(#metall)"')   # Anschnitt
circ(GX(uE), GY(uQ), dEin*s, "voll", 'fill="url(#metall)"')
circ(GX(0), GY(-uQ+6), dWi*s, "voll", 'fill="url(#metall)"')
rect(GX(-2), GY(-uQ+6), 4*s, (uQ-6-DA/2)*s, "voll", 'fill="url(#metall)"')
line(GX(-KL/2)-4, GY(0), GX(KL/2)+4, GY(0), "mitte")
line(GX(uE), GY(uQ)+3, GX(uE), gy+31, "hilf")
text(GX(-42), gy+34, "Einguss &#216;10 senkrecht + Querlauf in der Teilungsebene", 2.4, "middle", c="sub")
line(GX(3), GY(uQ-4), GX(26), gy+29, "hilf")
text(GX(27), gy+30, "Anschnitt &#216;6", 2.4, c="sub")
line(GX(2), GY(-uQ+6), GX(20), gy-30, "hilf")
text(GX(21), gy-30, "Windpfeife &#216;4", 2.4, c="sub")
line(GX(-LA/2-KM/2), GY(-DI/2), GX(-46), gy-30, "hilf")
text(GX(-47), gy-30, "Kernmarke", 2.4, "end", c="sub")
dimh(GX(-KL/2), GX(KL/2), gy+42, "190")
dimv(GY(-KB/2), GY(KB/2), GX(KL/2)+7, "90", side="right")

# =============================================== Textspalten
def block(x, y, w, h, titel, zeilen, sz=2.65, lh=4.0):
    rect(x, y, w, h, "box")
    text(x+3.5, y+6.5, titel, 3.3, w="bold")
    yy = y + 12.5
    for z in zeilen:
        fett = z.startswith("*")
        text(x+3.5, yy, z[1:] if fett else z, sz, w=("bold" if fett else None))
        yy += lh

block(165, 150, 118, 62, "Warum dieses Bauteil hinterschnittfrei ist", [
 "Teilungsebene = waagerechte Ebene durch die",
 "Bohrungsachse (h = 45 mm), gr&#246;&#223;ter Querschnitt",
 "des Lagerauges liegt darin.",
 "*Entscheidend: keine zur Ausheberichtung",
 "*konkave Fl&#228;che im Modell.",
 "Lagerauge, Rippe und Platte sind nach au&#223;en",
 "konvex bzw. eben; die einzige konkave Fl&#228;che",
 "ist die Bohrung &#8212; und die macht der Kern,",
 "nicht das Modell. Genau daran ist die",
 "Riemenscheibe gescheitert (Ringnut hinter",
 "der Kranz-Innenfl&#228;che &#216;54)."])

block(288, 150, 118, 62, "Anforderungscheck", [
 "*A2 reales Bauteil &#8212; Stehlager, echtes",
 "  Maschinenelement, Funktion plausibel",
 "*A3 mindestens ein Kern &#8212; Bohrung &#216;20",
 "  zwingend gekernt, Kern &#216;20 &#215; 60 liegend",
 "*A4 Modell / Kernkasten &#8212; geteiltes Modell,",
 "  Teilung durch die Achse, 3D-Druck wie E5",
 "*A5/A6 Zinn &#8212; unver&#228;ndert, ca. 0,43 kg",
 "*E7 zwei Versionen &#8212; F/O bleibt erhalten,",
 "  gleiche Au&#223;enkontur, siehe Tabelle unten",
 "Kastenpassung: 25 mm Sand seitlich, 35 mm",
 "unter der Platte, 45 mm an den Stirnseiten."])

block(165, 216, 118, 69, "Gie&#223;technik", [
 "*Erstarrungsmoduln (M = V/A):",
 "Lagerauge 3,9 &#183; Grundplatte 2,6 &#183; Rippe 2,2 mm",
 "&#8594; Die dickste Stelle liegt oben, direkt unter",
 "dem Speiser. Genau das war bei der Riemen-",
 "scheibe nicht erreichbar.",
 "*Speiser: &#216;20 &#8594; M = d/4 = 5,0 mm",
 "erforderlich M &#8805; 1,2 &#183; 3,9 = 4,7 mm &#10003;",
 "*Offener Punkt:",
 "Der Oberkasten ist 80 mm hoch, der offene",
 "Speiser wird dadurch 60 mm lang (ca. 137 g",
 "Kreislaufmaterial). Mit einem selbst gebauten",
 "40-mm-Oberkasten (A4 verlangt den Bau",
 "ohnehin) w&#228;ren es ca. 46 g.",
 "*Kernauftrieb: F = V &#183; &#916;&#961; &#183; g = 0,54 N",
 "(&#8776; 55 g) &#8594; Kernmarken 14 mm gen&#252;gen."], sz=2.5, lh=3.55)

block(288, 216, 118, 69, "Version F gegen&#252;ber Version O", [
 "*Merkmal                V-O            V-F",
 "Rippe                      5 mm         2,5 mm",
 "Kehlen                    R3               R0 scharf",
 "Lagerauge             &#216;40             &#216;48",
 "Anschnitt                seitlich       oben a. Rippe",
 "Speiser                    &#216;20             keiner",
 "Entl&#252;ftung             Windpfeife  keine",
 "Gie&#223;temperatur    ca. 280 &#176;C  ca. 240 &#176;C",
 "*Erwartete Fehlerbilder an V-F:",
 "Sauglunker im Lagerauge (keine Speisung) &#183;",
 "Kaltlauf in der 2,5-mm-Rippe &#183; Warmriss an",
 "der scharfen Kehle Rippe/Platte (Knoten-",
 "punkt) &#183; Gasblasen ohne Entl&#252;ftung.",
 "*Didaktisch neu gegen&#252;ber der Riemenscheibe:",
 "Der Knotenpunkt Rippe/Grundplatte ist das",
 "Lehrbuchbeispiel f&#252;r Materialanh&#228;ufung."], sz=2.5, lh=3.55)

add("</svg>")
open("../../90_Assets/Bilder/Lagerbock_Vorschlag.svg","w",encoding="utf-8").write("\n".join(out))
print("ok")
