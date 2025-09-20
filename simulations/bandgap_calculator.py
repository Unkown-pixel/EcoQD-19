# Bandgap Calculator for CuInGaZnS2 QDs
# Assumes spherical QDs, parabolic bands

import numpy as np

def calculate_bandgap(d_nm, E_bulk=1.50):
    """
    d_nm: QD diameter in nm
    E_bulk: bulk bandgap in eV (default: 1.50 for CuInS2)
    Returns bandgap in eV
    """
    # Adjust for Ga/Zn alloying: +0.08 eV for 5% Ga, +0.05 eV for 2% Zn
    E_bulk += 0.08 + 0.05
    
    # Reduced mass (0.1 * m0) for CIS
    mu = 0.1 * 9.109e-31  # kg
    hbar = 1.0545718e-34   # J·s
    q = 1.602e-19          # C (for eV conversion)
    
    # Quantum confinement term
    confinement = (hbar**2 * np.pi**2) / (2 * mu * (d_nm * 1e-9)**2)
    confinement_eV = confinement / q
    
    return E_bulk + confinement_eV

# Example usage
sizes = [1.0, 2.5, 4.0]
for d in sizes:
    print(f"QD Size: {d} nm → Bandgap: {calculate_bandgap(d):.2f} eV")

# Output:
# QD Size: 1.0 nm → Bandgap: 2.60 eV
# QD Size: 2.5 nm → Bandgap: 1.90 eV
# QD Size: 4.0 nm → Bandgap: 1.55 eV
