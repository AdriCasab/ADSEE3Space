import math

W = 586.2
FlightAltitude = 500*1000


def MarsOrbitalPeriod(altitude):
    Gconst = 6.67430e-11
    MarsMass = 0.64169e24
    MarsRadius = 3396.2 * 1000
    flightRadius = altitude + MarsRadius
    orbitalPeriod= math.sqrt(4*(math.pi**2)*(flightRadius**3)/(Gconst*MarsMass))
    return orbitalPeriod


print(MarsOrbitalPeriod(FlightAltitude))