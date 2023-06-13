"""Test examples that do not require downloading."""
import numpy as np
import pytest

import pyvista as pv
from pyvista import examples
from pyvista.core.errors import PyVistaDeprecationWarning


def test_sphere_with_texture_map():
    sphere = pv.examples.planets._sphere_with_texture_map()
    assert isinstance(sphere, pv.PolyData)
    assert 'Texture Coordinates' in sphere.point_data
    assert sphere['Texture Coordinates'].shape == (sphere.n_points, 2)


def test_load_earth():
    mesh = pv.examples.planets.load_earth()
    assert isinstance(mesh, pv.PolyData)
    assert mesh.n_cells
    with pytest.warns(PyVistaDeprecationWarning):
        assert mesh.textures["surface"]
