# cv_model.py
import numpy as np

# physical constants
F = 96485.0        # C mol^-1 e-
R = 8.31447        # J mol^-1 K^-1
T = 298.0          # K

def randles_sevcik_peak(ne, A, C_bulk, D, v):
    """
    Randles–Ševčik peak current (A)
    ne      : electrons per reaction
    A       : electrode area (cm^2)
    C_bulk  : bulk concentration (mol cm^-3)
    D       : diffusion coefficient (cm^2 s^-1)
    v       : scan rate (V s^-1)
    """
    return 2.69e5 * (ne**1.5) * A * C_bulk * np.sqrt(D) * np.sqrt(v)


def butler_volmer_current(E, i0, ne, alpha, E_eq):
    """
    Butler–Volmer current (A) at potential E.
    """
    arg_fwd = ((1 - alpha) * ne * F * (E - E_eq)) / (R * T)
    arg_rev = (-alpha * ne * F * (E - E_eq)) / (R * T)
    return i0 * (np.exp(arg_fwd) - np.exp(arg_rev))


def cottrell_current(t_since_peak, ne, A, C_bulk, D):
    """
    Cottrell current (A) – diffusion‑controlled, decays ~ 1/sqrt(t)
    """
    return ne * F * A * C_bulk * np.sqrt(D / (np.pi * t_since_peak))


def cv_current(E_t, t_array, *,
               ne, A, C_bulk, D,
               v, i0, alpha, E_eq):
    """
    Build i(t) for one CV cycle using:
      - Butler–Volmer until peak
      - Randles–Ševčik for the peak value
      - Cottrell for decay after peak
    Returns array i(t) in A.
    """
    deltaE = E_t.max() - E_t.min()
    t_half = deltaE / v

    i_peak_RS = randles_sevcik_peak(ne, A, C_bulk, D, v)
    i = np.zeros_like(E_t)
    half_idx = np.argmin(np.abs(t_array - t_half))

    # ----- forward sweep -----
    reached_peak = False
    t_peak = None
    for k in range(half_idx + 1):
        E = E_t[k]
        if not reached_peak:
            i_BV = butler_volmer_current(E, i0, ne, alpha, E_eq)
            if abs(i_BV) >= i_peak_RS:
                reached_peak = True
                t_peak = t_array[k]
                i[k] = np.sign(i_BV) * i_peak_RS
            else:
                i[k] = i_BV
        else:
            dt = t_array[k] - t_peak
            i[k] = np.sign(i[k-1]) * cottrell_current(dt, ne, A, C_bulk, D)

    # ----- reverse sweep -----
    reached_peak = False
    t_peak = None
    for k in range(half_idx + 1, len(t_array)):
        E = E_t[k]
        if not reached_peak:
            i_BV = butler_volmer_current(E, i0, ne, alpha, E_eq)
            if abs(i_BV) >= i_peak_RS:
                reached_peak = True
                t_peak = t_array[k]
                i[k] = np.sign(i_BV) * i_peak_RS
            else:
                i[k] = i_BV
        else:
            dt = t_array[k] - t_peak
            i[k] = np.sign(i[k-1]) * cottrell_current(dt, ne, A, C_bulk, D)

    return i
