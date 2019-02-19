import pytest

import numpy as np

from capytaine.mesh.mesh import Mesh
from capytaine.mesh.meshes_collection import CollectionOfMeshes
from capytaine.mesh.symmetries import TranslationalSymmetry, ReflectionSymmetry

from capytaine.bodies.predefined.rectangle import Rectangle, OpenRectangularParallelepiped, RectangularParallelepiped
from capytaine.bodies.predefined.cylinder import Disk, HorizontalCylinder, VerticalCylinder


def test_rectangle_generation():
    # Rejects invalid inputs:
    with pytest.raises(AssertionError):
        Rectangle(size=(5.0, 6.0, 7.0))

    with pytest.raises(AssertionError):
        Rectangle(size=(-4, 5))

    with pytest.raises(AssertionError):
        Rectangle(resolution=(4.1, 5))

    with pytest.raises(ValueError):
        Rectangle(resolution=(3, 3), reflection_symmetry=True)

    # Test mesh with symmetry
    rec = Rectangle(size=(10, 10), resolution=(6, 2),
                    reflection_symmetry=False, translational_symmetry=False,
                    center=(0, 0, -5), name="test")

    assert rec.name == "test"
    assert isinstance(rec.mesh, Mesh)
    assert rec.mesh.name == "test_mesh"
    assert all(rec.size == [10.0, 10.0])
    assert all(rec.center == [0, 0, -5.0])
    assert rec.mesh.nb_faces == 12
    assert rec.mesh.nb_vertices == 21
    assert rec.area == 100

    # x coordinate
    assert np.all(rec.mesh.vertices[:, 0] == 0.0)

    # y coordinate
    assert np.all(rec.mesh.vertices[:, 1] <= 5.0)
    assert np.all(rec.mesh.vertices[:, 1] >= -5.0)

    # z coordinate
    assert np.all(rec.mesh.vertices[:, 2] <= 0.0)
    assert np.all(rec.mesh.vertices[:, 2] >= -10.0)

    # Test mesh with reflection symmetry
    sym_rec = Rectangle(size=(10, 10), resolution=(6, 2),
                        translational_symmetry=False, reflection_symmetry=True,
                        center=(0, 0, -5))
    assert isinstance(sym_rec.mesh, ReflectionSymmetry)
    assert sym_rec.mesh.nb_submeshes == 2
    assert sym_rec.mesh.nb_faces == 12

    sym_rec_merged_mesh = sym_rec.mesh.merged()
    assert isinstance(sym_rec_merged_mesh, Mesh)
    # assert sym_rec_merged_mesh == rec.mesh

    # Test mesh with translation symmetry
    trans_rec = Rectangle(size=(10, 10), resolution=(6, 2),
                          translational_symmetry=True, reflection_symmetry=False,
                          center=(0, 0, -5))
    assert isinstance(trans_rec.mesh, TranslationalSymmetry)
    assert trans_rec.mesh.nb_submeshes == 6
    assert trans_rec.mesh.nb_faces == 12

    trans_rec_merged_mesh = trans_rec.mesh.merged()
    assert isinstance(trans_rec_merged_mesh, Mesh)
    # assert trans_rec_merged_mesh == rec.mesh


def test_open_parallelepiped_generation():
    para = OpenRectangularParallelepiped(size=(5.0, 1.0, 3.0), center=(0, 0, -1.5),
                                         resolution=(5, 2, 3),
                                         translational_symmetry=False, name="test")
    assert para.name == "test"
    assert isinstance(para.mesh, Mesh)
    assert para.mesh.name == "test_mesh"
    assert para.mesh.nb_faces == 42

    assert np.isclose(np.abs(para.mesh.vertices[:, 0]).max(), 2.5)
    assert np.isclose(np.abs(para.mesh.vertices[:, 1]).max(), 0.5)
    assert np.all(para.mesh.vertices[:, 2] <= 0.0)
    assert np.all(para.mesh.vertices[:, 2] >= -3.0)

    clever_para = OpenRectangularParallelepiped(size=(5.0, 1.0, 3.0), center=(0, 0, -1.5),
                                                resolution=(5, 2, 3),
                                                translational_symmetry=True, name="clever_test")

    assert clever_para.mesh.nb_faces == 42
    assert isinstance(clever_para.mesh, CollectionOfMeshes)
    assert any(isinstance(submesh, TranslationalSymmetry) for submesh in clever_para.mesh)


def test_parallelepiped_generation():
    full_para = RectangularParallelepiped(size=(5.0, 1.0, 3.0), center=(0, 0, -1.5),
                                          resolution=(6, 2, 3),
                                          translational_symmetry=False, name="full_test")
    assert full_para.mesh.nb_faces == 72
    # full_para.show()

    sym_para = RectangularParallelepiped(size=(5.0, 1.0, 3.0), center=(0, 0, -1.5),
                                         resolution=(6, 2, 3),
                                         reflection_symmetry=True, name="sym_full_test")
    assert sym_para.mesh.nb_faces == 72
    # sym_para.show()

    trans_para = RectangularParallelepiped(size=(5.0, 1.0, 3.0), center=(0, 0, -1.5),
                                           resolution=(6, 2, 3),
                                           translational_symmetry=True, name="trans_full_test")
    assert trans_para.mesh.nb_faces == 72
    # trans_para.show()


def test_disk():
    a = Disk(resolution=(6, 6))
    b = Disk(resolution=(6, 6), axial_symmetry=True)
    # print(b.mesh.tree_view())
    c = Disk(resolution=(6, 6), reflection_symmetry=True)
    # TODO

def test_cylinder():
    HorizontalCylinder()
    VerticalCylinder()
    # TODO
