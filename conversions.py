import numpy as np
import cs50

print("Calculating conversions for CSTR and PFR combinations.")
tCSTR = cs50.get_int("Provide residence time for the CSTR: ")
tPFR = cs50.get_int("Provide residence time for the PFR: ")
k = 0.00015 # cs50.get_int("Provide rate constant: ")
print("Assuming an initial concentration of 0.010 mol/L")
cA0 = 1
# First order
# CSTR -> PFR
# concentration behind CSTR
cAi = cA0/(k * tCSTR + 1)
# concentration behind PFR
cA = cAi * np.exp(-k * tPFR)
conversion1 = ((cA0-cA)/cA0)*100

# PFR -> CSTR
# concentration behind PFR
cAi = cA0 * np.exp(-k *tPFR)
# concentration behind CSTR
cA = cAi/(k * tCSTR + 1)
conversion2 = ((cA0-cA)/cA0)*100

# Second order
# CSTR -> PFR
# concentration behind CSTR
cAi = (np.sqrt(1 + 4 * tCSTR * k * cA0) - 1)/(2 * tCSTR * k)
# concentration behind PFR
cA = (1)/((1/cAi) + tPFR * k)
conversion3 = ((cA0-cA)/cA0)*100

# PFR -> CSTR
# concentration behind PFR
cAi = (1)/((1/cA0) + tPFR * k)
# concentration behind CSTR
cA = (np.sqrt(1 + 4 * tCSTR * k * cAi) - 1)/(2 * tCSTR * k)
conversion4 = ((cA0-cA)/cA0)*100

# Printing results
print("######\nFirst order reaction\n######")
print("CSTR -> PFR: Conversion: {}".format(round(conversion1, 2)))
print("PFR -> CSTR: Conversion: {}".format(round(conversion2, 2)))
print("######\nSecond order reaction\n######")
print("CSTR -> PFR: Conversion: {}".format(round(conversion3, 2)))
print("PFR -> CSTR: Conversion: {}".format(round(conversion4, 2)))
