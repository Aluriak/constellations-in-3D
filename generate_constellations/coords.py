"""Attempt to compute 3D coordinates of objects
given their longitude and lattitude in galactic coordinates.

The SIMBAD database is used as reference for objects coordinates.
For instance, for tau ceti: http://simbad.u-strasbg.fr/simbad/sim-id?Ident=LHS+146

"""
import math
import pprint


MAX_DIST_ERROR = 2
OBJECTS = {
    # galactic coordinates and parallaxe value (in milliarcsecond)
    'tau ceti': (173.1007, -73.4397, 273.96),
}


def simbad_unit_to_radians(x):
    return math.radians(x)


def coords_from_long_lat(longitude:float, lattitude:float,
                         parallaxe:float) -> (float, float, float):
    """

    longitude -- longitude in `SIMBAD unit (degree probably)`
    lattitude -- lattitude in `SIMBAD unit (degree probably)`
    parallaxe -- parallaxe in milliarcsecond

    """
    # relations du to definitions of parallaxe itself
    parallaxe_arcsecond = parallaxe / 1000
    parsec = 1 / parallaxe_arcsecond

    # unleash the power of geometry
    lattitude, longitude = simbad_unit_to_radians(lattitude), simbad_unit_to_radians(longitude)

    z = parsec * math.sin(lattitude)
    p = parsec * math.cos(lattitude)
    y = p * math.sin(longitude)
    x = p * math.cos(longitude)

    # difference between computed distance and parallaxe predicted distance
    distance_by_xyz = math.sqrt(x**2 + y**2 + z**2)
    dist_error = abs(round(distance_by_xyz / parsec, 2))
    if dist_error > MAX_DIST_ERROR:
        print('ERROR: {}%'.format(dist_error))

    # ready to be put into a 3D env
    return x, y, z


def coords_3D(objects:dict) -> dict:
    """Return a {object: (x, y, z)} mapping.

    objects -- a mapping {object: (longiture, lattitude, parallaxe)}

    longitude and lattitude must be in `SIMBAD unit (degree probably)`
    parallaxe must be in milliarcsecond.

    """
    return {
        obj: coords_from_long_lat(*gal_coords)
        for obj, gal_coords in OBJECTS.items()
    }


if __name__ == "__main__":
    print(coords_3D(OBJECTS))
