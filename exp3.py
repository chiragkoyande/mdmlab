"""
Experiment No. 3
Demonstration of Frequency Reuse Concept in Cellular Systems
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------
# Function to draw a hexagonal cell
# ------------------------------------------------------
def draw_hexagon(ax, x, y, r, color, label):
    angles = np.linspace(0, 2*np.pi, 7)
    hx = x + r*np.cos(angles)
    hy = y + r*np.sin(angles)

    ax.plot(hx, hy, color='black')
    ax.fill(hx, hy, alpha=0.35, color=color)
    ax.text(x, y, label,
            ha='center',
            va='center',
            fontsize=12,
            weight='bold')

# ------------------------------------------------------
# Cell Radius
# ------------------------------------------------------
R = 1

# Seven-cell cluster coordinates
cells = [
    (0, 0),
    (np.sqrt(3)*R, 0),
    (np.sqrt(3)/2*R, 1.5*R),
    (-np.sqrt(3)/2*R, 1.5*R),
    (-np.sqrt(3)*R, 0),
    (-np.sqrt(3)/2*R, -1.5*R),
    (np.sqrt(3)/2*R, -1.5*R)
]

# Frequency allocation
frequencies = ['F1','F2','F3','F4','F5','F6','F7']

colors = ['red',
          'green',
          'blue',
          'orange',
          'purple',
          'cyan',
          'yellow']

fig, ax = plt.subplots(figsize=(8,8))

for i in range(7):
    draw_hexagon(ax,
                 cells[i][0],
                 cells[i][1],
                 R,
                 colors[i],
                 frequencies[i])

# ------------------------------------------------------
# Frequency Reuse
# ------------------------------------------------------

reuse_cells = [
    (0,5),
    (0,-5),
    (6,0),
    (-6,0)
]

for x,y in reuse_cells:
    draw_hexagon(ax,
                 x,
                 y,
                 R,
                 'red',
                 'F1')

ax.set_title("Frequency Reuse in Cellular Communication",
             fontsize=16)

ax.set_aspect('equal')
ax.axis('off')

plt.savefig('/home/chiragk/mdmlab/outputs/exp3_frequency_reuse.png', dpi=150, bbox_inches='tight')
print("EXPERIMENT 3 — Frequency Reuse in Cellular Communication")
print("Graph saved: exp3_frequency_reuse.png")
print("\nThe plot shows:")
print("- Seven hexagonal cells with F1 through F7 allocation")
print("- Reuse of F1 in four distant cells at coordinates (0,5), (0,-5), (6,0), (-6,0)")
