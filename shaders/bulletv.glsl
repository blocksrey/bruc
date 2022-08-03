#version 130
#extension GL_ARB_explicit_attrib_location : enable
#extension GL_ARB_separate_shader_objects : enable

uniform float camd;
uniform vec2 camp, camo, wins;

layout (location = 0) in vec2 pos0;

vec2 cmul(vec2 a, vec2 b) {
	return vec2(a.x*b.x - a.y*b.y, a.x*b.y + a.y*b.x);
}

void main() {
	gl_Position = vec4(cmul(camo, pos0 - camp)*vec2(wins.y/wins.x, 1)/camd, 0, 1);
}