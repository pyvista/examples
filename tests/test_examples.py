"""Test examples that do not require downloading."""
import pyvista as pv
from pvexamples import planets


def test_sphere_with_texture_map():
    sphere = planets._sphere_with_texture_map()
    assert isinstance(sphere, pv.PolyData)
    assert 'Texture Coordinates' in sphere.point_data
    assert sphere['Texture Coordinates'].shape == (sphere.n_points, 2)


def test_load_earth():
    mesh = planets.load_earth()
    assert isinstance(mesh, pv.PolyData)
    assert mesh.n_cells
    assert mesh.textures["surface"]
