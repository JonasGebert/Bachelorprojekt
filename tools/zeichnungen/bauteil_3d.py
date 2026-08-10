# -*- coding: utf-8 -*-
"""3D-Ansicht (Rotationskoerper, viertelgeschnitten) der Miniatur-Riemenscheibe."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def kontur(dN, t, dB=14.0, D=70.0, S=8.0, B=20.0, lN=24.0):
    rN, rB, rKi, rKa = dN/2, dB/2, (D-2*S)/2, D/2
    return [(-lN/2, rB), (-lN/2, rN), (-t/2, rN), (-t/2, rKi),
            (-B/2, rKi), (-B/2, rKa), (B/2, rKa), (B/2, rKi),
            (t/2, rKi), (t/2, rN), (lN/2, rN), (lN/2, rB), (-lN/2, rB)]

def verfeinern(pts, n=6):
    out = []
    for (z1, r1), (z2, r2) in zip(pts[:-1], pts[1:]):
        for i in range(n):
            f = i/n
            out.append((z1 + (z2-z1)*f, r1 + (r2-r1)*f))
    out.append(pts[-1])
    return out

def zeichne(ax, kt, a0=0.0, a1=270.0, farbe="#7d94b0", kern=True, lN=24.0, lKM=12.0, rB=7.0):
    pts = verfeinern(kt, 8)
    z = np.array([p[0] for p in pts])
    r = np.array([p[1] for p in pts])
    th = np.radians(np.linspace(a0, a1, 90))
    Z, T = np.meshgrid(z, th)
    R, _ = np.meshgrid(r, th)
    X, Y = R*np.cos(T), R*np.sin(T)
    ax.plot_surface(X, Y, Z, color=farbe, linewidth=0, antialiased=True,
                    shade=True, rstride=1, cstride=1, alpha=1.0)
    # Schnittflaechen an den beiden Winkelgrenzen
    for a in (a0, a1):
        c, s = np.cos(np.radians(a)), np.sin(np.radians(a))
        poly = [(rr*c, rr*s, zz) for zz, rr in kt]
        pc = Poly3DCollection([poly], facecolor="#c9d6e4", edgecolor="#24405e", linewidths=0.6)
        ax.add_collection3d(pc)
    if kern:
        lk = lN + 2*lKM
        th2 = np.radians(np.linspace(0, 360, 80))
        zz = np.linspace(-lk/2, lk/2, 2)
        T2, Z2 = np.meshgrid(th2, zz)
        ax.plot_surface(rB*np.cos(T2), rB*np.sin(T2), Z2,
                        color="#e3c766", linewidth=0, shade=True, alpha=1.0)

def setup(ax, titel):
    ax.set_box_aspect((1, 1, 0.62))
    ax.set_xlim(-35, 35); ax.set_ylim(-35, 35); ax.set_zlim(-25, 25)
    ax.view_init(elev=24, azim=-55)
    ax.set_axis_off()

fig = plt.figure(figsize=(11, 4.4), dpi=200)
fig.patch.set_facecolor("white")

ax1 = fig.add_subplot(1, 2, 1, projection="3d")
zeichne(ax1, kontur(dN=28, t=5.0))
setup(ax1, "")

ax2 = fig.add_subplot(1, 2, 2, projection="3d")
zeichne(ax2, kontur(dN=36, t=2.5))
setup(ax2, "")

fig.suptitle("Miniatur-Riemenscheibe — 3D-Ansicht, Viertel ausgeschnitten (Kern gelb)",
             fontsize=13, weight="bold", color="#14243a", y=0.965)
fig.text(0.5, 0.035,
         "Prinzipdarstellung ohne Schwindmaß, ohne Formschrägen, ohne Radien · Maße in mm · "
         "Quelle: 32_Konstruktion/Bauteilkonzept.md",
         ha="center", fontsize=8, color="#4a5b70")
fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.08, wspace=0.02)
ax1.set_position([-0.04, -0.12, 0.58, 1.06])
ax2.set_position([ 0.46, -0.12, 0.58, 1.06])
for x, t1, t2 in ((0.25, "Version O — optimiert", "Steg 5 mm · Nabe Ø28 · Kehlen R3"),
                  (0.75, "Version F — fehlerprovozierend", "Steg 2,5 mm · Nabe Ø36 · Kehlen R0")):
    fig.text(x, 0.855, t1, ha="center", fontsize=11.5, weight="bold", color="#14243a")
    fig.text(x, 0.795, t2, ha="center", fontsize=9, color="#4a5b70")
fig.savefig("../../90_Assets/Bilder/Bauteil-Riemenscheibe_3D.png",
            facecolor="white")
print("ok")
