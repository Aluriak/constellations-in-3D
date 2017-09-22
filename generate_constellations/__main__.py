"""Aggregation of all other treatments.

"""
from . import constellations
from . import stars
from . import coords


if __name__ == "__main__":
    for constellation, links, stars_id in constellations.by_name('Camelopardalis'):
    # for constellation, links, stars_id in constellations.by_name('Cetus'):
        for name, *place, carthesian, id_ in stars.stars_from_name(*stars_id):
            # print(name, place)
            print(id_, name, carthesian, '\t', place)

