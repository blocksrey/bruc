from vec2 import Vec2
from ray2 import Ray2
from math import inf, atan2
from sorter import Sorter


class Mesh2:
	def __init__(mesh2, vertices):
		mesh2.sorter = Sorter()
		mesh2.update_vertices(vertices)

	def get_centroid(mesh2):
		s = Vec2(0, 0)

		for v in mesh2.vertices:
			s += v

		return s/len(mesh2.vertices)

	def build_rays(mesh2):
		mesh2.rays = ()

		n = len(mesh2.vertices)

		for i in range(n):
			va = mesh2.vertices[i]
			vb = mesh2.vertices[(i + 1)%n]

			mesh2.rays += (Ray2(va, vb - va), )

	def update_vertices(mesh2, vertices):
		mesh2.vertices = vertices

		c = mesh2.get_centroid() # pivot

		for v in mesh2.vertices:
			mesh2.sorter.set(atan2(v.y - c.y, v.x - c.x), v)

		mesh2.vertices = mesh2.sorter.sorted

		mesh2.build_rays()

	def get_aabb(mesh2):
		ux, uy = -inf, -inf
		lx, ly = +inf, +inf

		for v in mesh2.rays:
			vx, vy = v.o.x, v.o.y

			ux, uy = max(ux, vy), max(uy, vy)
			lx, ly = min(lx, vy), min(ly, vy)

		return Vec2(ux, uy), Vec2(lx, ly)

	def project_ray(mesh2, ray2):
		z = inf

		for ray2i in mesh2.rays:
			if proj := ray2.project_ray(ray2i):
				z = min(z, proj)

		return z