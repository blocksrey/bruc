#version 130
#extension GL_ARB_explicit_attrib_location:enable
#extension GL_ARB_separate_shader_objects:enable

uniform vec2 wins;
uniform float camd,time;

in vec2 fragCoord;

layout (location=0) out vec4 col1;

const float speed=0.02;
const float cloudcover=0.5;
const vec3 skycolor1=vec3(0,0,0.3);
const vec3 skycolor2=vec3(0.1,0.4,0.8);

const mat2 m=mat2(1.69,1.21,-1.23,1.62);

vec2 hash(vec2 p){
	p=vec2(dot(p,vec2(127.1,311.7)),dot(p,vec2(269.5,183.3)));
	return 2*fract(sin(p)*43758.5453123)-1;
}

float noise(vec2 p){
	const float K1=0.366025404;//(sqrt(3)-1)/2;
	const float K2=0.211324865;//(3-sqrt(3))/6;
	vec2 i=floor(p+(p.x+p.y)*K1);
	vec2 a=p-i+(i.x+i.y)*K2;
	vec2 o=(a.x>a.y)?vec2(1,0):vec2(0,1);//vec2 of=0.5+0.5*vec2(sign(a.x-a.y),sign(a.y-a.x));
	vec2 b=a-o+K2;
	vec2 c=a-1+2*K2;
	vec3 h=max(0.5-vec3(dot(a,a),dot(b,b),dot(c,c)),0);
	vec3 n=h*h*h*h*vec3(dot(a,hash(i+0)),dot(b,hash(i+o)),dot(c,hash(i+1)));
	return dot(n,vec3(70));
}

float fbm(vec2 n){
	float total=0,amplitude=0.1;
	for (int i=4;--i>=0;){
		total+=noise(n)*amplitude;
		n=m*n;
		amplitude*=0.4;
	}
	return total;
}

void main(){
	float cloudscale=0.2+0.0005*camd;//this isnt fucking 'cloud scale'

	vec2 p=fragCoord/wins;
	vec2 uv=p;
	float tim=time*speed;
	float q=fbm(uv*cloudscale*0.5);

	//ridged noise shape
	float r=0;
	//*
	uv*=cloudscale;
	uv-=q-tim;
	float weight=0.8;
	for (int i=4;--i>=0;){
		r+=abs(weight*noise(uv));
		uv=m*uv+tim;
		weight*=0.7;
	}

	float c=0;

	float c1=0;
	//*noise ridge color
	tim=time*speed*3;
	uv=p;
	uv*=cloudscale*3;
	uv-=q-tim;
	weight=0.4;
	for (int i=4;--i>=0;){
		c1+=abs(weight*noise(uv));
		uv=m*uv+tim;
		weight*=0.6;
	}
	//*/

	c+=c1;

	vec3 skycolor=mix(skycolor2,skycolor1,p.y);
	vec3 cloudcolor=vec3(1.1,1.1,0.9)*clamp((1+2*c),0,1);

	vec3 result=mix(skycolor,clamp(skycolor+cloudcolor,0,1),clamp(cloudcover+c,0,1));

	col1=vec4(result,1);
}