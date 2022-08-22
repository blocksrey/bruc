#version 130
#extension GL_ARB_explicit_attrib_location:enable
#extension GL_ARB_separate_shader_objects:enable

in vec2 pos1;
layout (location=1) in vec4 col0;
layout (location=0) out vec4 col1;

void main(){
	col1=col0;
}