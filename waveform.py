# waveform.py
import numpy as np

def triangular_potential(t_array, E1, E2, v):
    """
    Piece‑wise linear triangular potential:
    E1 -> E2 (forward), then E2 -> E1 (reverse)
    t_array : numpy array of times
    E1, E2  : lower and upper potentials (V)
    v       : scan rate (V/s)
    """
    deltaE = E2 - E1
    t_half = deltaE / v
    E = np.empty_like(t_array, dtype=float)

    for i, ti in enumerate(t_array):
        if ti <= t_half:
            E[i] = E1 + v * ti
        else:
            E[i] = E2 - v * (ti - t_half)
    return E
