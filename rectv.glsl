#version 130

#extension GL_ARB_explicit_attrib_location : enable
#extension GL_ARB_separate_shader_objects : enable

layout (location = 0) in vec2 pos0;
layout (location = 3) in vec3 col0;

layout (location = 1) out vec3 col1;

uniform vec2 wins;

uniform vec3 camp;
uniform float camo;

void main() {
	mat2 rotm = mat2(
		+cos(camo), -sin(camo),
		+sin(camo), +cos(camo)
	);

	gl_Position = vec4(rotm*(vec2(-1, 2)*(camp.xy - pos0.xy))/(camp.z*wins), 0, 1);

	col1 = col0;
}