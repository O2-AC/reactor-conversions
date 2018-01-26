# reaction 2nd order
import numpy as np

k = 10
cA0 = 1
n = 0.1

tCSTR = 1 # first reactor
tPFR = n * tCSTR # second reactor
cAi1 = (np.sqrt(1 + 4 * tCSTR * k * cA0) - 1)/(2 * tCSTR * k)
convint1 = ((1-cAi1)/1)*100
cA1 = (1)/((1/cAi1) + tPFR * k)
conversion1 = ((1-cA1)/1)*100
cAi2 = (1)/((1/cA0) + tPFR * k)
convint2 = ((1-cAi2)/1)*100
cA2 = (np.sqrt(1 + 4 * tCSTR * k * cAi2) - 1)/(2 * tCSTR * k)
conversion2 = ((1-cA2)/1)*100
print("-----\nCSTR -> PFR\n-----")
print("residence time CSTR: {}".format(tCSTR))
print("residence time PFR: {}".format(tPFR))
print("concentration after CSTR: {}".format(round(cAi1, 2)))
print("conversion in CSTR: {}".format(round(convint1, 2)))
print("concentration after PFR: {}".format(round(cA1, 2)))
print("conversion in PFR: {}".format(round(conversion1-convint1, 2)))
print("overall conversion: {}".format(round(conversion1, 2)))
print("-----\nPFR -> CSTR\n-----")
print("residence time CSTR: {}".format(tCSTR))
print("residence time PFR: {}".format(tPFR))
print("concentration after PFR: {}".format(round(cAi2, 2)))
print("conversion in PFR: {}".format(round(convint2, 2)))
print("concentration after CSTR: {}".format(round(cA2, 2)))
print("conversion in CSTR: {}".format(round(conversion2-convint2, 2)))
print("overall conversion: {}".format(round(conversion2, 2)))
