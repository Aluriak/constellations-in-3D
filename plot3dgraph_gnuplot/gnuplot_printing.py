import subprocess
import clyngor


OUTPUT_DATA_FILE = 'output/constellation.dat'
ASP_SOURCE_CODE = 'plot3dgraph_gnuplot/search_whole_path.lp'


def to_dat(points:iter, fname:str=OUTPUT_DATA_FILE):
    with open(fname, 'w') as fd:
        for point in points:
            fd.write(' '.join(map(str, point)) + '\n')


def walk_by_all_edges(graph:dict) -> iter:
    """Yield nodes to visit in order.

    This call ASP for resolution.

    """
    data = '.'.join('edge("{}","{}")'.format(pred, succ)
                    for pred, succs in graph.items()
                    for succ in succs) + '.'
    assert len(data) > 1
    for answer in clyngor.solve(ASP_SOURCE_CODE, inline=data).by_predicate.careful_parsing:
        pass
    # print(sorted(answer['goto'], key=lambda x: x[0]))
    yield from (n.strip('"') for _, n in sorted(answer['goto'], key=lambda x: x[0]))


def call_gnuplot(data_file:str=OUTPUT_DATA_FILE, gnuplot_bin:str='gnuplot'):
    command = [gnuplot_bin, '-e', 'splot "{}" w lp ps 1 ; pause -1'.format(data_file)]
    # print('COMMAND:', command)
    # print('COMMAND:', ' '.join(command))
    process = subprocess.Popen(command)
    process.wait()


def plot(graph:dict, fname:str=OUTPUT_DATA_FILE):
    """Build the data file, then call gnuplot on it"""
    writable = lambda s: s.strip('()').replace(',', '').split(' ')
    to_dat(map(writable, walk_by_all_edges(graph)), fname=fname)
    call_gnuplot()



if __name__ == "__main__":
    COORDS = {
        'a': (0, 0, 0),
        'b': (0, 4, 0),
        'c': (2, 2, 1),
        'd': (3, 1, 0),
        'e': (5, -1, 0),
    }

    GRAPH = {
        'a': {'b', 'd'},
        'b': {'a', 'c'},
        'c': {'b', 'd'},
        'd': {'a', 'c', 'e'},
        'e': {'d'},
    }
    to_dat(map(COORDS.__getitem__, walk_by_all_edges(GRAPH)))
    call_gnuplot()


    GRAPH = {
        (0, 0, 0): {(0, 4, 0)},
        (0, 4, 0): {(2, 2, 0)},
        (2, 2, 0): {(3, 1, 0)},
        (3, 1, 0): {(5, -1, 0)},
    }
    print_graph(GRAPH)
