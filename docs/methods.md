# Simulation Methodology — EcoQD-19

## Bandgap Calculation

Bandgap of CuInGaZnS₂ QDs estimated via quantum confinement model:

E_g(d) = E_g(bulk) + (ħ²π² / 2μd²)

Where:
- d = QD diameter (nm)
- μ = reduced mass (0.1m₀ for CIS)
- E_g(bulk) = 1.50 eV for CuInS₂ → adjusted for Ga/Zn alloying

## EQE Simulation

Used transfer matrix method (TMM) for graded absorber stack. Assumed:

- Absorption coefficient α(λ) from published CIS QD data
- Reflection losses minimized via MgF₂ ARC
- Charge collection efficiency = 95% for all layers

## Stability Prediction

Based on:
- Zwitterionic ligand → resists humidity
- Br⁻ passivation → reduces surface traps
- NiOₓ/MoOₓ → blocks oxygen/moisture ingress

## Efficiency Calculation

PCE = (Jsc × Voc × FF) / Pin

Pin = 100 mW/cm² (AM1.5G)
Jsc = ∫ EQE(λ) × AM1.5(λ) dλ
Voc = E_g/q - 0.4 V (empirical loss factor)
FF = 0.80 (optimized interfaces)
