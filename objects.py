import numpy as np

def cross(u ,v):
    return [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]
def d(u,v):
    return [u[i] - v[i] for i in range(3)]
class triangle:
    def __init__(self, app) -> None:
        self.app = app
        self.ctx = app.ctx
        self.v= self.get_vertex_data()
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program('default')
        
        
        self.vao = self.get_vao()
        #self.shader_program['normal'].write(np.array([cross(d(self.v[0][i[2]-1], self.v[0][i[0]-1]), d(self.v[0][i[1]-1], self.v[0][i[0]-1])) for i in self.v[1] ]))
        
    def render(self, r):
        self.shader_program['rot'].write(np.array(r))
        self.vao.render()
        
    def zbl(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()
        
    def get_vao(self):
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '3f 3f', 'aPos', 'normal')], index_element_size=4)

        return vao
    
    def get_vertex_data(self):
        vertex_data,faces = load_obj('C:/Users/ORDI/Desktop/Dossiers/vsCode code/Python/pythonGrafiks-main/teapot.obj')
        return vertex_data, faces
    
    def get_vbo(self):
        vertex, faces = self.v
        crd=[]
        norm = [cross(d(vertex[triangles[1]-1], vertex[triangles[2]-1]), d(vertex[triangles[1]-1], vertex[triangles[0]-1])) for triangles in faces]
        for i in norm:
            crd.extend([i]*3)
        norm = crd
        kolchi = np.hstack([[[vertex[i-1][2], vertex[i-1][1], vertex[i-1][0]] for triangles in faces for i in triangles], norm])
        vbo = self.ctx.buffer(kolchi)
        return vbo
    
    def get_shader_program(self, shader_name):
        with open(f'C:/Users/ORDI/Desktop/Dossiers/vsCode code/Python/modernGL/{shader_name}.vert') as file:
        #vertex_shader = "#version 330 core\n layout (location = 0) in vec3 aPos;\n void main()\n{\ngl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n}" 
            vertex_shader=file.read()
            
        with open(f'C:/Users/ORDI/Desktop/Dossiers/vsCode code/Python/modernGL/{shader_name}.frag') as file:
        #fragment_shader = "#version 330 core\n out vec4 FragColor; \n void main()\n {\n FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f); \n}\n"
            fragment_shader=file.read()
            
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
def load_obj(name):
    v=[]
    f=[]
    obj=open(name)    
    for line in obj.readlines():
        if line[:2] == "v ":
            l=line.split()[1:]

            vert = [100*float(l[0]), 100*float(l[1]), 100*float(l[2])]
            v.append(vert)

        elif line[:2] == "f ":
            l=line.split()[1:]

            faces = [int(l[0]), int(l[1]), int(l[2])]
            f.append(faces)
    obj.close()

    return v, f
    
    