#version 130
#extension GL_ARB_explicit_attrib_location : enable
#extension GL_ARB_separate_shader_objects : enable

layout (location = 0) in vec2 pos0;

uniform vec2 wins;

uniform vec3 camp;
uniform float camo;

mat2 rotm = mat2(
	+cos(camo), +sin(camo),
	-sin(camo), +cos(camo)
);

void main() {
	gl_Position = vec4(rotm*(camp.xy - pos0.xy)*vec2(-wins.y/wins.x, 1)/camp.z, 0, 1);
}