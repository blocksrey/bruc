from vec3 import vec3
from pyglet.graphics import draw
from pyglet.gl import GL_TRIANGLES

# p0 + (tx, ty)*s : 0 <= tx < 1 && 0 <= ty < 1
def draw_rect(p0, s, c):
	p1 = p0 + s
	c *= vec3(255, 255, 255)
	draw(
		6,
		GL_TRIANGLES,
		("v2i", (
			p0.x, p0.y,
			p1.x, p1.y,
			   0, p1.y,
			p0.x, p0.y,
			p1.x, p1.y,
			p1.x,    0
		)),
		("c3B", (
			c.x, c.y, c.z,
			c.x, c.y, c.z,
			c.x, c.y, c.z,
			c.x, c.y, c.z,
			c.x, c.y, c.z,
			c.x, c.y, c.z
		))
	)