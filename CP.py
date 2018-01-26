from __future__ import division
import numpy as np

cA0 = 1
k = 0.2
tPFR = 1
tCSTR = 10

# CSTR -> PFR
print("----\nCSTR-PFR\n----")
# concentration behind CSTR
cAi = cA0/(k * tCSTR + 1)
convint = ((1-cAi)/cA0) * 100
print("conversion CSTR: {}".format(convint))
# concentration behind PFR
cA1 = cAi * np.exp(-k * tPFR)
conversion = ((1-cA1)/cA0)*100
print("conversion PFR: {}".format(conversion - convint))
print("conversion: {}".format(conversion))
# PFR -> CSTR
print("----\nPFR-CSTR\n----")
# concentration behind PFR
cAi = cA0 * np.exp(-k *tPFR)
convint = ((1-cAi)/cA0) *100
print("conversion PFR: {}".format(convint))

# concentration behind CSTR
cA2 = cAi/(k * tCSTR + 1)
conversion = ((1-cA1)/cA0)*100
print("conversion CSTR: {}".format(conversion - convint))
print("conversion: {}".format(conversion))