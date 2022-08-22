#version 130
#extension GL_ARB_explicit_attrib_location:enable
#extension GL_ARB_separate_shader_objects:enable

uniform float camd,time;
uniform vec2 camp,camo,wins;

layout (location=0) in vec2 pos0;
layout (location=3) in vec4 col0;

out vec2 pos1;
layout (location=1) out vec4 col1;

vec2 cmul(vec2 a,vec2 b){
	return vec2(a.x*b.x-a.y*b.y,a.x*b.y+a.y*b.x);
}

void main(){
	gl_Position=vec4(cmul(camo,pos0-camp)*vec2(wins.y/wins.x,1)/camd,0,1);
	pos1=pos0;
	col1=col0;
}