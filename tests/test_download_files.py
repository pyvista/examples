"""
Test downloading files.
"""
from pvexamples import planets


def test_load_sun():
    mesh = planets.load_sun()
    assert mesh.n_cells
    assert mesh.textures["atmosphere"]


def test_load_moon():
    mesh = planets.load_moon()
    assert mesh.n_cells
    assert mesh.textures["surface"]


def test_load_mercury():
    mesh = planets.load_mercury()
    assert mesh.n_cells
    assert mesh.textures["surface"]


def test_load_venus():
    mesh = planets.load_venus()
    assert mesh.n_cells
    assert mesh.textures["surface"]
    assert mesh.textures["atmosphere"]


def test_load_mars():
    mesh = planets.load_mars()
    assert mesh.n_cells
    assert mesh.textures["surface"]


def test_load_jupiter():
    mesh = planets.load_jupiter()
    assert mesh.n_cells
    assert mesh.textures["atmosphere"]


def test_load_saturn():
    mesh = planets.load_saturn()
    assert mesh.n_cells
    assert mesh.textures["atmosphere"]


def test_load_saturn_rings():
    mesh = planets.load_saturn_rings()
    assert mesh.n_cells
    assert mesh.textures["atmosphere"]


def test_load_uranus():
    mesh = planets.load_uranus()
    assert mesh.n_cells
    assert mesh.textures["atmosphere"]


def test_load_neptune():
    mesh = planets.load_neptune()
    assert mesh.n_cells
    assert mesh.textures["atmosphere"]


def test_load_pluto():
    mesh = planets.load_pluto()
    assert mesh.n_cells
    assert mesh.textures["surface"]
