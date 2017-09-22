from collections import defaultdict
from . import constellations
from . import stars as stars_module
from . import coords


def as_graphs(names:str or [str]) -> [str, dict, dict]:
    """Yield (constellation name, graph of structure, mapping star name to object)"""
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
