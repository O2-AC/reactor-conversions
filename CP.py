# reaction first order
import numpy as np

cA0 = 1
k = 1
tPFR = 10
tCSTR = 1

# CSTR -> PFR
print("----\nCSTR-PFR\n----")
# concentration behind CSTR
cAi = cA0/(k * tCSTR + 1)
convint = ((1-cAi)/cA0) * 100
print("conversion CSTR: {}".format(round(convint, 2)))
# concentration behind PFR
cA1 = cAi * np.exp(-k * tPFR)
conversion = ((1-cA1)/cA0)*100
print("conversion PFR: {}".format(round(conversion - convint, 2)))
print("conversion: {}".format(round(conversion, 2)))
# PFR -> CSTR
print("----\nPFR-CSTR\n----")
# concentration behind PFR
cAi = cA0 * np.exp(-k *tPFR)
convint = ((1-cAi)/cA0) *100
print("conversion PFR: {}".format(round(convint, 2)))

# concentration behind CSTR
cA2 = cAi/(k * tCSTR + 1)
conversion = ((1-cA1)/cA0)*100
print("conversion CSTR: {}".format(round(conversion - convint, 2)))
print("conversion: {}".format(round(conversion, 2)))
