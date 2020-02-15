from gl_drawable.drawable_2d.polygon import Polygon
from gl_drawable.drawable_2d.square import Square
from gl_drawable.drawable_3d.cube import Cube
from gl_drawable.drawable_3d.polyhedron import Polyhedron
from gl_drawable.drawable_3d.sphere import UVSphere


def polygon_complexity(polygon: Polygon, percentage: float):
    segments = polygon.segments
    radius = polygon.radius
    axis = polygon.axis
    color = polygon.color

    segments += segments * percentage

    return Polygon(segments=segments, axis=axis, radius=radius, color=color)


def polyhedron_complexity(polyhedron: Polyhedron, percentage: float):
    pass
