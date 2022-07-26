#version 130

varying vec4 position;

void main() {
	position = ftransform();
	gl_Position = ftransform();
}