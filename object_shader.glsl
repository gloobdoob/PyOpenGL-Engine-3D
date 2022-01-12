// VERTEX_SHADER
# version 330 core
layout(location = 0) in vec3 position;
layout(location = 1) in vec2 texCoords;
layout(location = 2) in vec3 normals;

uniform mat4 projection;
uniform mat4 model;
uniform mat4 view;

out vec3 FragPos;
out vec2 v_TexCoords;
out vec3 Normal;
void main()
{
    gl_Position  =   projection * view *  model * vec4(position, 1.0);
    FragPos = vec3(model * vec4(position,1.0));
    Normal = mat3(transpose(inverse(model)))*normals;
    v_TexCoords = texCoords;
}

// FRAGMENT_SHADER
# version 330 core
struct colorMaterial{
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
    float shininess;
};

struct texMaterial{
    sampler2D diffuse;
    sampler2D specular;
    float shininess;
};

struct Light{
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
    vec3 position;
    vec3 direction;

    float constant;
    float linear;
    float quadratic;
};

in vec3 Normal;
in vec2 v_TexCoords;
in vec3 FragPos;

uniform Light light;
uniform colorMaterial col_material;
uniform texMaterial tex_material;

uniform vec3 viewPos;
uniform vec3 lightColor;
uniform vec3 u_Color;

uniform sampler2D u_Texture;
uniform int switcher = 0;

out vec4 FragColor;

void main()
{

    float distance = length(light.position - FragPos);
    float attenuation = 1.0/(light.constant + light.linear * distance + light.quadratic * (distance*distance));

    vec3 norm = normalize(Normal);
   // vec3 lightDir = normalize(-light.direction);
    vec3 lightDir = normalize(light.position - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);

    float specularStrength = 0.5;
    vec3 viewDir = normalize(-FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);


    if(switcher == 0){
        float spec = pow(max(dot(viewDir, reflectDir), 0.0), tex_material.shininess);

        vec4 texColor = texture(tex_material.diffuse, v_TexCoords);

        vec3 ambient = light.ambient * vec3(texColor) ;
        vec3 diffuse = light.diffuse * (diff * vec3(texColor));
        vec3 specular = (vec3(texture(tex_material.specular, v_TexCoords))) * spec * light.specular;

        ambient *= attenuation;
        diffuse *= attenuation;
        specular *= attenuation;

        vec3 result = ambient + diffuse + specular;
        FragColor = vec4(result,1.0);}

    else if (switcher == 1){

        float spec = pow(max(dot(viewDir, reflectDir), 0.0), col_material.shininess);

        vec3 ambient = light.ambient * col_material.ambient ;
        vec3 diffuse = light.diffuse * (diff * col_material.diffuse);
        vec3 specular = (col_material.specular * spec) * light.specular;

        ambient *= attenuation;
        diffuse *= attenuation;
        specular *= attenuation;

        vec3 result = ambient + diffuse + specular;
        FragColor = vec4(result,1.0);}
}


