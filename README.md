# Conversions in reactor cascades
## Description of the problem
It is asked which reactor configuration of a PFR and CSTR can yield the highest conversions. Although it has been thought that a cascade of CSTR -> PFR should yield higher conversions, based on the higher mean educt concentration in a PFR compared to a CSTR. First calculations did not confirm this thought.

## How to solve the problem
By calculating the respective conversions of the different combinations for different reaction orders a final conclusion should be drawn.
The developed program should be able to suit different reactor volumes and rate constants. It should return based on the different input parameters which reactor combination yields the higher conversion.

## The math
### Conversion
![conversion](https://www.zahlen-kern.de/editor/equations/hvot.png)
### First order reaction kinetics
#### PFR
![1st order PFR](https://www.zahlen-kern.de/editor/equations/hvod.png)
integrates to: ![1st order PFR int](https://www.zahlen-kern.de/editor/equations/hvom.png)

#### CSTR
![1st order CSTR int](https://www.zahlen-kern.de/editor/equations/hvon.png)

### Second order reaction kinetics
#### PFR
![2nd order PFR int](https://www.zahlen-kern.de/editor/equations/hwcv.png)

#### CSTR
![2nd order CSTR int](https://www.zahlen-kern.de/editor/equations/hwcw.png)

## The WebApp
The WebApp shall ask the user for inputs of start concentration, reaction order, reaction rate and residence times.
Instead of asking for residence times there shall be the possibility to enter reactor volumes and flow rates.
Steady state operations of ideal reactors  will be assumed for calculations.
The WebApp should return the conversions of the different reactor combinations in a bar plot.
