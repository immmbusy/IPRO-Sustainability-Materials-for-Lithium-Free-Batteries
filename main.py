# main.py
"""
Compare illustrative cyclic-voltammetry (CV) curves for Ca, Mg, Al, and Li.

IMPORTANT:
- The electron counts are set to Ca=2, Mg=2, Al=3, Li=1.
- The uploaded project document does not provide complete material-specific
  diffusion/concentration/exchange-current data for all four materials.
- Therefore this is a comparison using shared placeholder parameters, not
  validated predictions for real battery materials.
- cv_model.py uses the Randles-Sevcik form with cm-based units. The shared
  C_bulk below is chosen to correspond approximately to the project's
  ferrocene beta value when D=25e-6 cm^2/s. Replace with measured data when
  available.
"""

import numpy as np
import matplotlib.pyplot as plt

from waveform import triangular_potential
from cv_model import cv_current

# ---------- shared simulation parameters ----------
alpha = 0.5
A = 0.36                 # cm^2
v = 0.2                  # V/s
D = 25.0e-6              # cm^2/s (placeholder)
C_bulk = 2.88e-7          # mol/cm^3 (placeholder; not a measured value)
i0 = 25e-6                # A (placeholder)
E_eq = 0.0                # V

E1 = -0.4
E2 = 0.6
N = 1000

deltaE = E2 - E1
t_half = deltaE / v
t_final = 2 * t_half
t = np.linspace(0, t_final, N)
E_t = triangular_potential(t, E1, E2, v)

# Electron count per reaction from the project table / common ion charges.
materials = {
    "Calcium (Ca²⁺)": 2,
    "Magnesium (Mg²⁺)": 2,
    "Aluminum (Al³⁺)": 3,
    "Lithium (Li⁺)": 1,
}

# Plot one CV curve per material, with shared placeholder parameters.
fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True)
axes = axes.ravel()

for ax, (material, ne) in zip(axes, materials.items()):
    current = cv_current(
        E_t, t,
        ne=ne,
        A=A,
        C_bulk=C_bulk,
        D=D,
        v=v,
        i0=i0,
        alpha=alpha,
        E_eq=E_eq,
    )

    ax.plot(E_t, current * 1e6, linewidth=1.8)
    ax.axhline(0, color="black", linewidth=0.6)
    ax.set_title(f"{material} — ne = {ne}")
    ax.set_xlabel("Potential (V)")
    ax.set_ylabel("Current (µA)")
    ax.grid(True, alpha=0.25)

fig.suptitle(
    "Illustrative CV Curves for Ca, Mg, Al, and Li\n"
    "Shared placeholder parameters; not material-validated",
    fontsize=13,
)
fig.tight_layout()
plt.show()
