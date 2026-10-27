# IPRO: Theoretical Modeling of Eco-Friendly Lithium-Free Battery Materials

An electrochemistry simulation tool developed for the **IPRO Sustainability Materials for Lithium-Free Batteries** project. This Python application models battery material behavior by simulating potential waveforms and generating **Cyclic Voltammetry (CV)** curves using fundamental electrochemical equations.

---

## 📌 Project Overview

The main goal of this project is to model and compare alternative anode materials (e.g., Magnesium, Zinc, Aluminum, Ferrocene) against traditional Lithium anodes for next-generation eco-friendly energy storage.

The simulation program:
1. Generates a **Triangular Potential Waveform** $E(t)$ across a time domain $[0, t_{\text{final}}]$.
2. Computes current response using the **Butler-Volmer Equation** (initial activation/rise).
3. Determines peak current limits $i_{\text{peak}}$ using the **Randles-Sevcik Equation**.
4. Simulates diffusion-controlled current decay past peak potential using the **Cottrell Equation**.
5. Plots the resulting **Cyclic Voltammogram (CV Curve)** of Current ($\mu\text{A}$) versus Potential ($\text{V}$).

---

## 📐 Electrochemical Equations & Mathematical Foundation

### 1. Potential Waveform $E(t)$
A triangular waveform applied at scan rate $v = \pm 0.2\,\text{V/s}$ between initial potential $E_1 = -0.50\,\text{V}$ and switching potential $E_2 = +0.50\,\text{V}$:
$$E(t) = \begin{cases} E_1 + v \cdot t & 0 \le t \le t_{\text{switch}} \\ E_2 - v \cdot (t - t_{\text{switch}}) & t_{\text{switch}} < t \le t_{\text{final}} \end{cases}$$

### 2. Butler-Volmer Equation (Current Density / Initial Growth)
Describes the charge-transfer kinetics at the electrode interface:
$$i(E) = i_0 \left[ \exp\left( \frac{(1-\alpha) n_e F (E - E_{\text{eq}})}{R T} \right) - \exp\left( -\frac{\alpha n_e F (E - E_{\text{eq}})}{R T} \right) \right]$$

### 3. Randles-Sevcik Equation (Peak Current Limit)
Calculates maximum achievable peak current $i_{\text{peak}}$ under linear sweep voltammetry:
$$i_{\text{peak}} = (2.69 \times 10^5) \, n_e^{3/2} \, A \, \beta \sqrt{v}$$
*where $\beta = C_{\text{bulk}}\sqrt{D}$.*

### 4. Cottrell Equation (Diffusion Current Decay)
Describes the current decline over time past the peak oxidation/reduction points:
$$i(t) = \frac{n_e F A \beta}{\sqrt{\pi t}}$$

---

## 📊 Physical Constants & Simulation Parameters

| Parameter | Notation | Benchmark Value | Units |
| :--- | :--- | :--- | :--- |
| **Faraday Constant** | $F$ | `96485` | $\text{C / mol e}^-$ |
| **Universal Gas Constant** | $R$ | `8.31447` | $\text{J / (mol}\cdot\text{K)}$ |
| **Temperature** | $T$ | `298` | $\text{K}$ |
| **Transfer Coefficient** | $\alpha$ | `0.5` | unitless |
| **Scan Rate** | $v$ | `0.2` | $\text{V/s}$ |
| **Electrode Surface Area** | $A$ | $0.36 \times 10^{-4}$ | $\text{m}^2$ |
| **Exchange Current** | $i_0$ | `25` | $\mu\text{A}$ |

---

## 🧪 Material Benchmarks

| Material | Electrons Transferred ($n_e$) | Compound Property $\beta = C\sqrt{D}$ ($\text{mol} / (\text{m}^3\cdot\text{s}^{1/2})$) |
| :--- | :---: | :---: |
| **Ferrocene (FCN)** *(Validation Model)* | `1` | $1.44 \times 10^{-5}$ |
| **Lithium (Li)** | `1` | Target Benchmark |
| **Magnesium (Mg)** | `2` | Eco-Friendly Candidate |
| **Zinc (Zn)** | `2` | Eco-Friendly Candidate |
| **Calcium (Ca)** | `2` | Eco-Friendly Candidate |
| **Aluminum (Al)** | `3` | Eco-Friendly Candidate |

---

## 🛠️ Requirements & Dependencies

Make sure Python 3.8+ is installed along with the following libraries:

```bash
pip install numpy matplotlib scipy
