from collections import defaultdict
from . import constellations
from . import stars as stars_module
from . import coords


def as_graphs(names:str or [str]) -> [str, dict, dict]:
    """Yield (constellation name, graph of structure, mapping star name to object)"""
    if 'example' in names:
        yield from example()
        return
    for constellation, links, stars_id in constellations.by_name(names):
        # get the coords and the names
        stars = {}
        for star in stars_module.stars_from_name(*stars_id):
            stars[star.source] = star
        # create a graph instead of a list of adjacency
        graph = defaultdict(set)
        for pred, succ in links:
            graph[stars[pred]].add(stars[succ])
        stars = {star.name: star for star in stars.values()}
        yield str(constellation), dict(graph), dict(stars)


def example() -> (str, dict, dict):
    def make_star(name, galactic):
        return stars_module.Star(
            name,
            *galactic,
            carthesian=coords.coords_from_long_lat(*galactic),
            source=name,
        )
    dist = 1 / 1000
    stars = {star.name: star for star in (make_star(*p) for p in (
        ('a', (0, 0, dist)),
        ('b', (5, 5, dist)),
        ('c', (0, 10, dist)),
        ('d', (-5, 5, dist)),
    ))}
    graph = {'a': {'b', 'd'}, 'b': {'a', 'c'}, 'c': {'b', 'd'}, 'd': {'a', 'c'}}
    graph = {stars[pred]: {stars[succ] for succ in succs} for pred, succs in graph.items()}
    yield 'example', graph, stars
