#version 130

varying vec4 position;

void main() {
	gl_FragColor = vec4(position.x, 0, 0, 1);
}