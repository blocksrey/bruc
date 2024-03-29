#version 130
#extension GL_ARB_explicit_attrib_location:enable
#extension GL_ARB_separate_shader_objects:enable

uniform float camd;
uniform vec2 camp,camo,wins;

layout (location=0) in vec2 pos0;

out vec2 fragCoord;

vec2 cmul(vec2 a,vec2 b){
	return vec2(a.x*b.x-a.y*b.y,a.x*b.y+a.y*b.x);
}

void main(){
	fragCoord=cmul(pos0*vec2(wins.x/wins.y,1),camo*vec2(-1,1))*wins;
	gl_Position=vec4(pos0,0,1);
}