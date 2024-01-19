#version 330 core
out vec4 FragColor;

in vec4 vertexColor;

uniform vec3 rot;
void main()
{
    FragColor = vec4(255, 255, 255, 1);
}
