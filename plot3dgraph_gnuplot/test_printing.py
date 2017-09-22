
from . import gnuplot_printing


def test_linear():
    GRAPH = {
        'a': {'b'},
        'b': {'c'},
        'c': {'d'},
        'd': {'e'},
    }
    order = ''.join(gnuplot_printing.walk_by_all_edges(GRAPH))
    assert order in {'abcde', 'edcba'}


def test_weird_node_name():
    GRAPH = {
        (0, 0, 0): {(0, 4, 0)},
        (0, 4, 0): {(2, 2, 0)},
        (2, 2, 0): {(3, 1, 0)},
        (3, 1, 0): {(5, -1, 0)},
    }
    tuple(gnuplot_printing.walk_by_all_edges(GRAPH))  # do not raise errors


def test_cycle_eulerian():
    GRAPH = {
        'a': {'b', 'd'},
        'b': {'a', 'c'},
        'c': {'b', 'd'},
        'd': {'a', 'c', 'e'},
        'e': {'d'},
    }
    order = ''.join(gnuplot_printing.walk_by_all_edges(GRAPH))
    assert order in {'dcbade', 'dabcde', 'edcbad', 'edabcd'}
