# Simple EQE simulator for graded QD stack
# Assumes 100% absorption in bandgap range, 95% charge collection

def simulate_eqe(wavelengths, qd_sizes, thicknesses):
    """
    wavelengths: array of wavelengths in nm
    qd_sizes: list of QD sizes [nm]
    thicknesses: list of layer thicknesses [% of total]
    Returns EQE array
    """
    import numpy as np
    
    # Calculate bandgaps
    bandgaps = [calculate_bandgap(d) for d in qd_sizes]  # Use from bandgap_calculator.py
    
    # Convert bandgap to cutoff wavelength
    cutoffs = [1240 / Eg for Eg in bandgaps]  # λ(nm) = 1240 / E_g(eV)
    
    eqe = np.zeros_like(wavelengths)
    
    for i, cutoff in enumerate(cutoffs):
        # Layer absorbs from UV up to cutoff
        mask = wavelengths <= cutoff
        # Weight by thickness and collection efficiency
        eqe[mask] += thicknesses[i] * 0.95
    
    # Cap at 100%
    eqe = np.minimum(eqe, 1.0)
    return eqe

# Example
import numpy as np
wl = np.arange(300, 900, 10)
qd_sizes = [1.0, 2.5, 4.0]
thicknesses = [0.2, 0.4, 0.4]  # 20%, 40%, 40%

eqe = simulate_eqe(wl, qd_sizes, thicknesses)

for w, e in zip(wl, eqe):
    print(f"{w} nm: {e*100:.1f}%")
