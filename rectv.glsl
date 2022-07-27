#version 130

#extension GL_ARB_explicit_attrib_location : enable
#extension GL_ARB_separate_shader_objects : enable

layout (location = 0) in vec2 pos0;
layout (location = 1) in vec3 col0;

layout (location = 1) out vec3 col1;

void main() {
	gl_Position = vec4(pos0.xy, 0, 1);
	col1 = col0;
}