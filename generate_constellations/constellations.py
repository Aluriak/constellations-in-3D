"""Definitions of constellations,
using Stellarium files.

"""
import csv
from itertools import zip_longest, chain


CONSTELLATIONS_STARS = 'data/constellation.dat'
CONSTELLATIONS_NAMES = 'data/constellation_names.dat'


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def constellations_links(fname:str=CONSTELLATIONS_STARS) -> [(str, {tuple})]:
    """Yield (constellation id, links) found in given file.
    """
    with open(fname) as fd:
        for line in fd:
            line = line.split()
            if not line: return
            id_, nb_link, *links = line
            hip_links = ('HIP ' + link for link in links)
            links = frozenset(map(tuple, grouper(hip_links, 2)))
            assert len(links) == int(nb_link), "{} != {}, which is unexpected".format(len(links), nb_link)
            yield id_, links


def constellations_names(fname:str=CONSTELLATIONS_NAMES) -> [(str, str)]:
    """Yield (constellation id, constellation name) found in given file.
    """
    with open(fname) as fd:
        reader = csv.reader(fd, delimiter='\t')
        for line in reader:
            id_, name, *_ = line
            yield id_, name


def by_name(*names:str) -> (str, frozenset, frozenset):
    """Return (constellation name, links between stars, stars id)"""
    names = frozenset(map(str.lower, names))
    ids = dict(constellations_names())
    if not set(map(str.lower, ids.values())) & set(names):
        print('WARNING: given names ({}) do not exists. Full list: {}.'.format(
            ', '.join(names), ', '.join(ids.values())
        ))
    # print(ids)
    cons = ((ids[id_].strip('"').lower(), link) for id_, link in constellations_links())
    yield from (
        (id_, link, frozenset(chain.from_iterable(link)))
        for id_, link in cons
        if (names and id_ in names) or not names
    )


if __name__ == "__main__":
    print(dict(by_name()))
