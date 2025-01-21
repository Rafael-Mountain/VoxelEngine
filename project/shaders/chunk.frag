#version 330 core

layout (location = 0) out vec4 fragColor;

const vec3 gamma = vec3(2.2);
const vec3 inv_gamma = 1/gamma;

uniform sampler2D u_texture_0;

in vec3 voxel_color;
in vec2 uv;

void main(){
    vec3 text_col = texture(u_texture_0, uv).rgb;
    text_col = pow(text_col, gamma);
    
    text_col.rgb *= voxel_color;
    
    text_col = pow(text_col, inv_gamma);
    fragColor = vec4(text_col,1); 
    
}