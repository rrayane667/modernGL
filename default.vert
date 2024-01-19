#version 330 core

layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 normal;


out vec4 vertexColor;

uniform ivec3 rot;

vec3 norm(vec3 u){
    return u/(pow(u.x, 2) + pow(u.y, 2) + pow(u.z, 2));
}
float dot( vec3 u, vec3 v){
    return u.x*v.x + u.y*v.y + u.z*v.z;
}

void main()
{
    vertexColor = vec4(255, 0, 0, 1.0f);
    float theta = 0.02*rot.x;
    float phi = 0.02*rot.y;
    float zeta = rot.z;
    float x = (aPos.x*cos(theta)-aPos.z*sin(theta))*cos(zeta)-(aPos.y*cos(phi)-aPos.x*sin(theta)*sin(phi)-aPos.z*cos(theta)*sin(phi))*sin(zeta);
    float y = (aPos.x*cos(theta)-aPos.z*sin(theta))*sin(zeta)+cos(zeta)*(aPos.y*cos(phi)-aPos.x*sin(theta)*sin(phi)-aPos.z*cos(theta)*sin(phi));
    float z = aPos.y*sin(phi)+aPos.x*sin(theta)*cos(phi)+aPos.z*cos(phi)*cos(theta);

    vec3 norm_normal = norm(normal);
    float fac = dot(aPos-vec3(0, 0, -50),norm_normal);
    if (fac>0){
        vertexColor = vec4(fac*255, fac*255, fac*255, 1.0f);
    }
    
    gl_Position = vec4(400*x/((z+400+50)*1200), 400*y/((z+400+50)*600), 0, 1.0);


}

