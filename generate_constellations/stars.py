"""Query and retrieve stars informations
from SIMBAD database.

"""

from astroquery.simbad import Simbad
from collections import namedtuple
from . import coords


Star = namedtuple('Star', 'name, longitude, lattitude, parallax, carthesian, source')


def stars_from_name(*names:str, handler:Simbad=None) -> [Star]:
    """Yield Star instance for each given name.
    """
    if not handler:
        handler = Simbad()
        # print('FIELDS:', handler.get_votable_fields())
        # print('ADD FIELDS…')
        handler.remove_votable_fields('coordinates')
        handler.add_votable_fields('parallax')
        handler.add_votable_fields('ra(d;A;GAL;J2000;2000)')
        handler.add_votable_fields('dec(d;D;GAL;J2000;2000)')
        # print('FIELDS:', handler.get_votable_fields())

    for name in names:
        result_table = handler.query_object(name)
        if not result_table:
            print(f'ERROR: query for {name} failed by returing {result_table}')
        if len(result_table) != 1:
            print(f'ERROR: id {name} is associated with {len(result_table)} objects in SIMBAD db.')
            return
        for entry in result_table:
            # print(entry)
            # for col in entry.colnames:
                # print('\t', col, entry[col])
            # print(entry.colnames)
            # print(entry.columns)
            galactic = entry['RA_d_A_GAL_J2000_2000'], entry['DEC_d_D_GAL_J2000_2000'], entry['PLX_VALUE']
            yield Star(
                entry['MAIN_ID'],
                *galactic,
                carthesian=coords.coords_from_long_lat(*galactic),
                source=name,
            )


if __name__ == "__main__":
    print(dict(stars_from_name('tau cet', 'HIP 98036')))
