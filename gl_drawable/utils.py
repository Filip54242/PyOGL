from gl_drawable.drawable_2d.polygon import Polygon
from gl_drawable.drawable_2d.square import Square
from gl_drawable.drawable_3d.cube import Cube
from gl_drawable.drawable_3d.polyhedron import Polyhedron
from gl_drawable.drawable_3d.sphere import UVSphere


def square_complexity(square: Square, percentage: float):
    return square


def cube_complexity(cube: Cube, percentage: float):
    return cube


def polygon_complexity(polygon: Polygon, percentage: float):
    segments = polygon.segments
    radius = polygon.radius
    axis = polygon.axis
    color = polygon.color

    segments += int(segments * percentage)

    return Polygon(segments=segments, axis=axis, radius=radius, color=color)


def polyhedron_complexity(polyhedron: Polyhedron, percentage: float):
    segments = polyhedron.segments
    radius = polyhedron.radius
    color = polyhedron.color

    segments += int(segments * percentage)
    return Polyhedron(segments=segments, radius=radius, color=color)


def sphere_complexity(sphere: UVSphere, percentage: float):
    segments = sphere.segments
    radius = sphere.radius
    color = sphere.color
    rings = sphere.no_rings

    segments += int(segments * percentage)
    rings += int(rings * percentage)

    return UVSphere(segments=segments, rings=rings, color=color, radius=radius)
