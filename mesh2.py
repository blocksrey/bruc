from vec2 import Vec2
from math import inf

class Mesh2:
	def __init__(mesh2, *vertices):
		mesh2.vertices = vertices
		mesh2._sort()

	def _sort(mesh2):
		pass

	# this is kinda trash but whatever
	def build_rays(mesh2):
		rays = []

		vert_count = len(mesh2.vertices)

		for index in range(vert_count - 1):
			va = mesh2.vertices[index + 0]
			vb = mesh2.vertices[index + 1]

			rays.append((va, vb - va, abs(vb - va)))

		return rays

	def get_aabb(mesh2):
		ux, uy = -inf, -inf
		lx, ly = +inf, +inf

		for vertex in mesh2.vertices:
			vx, vy = vertex.x, vertex.y

			ux, uy = max(ux, vy), max(uy, vy)
			lx, ly = min(lx, vy), min(ly, vy)

		return Vec2(ux, uy), Vec2(lx, ly)