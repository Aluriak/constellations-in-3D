
import math
from . import coords


def test_simple():
    ROUND = 4
    rounded = lambda x, y, z: (round(x, ROUND), round(y, ROUND), round(z, ROUND))
    func = coords.coords_from_long_lat
    assert rounded(*func(0, 0, 100)) == rounded(10, 0, 0)
    assert rounded(*func(90, 0, 100)) == rounded(0, 10, 0)
    assert rounded(*func(-90, 0, 100)) == rounded(0, -10, 0)
    assert rounded(*func(0, 90, 100)) == rounded(0, 0, 10)
    assert rounded(*func(0, -90, 100)) == rounded(0, 0, -10)
    assert rounded(*func(180, 0, 100)) == rounded(-10, 0, 0)
    assert rounded(*func(45, 0, 1000)) == rounded(math.sin(math.radians(45)), math.cos(math.radians(45)), 0)


def test_double_rotation():
    ROUND = 4
    rounded = lambda x, y, z: (round(x, ROUND), round(y, ROUND), round(z, ROUND))
    func = coords.coords_from_long_lat
    assert rounded(*func(90, 90, 100)) == rounded(0, 0, 10)
