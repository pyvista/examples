"""
Test downloading files.
"""
import os
import warnings
import numpy as np
import pytest

import pyvista as pv
from pyvista import examples



def test_load_sun():
    mesh = examples.planets.load_sun()
    assert mesh.n_cells
    assert mesh.textures["atmosphere"]


def test_load_moon():
    mesh = examples.planets.load_moon()
    assert mesh.n_cells
    assert mesh.textures["surface"]


def test_load_mercury():
    mesh = examples.planets.load_mercury()
    assert mesh.n_cells
    assert mesh.textures["surface"]


def test_load_venus():
    mesh = examples.planets.load_venus()
    assert mesh.n_cells
    assert mesh.textures["surface"]
    assert mesh.textures["atmosphere"]


def test_load_mars():
    mesh = examples.planets.load_mars()
    assert mesh.n_cells
    assert mesh.textures["surface"]


def test_load_jupiter():
    mesh = examples.planets.load_jupiter()
    assert mesh.n_cells
    assert mesh.textures["atmosphere"]


def test_load_saturn():
    mesh = examples.planets.load_saturn()
    assert mesh.n_cells
    assert mesh.textures["atmosphere"]


def test_load_saturn_rings():
    mesh = examples.planets.load_saturn_rings()
    assert mesh.n_cells
    assert mesh.textures["atmosphere"]


def test_load_uranus():
    mesh = examples.planets.load_uranus()
    assert mesh.n_cells
    assert mesh.textures["atmosphere"]


def test_load_neptune():
    mesh = examples.planets.load_neptune()
    assert mesh.n_cells
    assert mesh.textures["atmosphere"]


def test_load_pluto():
    mesh = examples.planets.load_pluto()
    assert mesh.n_cells
    assert mesh.textures["surface"]
