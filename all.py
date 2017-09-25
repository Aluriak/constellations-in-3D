"""Aggregation of all submodules.
"""


import argparse
import generate_constellations
import plot3dgraph_gnuplot


def cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('constellation', type=str, nargs='+',
                        default=['cygnus'],
                        help="Name of the constellation to print. Try cygnus, "
                        "cetus, ursa minor, or camelopardalis")
    return parser.parse_args()


def run(constellations:[str]):
    print("Starting.")
    for name, graph, stars in generate_constellations.as_graphs(constellations):
    # for name, graph, stars in generate_constellations.example():
        print("Processing constellation {} ({} stars)…"
              "".format(name.title(), len(stars)), end='', flush=True)
        print('\nGRAPH:', graph, end='\n\n')
        print('STARS:', stars, end='\n\n')
        assert all(node.name in stars for node in graph)
        graph = {
            pred.carthesian: {succ.carthesian for succ in succs}
            for pred, succs in graph.items()
        }
        print("Done !")
        print("Plotting: press enter to stop.", end='', flush=True)
        plot3dgraph_gnuplot.plot(graph)
    print("Finished !")

TARGET = 'Cetus'
TARGET = 'Camelopardalis'
TARGET = 'Cygnus'
TARGET = 'Ursa Minor'

if __name__ == '__main__':
    args = cli()
    run(args.constellation)


