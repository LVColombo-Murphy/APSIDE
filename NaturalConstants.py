#Module with all constants we might or might not need plus some small routines
from numpy import pi
HBARC = 137.035999084  # MeV fm
HBARC3 = HBARC**3
HBARC4 = HBARC3*HBARC
PI2   = pi*pi

GConst = 6.67430e-11 # m3 kg–1 s–2
SoL    = 299792458.0 # m/s
SoL2   = SoL**2      # (m/s)^2
MSun   = 1.9891e+30  # kg

# Unit Conversion
JouleToMeV = 6.241457006000e12                  #   J -> MeV
ErgToMeV   = 624150.64799632                    # erg -> MeV
JouleToErg = JouleToMeV/ErgToMeV                #   J -> erg
mTofm      = 1.0e15                             #   m -> fm
# remember: 1 dyne = 1 erg/cm
DyneCM2ToMeVfm3 = ErgToMeV/((0.01*mTofm)**3)

MeVfm3ToErgcm3 = 1/ErgToMeV * 1/(1e-13)**3


# Needed for TOV explicitely
RSSSun = 2*GConst*MSun/SoL2  # m Schwarzschild Radius of the Sun
EDensityRenorm       = (MSun*SoL2)/(4*pi*RSSSun**3)    # J/m3
EDensityRenormMeVfm3 = EDensityRenorm*JouleToMeV/mTofm**3  # MeV/fm3


#CGS TOV Conversions

