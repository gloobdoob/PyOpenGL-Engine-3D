// VERTEX_SHADER
# version 330
layout(location = 0) in vec3 position;
layout(location = 1) in vec2 texCoords;
layout(location = 2) in vec3 normals;

uniform mat4 projection;
uniform mat4 model;
uniform mat4 view;
void main()
{
    gl_Position  = projection * view *  model * vec4(position, 1.0);
}
// FRAGMENT_SHADER
# version 330
out vec4 FragColor;

void main()
{
    FragColor = vec4(1.0);
}