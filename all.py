"""Aggregation of all submodules.
"""


import generate_constellations
import plot3dgraph_gnuplot

TARGET = 'Cetus'
TARGET = 'Ursa Minor'
TARGET = 'Camelopardalis'
TARGET = 'Cygnus'

if __name__ == '__main__':
    print("Starting.")
    for name, graph, stars in generate_constellations.as_graphs(TARGET):
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

