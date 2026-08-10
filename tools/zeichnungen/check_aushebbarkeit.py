# -*- coding: utf-8 -*-
"""
Aushebbarkeits-Nachweis (Projektionsregel):
Ein Modellteil laesst sich nur ziehen, wenn seine Querschnittsflaeche mit
wachsendem Abstand von der Teilungsebene MONOTON NICHT ZUNIMMT und jeder
Querschnitt in der Projektion des naeher an der Teilung liegenden liegt.
"""
import math

def pruefe(name, f, hmax, n=400):
    hs = [hmax*i/n for i in range(n+1)]
    A  = [f(h) for h in hs]
    verstoss = []
    for i in range(1, len(A)):
        if A[i] > A[i-1] + 1e-9:
            verstoss.append((hs[i], A[i-1], A[i]))
    ok = not verstoss
    print(f"{name:<46} {'OK  ziehbar' if ok else 'FEHLER  Hinterschnitt'}")
    if verstoss:
        h, a0, a1 = verstoss[0]
        print(f"    erster Verstoss bei h = {h:.1f} mm:  A waechst von {a0:.0f} auf {a1:.0f} mm^2")
    return ok

# ---------- 1) Riemenscheibe, Teilung durch die Achse -----------------------
# Querschnitt parallel zur Teilungsebene in der Tiefe y unter der Achse.
D, B, S, dN, lN, tS = 70., 20., 8., 28., 24., 5.
rKa, rKi, rN = D/2, (D-2*S)/2, dN/2
def A_riemenscheibe(y):
    """Flaeche des Modellhalbteils im Horizontalschnitt in der Tiefe y."""
    A = 0.0
    # Kranz: Ringflaeche rKi..rKa, axiale Breite B  -> zwei Streifen
    for r0, r1, br in ((rKi, rKa, B), (0.0, rN, lN)):     # Kranz und Nabe
        if y < r1:
            x1 = math.sqrt(max(r1*r1 - y*y, 0.0))
            x0 = math.sqrt(max(r0*r0 - y*y, 0.0)) if y < r0 else 0.0
            A += 2*(x1 - x0)*br
    # Steg
    if y < rKi:
        x1 = math.sqrt(max(rKi*rKi - y*y, 0.0))
        x0 = math.sqrt(max(rN*rN - y*y, 0.0)) if y < rN else 0.0
        A += 2*(x1-x0)*tS
    return A

# ---------- 2) Lagerbock mit waagerechter Bohrung, Teilung durch die Achse --
PL, PB, PT = 100., 44., 6.
RB, RL, RH1 = 5., 32., 25.
DA, LA, HA = 40., 32., 45.
def A_lagerbock_waagerecht(t):
    """t = Abstand unter der Teilungsebene (h = HA - t)."""
    h = HA - t
    if h >= HA - DA/2:                      # Lagerauge (liegender Zylinder)
        y = HA - h
        return 2*math.sqrt(max((DA/2)**2 - y*y, 0.0))*LA
    if h >= RH1:  return 0.0
    if h >= PT:   return RB*RL
    return PL*PB

# ---------- 3) Neuer Vorschlag: Stehbuchse, Bohrung senkrecht ---------------
NPL, NPB, NPT = 110., 36., 7.
NDA, NDI, NH = 34., 18., 47.
RT, RLg, RHh = 5., 25., 25.
def A_stehbuchse(h):
    """h = Hoehe ueber der Teilungsebene (= Plattenunterseite). Modell, also Bohrung voll."""
    if h < NPT:  return NPL*NPB
    A = math.pi/4*NDA**2
    if h <= NPT + RHh:
        l = RLg*(1 - (h-NPT)/RHh)
        A += 2*RT*l
    return A

print("Aushebbarkeit (Projektionsregel), Querschnitt parallel zur Teilungsebene\n")
pruefe("1) Riemenscheibe, Teilung durch die Achse", A_riemenscheibe, 34.9)
pruefe("2) Lagerbock, waagerechte Bohrung", A_lagerbock_waagerecht, 45.0)
pruefe("3) Stehbuchse, senkrechte Bohrung (neu)", A_stehbuchse, 47.0)

print("\nMassen und Moduln des neuen Vorschlags")
V_pl = NPL*NPB*NPT
V_na = math.pi/4*(NDA**2-NDI**2)*(NH-NPT)
V_ri = 2*0.5*RLg*RHh*RT
V = V_pl+V_na+V_ri
print(f"  V = {V:.0f} mm^3 = {V/1000:.1f} cm^3   ->  m = {V*7.29/1000:.0f} g Sn")
A_na = math.pi*NDA*(NH-NPT) + math.pi*NDI*(NH-NPT) + math.pi/4*(NDA**2-NDI**2)
print(f"  Modul Nabe    M = {V_na/A_na:.2f} mm")
A_pl = 2*NPL*NPB + 2*(NPL+NPB)*NPT - math.pi/4*NDA**2
print(f"  Modul Platte  M = {V_pl/A_pl:.2f} mm")
SPa, SPi = 38., 18.
M_sp = (math.pi/4*(SPa**2-SPi**2))/(math.pi*(SPa+SPi))
print(f"  Modul Ringspeiser Ø{SPa:g}/Ø{SPi:g}: M = {M_sp:.2f} mm"
      f"   (gefordert >= 1,2 x Nabe = {1.2*V_na/A_na:.2f} mm)")
V_kern = math.pi/4*NDI**2*NH
F = V_kern*1e-9*(7000-1500)*9.81
print(f"  Kernauftrieb  F = {F:.2f} N  ({F/9.81*1000:.0f} g)")
print(f"  Sandumhuellung im Kasten 190x90: {(190-NPL)/2:.0f} mm stirnseitig, "
      f"{(90-NPB)/2:.0f} mm seitlich")
