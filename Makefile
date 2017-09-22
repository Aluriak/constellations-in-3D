
PLOT_METHOD=gnuplot

.PHONY: generate_constellations constellations stars tests

all:
	python all.py

generate_constellations:
	python -m generate_constellations

plot_constellations:
	$(MAKE) plot_constellations_$(PLOT_METHOD)
plot_constellations_gnuplot:
	python -m plot_constellations_$(PLOT_METHOD)


t: tests
tests:
	python -m pytest */test_*.py -vv


retrieve_stellarium_data: data/constellation.dat data/constellation_names.dat
	curl https://raw.githubusercontent.com/Stellarium/stellarium/master/skycultures/western/constellationship.fab > data/constellation.dat
	curl https://raw.githubusercontent.com/Stellarium/stellarium/master/skycultures/western/constellation_names.eng.fab > data/constellation_names.dat
