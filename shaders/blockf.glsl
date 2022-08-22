#version 130
#extension GL_ARB_explicit_attrib_location:enable
#extension GL_ARB_separate_shader_objects:enable

in vec2 pos1;
layout (location=1) in vec4 col1;

layout (location=0) out vec4 col2;

vec2 GetGradient(vec2 intPos,float t){
	float hash=fract(sin(dot(intPos,vec2(12.9898,78.233)))*43758.5453);
	float angle=6.283185*hash+4*t*hash;
	return vec2(cos(angle),sin(angle));
}

float Pseudo3dNoise(vec3 pos){
	vec2 i=floor(pos.xy);
	vec2 f=pos.xy-i;
	vec2 blend=f*f*(3-2*f);
	float noiseVal =
		mix(
			mix(
				dot(GetGradient(i+vec2(0,0),pos.z),f-vec2(0,0)),
				dot(GetGradient(i+vec2(1,0),pos.z),f-vec2(1,0)),
				blend.x
			),
			mix(
				dot(GetGradient(i+vec2(0,1),pos.z),f-vec2(0,1)),
				dot(GetGradient(i+vec2(1,1),pos.z),f-vec2(1,1)),
				blend.x
			),
		blend.y
	);
	return 1.4*noiseVal;//normalize to about [-1..1]
}

void main(){
	vec2 char_pos=vec2(0.5,0.25)*pos1+0.5;
	vec2 to_edge=char_pos-round(char_pos);
	col2=col1;
	col2.rgb+=0.04*Pseudo3dNoise(vec3(8*pos1,0));
	col2.rgb*=1-0.3*dot(to_edge,to_edge);
}