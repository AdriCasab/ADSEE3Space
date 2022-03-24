import math
import numpy



def MarsOrbitalPeriod(altitude):
    Gconst = 6.67430e-11
    MarsMass = 0.64169e24
    MarsRadius = 3396.2 * 1000
    flightRadius = altitude + MarsRadius
    orbitalPeriod= math.sqrt(4*(math.pi**2)*(flightRadius**3)/(Gconst*MarsMass))
    percentageDarkness = (math.pi/2 - math.acos(MarsRadius/flightRadius))/math.pi
    darknessPeriod = orbitalPeriod*percentageDarkness
    return orbitalPeriod, darknessPeriod

def PowerRequirement(powerDay, powerNight, efficiencyDay, efficiencyNight, orbitalPeriod, darknessPeriod):
    brightnessPeriod = orbitalPeriod - darknessPeriod
    powerRequirement = (powerDay*brightnessPeriod/efficiencyDay + powerNight*darknessPeriod/efficiencyNight)/brightnessPeriod
    return powerRequirement



W = 586.2
FlightAltitude = 500*1000
solarPanelEfficiency = 0.20
powerDay = 800
powerNight = 400
efficiencyDay = 0.4
efficiencyNight = 0.3
orbitalPeriod, darknessPeriod = MarsOrbitalPeriod(FlightAltitude)
powerRequirement = PowerRequirement(powerDay, powerNight, efficiencyDay, efficiencyNight, orbitalPeriod, darknessPeriod)
print(powerRequirement)