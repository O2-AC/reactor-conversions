# reaction 2nd order
# k: 1
# fixed conversions in first reactor
# therefore: given residence times for first reactors useless
# if Conversions are not fixed for first reactor PFR -> CSTR will lead to higher conversions
import numpy as np

k = 1
cA0 = 1
n = 1

t1 = 100 # first reactor
t2 = n * t1 # second reactor
cAi1 = 0.5 # (np.sqrt(1 + 4 * t1 * k * cA0) - 1)/(2 * t1 * k)
convint1 = ((1-cAi1)/1)*100
cA1 = (1)/((1/cAi1) + t2 * k)
conversion1 = ((1-cA1)/1)*100
cAi2 = 0.5 # (1)/((1/cA0) + t1 * k)
convint2 = ((1-cAi2)/1)*100
cA2 = (np.sqrt(1 + 4 * t2 * k * cAi2) - 1)/(2 * t2 * k)
conversion2 = ((1-cA2)/1)*100
print("-----\nCSTR -> PFR\n-----")
print("residence time CSTR: {}".format(t1))
print("residence time PFR: {}".format(t2))
print("concentration after CSTR: {}".format(round(cAi1, 2)))
print("conversion in CSTR: {}".format(round(convint1, 2)))
print("concentration after PFR: {}".format(round(cA1, 2)))
print("conversion in PFR: {}".format(round(conversion1-convint1, 2)))
print("overall conversion: {}".format(round(conversion1, 2)))
print("-----\nPFR -> CSTR\n-----")
print("residence time CSTR: {}".format(t2))
print("residence time PFR: {}".format(t1))
print("concentration after PFR: {}".format(round(cAi2, 2)))
print("conversion in PFR: {}".format(round(convint2, 2)))
print("concentration after CSTR: {}".format(round(cA2, 2)))
print("conversion in CSTR: {}".format(round(conversion2-convint2, 2)))
print("overall conversion: {}".format(round(conversion2, 2)))
