import re
import itertools
import numpy as np

class Object_Reader:
    def __init__(self):
        self.buffer = []
        self.indices = []
        self.vertices = []
        self.uv_coords = []
        self.normals = []
        self.faces = []
        self.check_textures = True
        self.check_normals = True

    def read_obj(self, filename):
        obj = list(open(filename).read().split('\n'))
        for line in obj:
            if line.startswith('v '):
                self.vertices.append([float(i) for i in line.split()[1:]])

            if line.startswith('vt '):
                self.uv_coords.append([float(i) for i in line.split()[1:]])

            if line.startswith('vn '):
                self.normals.append([float(i) for i in line.split()[1:]])

            if line.startswith('f '):
                face_lines = line.split(' ')[1:]
                for val in face_lines:

                    val = re.findall(r'\d+', val)

                    ind = ([int(i)-1 for i in val])

                    if len(ind) == 1:
                        self.faces.append(ind[0])
                    else:
                        self.faces.append(ind)

        for ind in self.faces:
            if len(self.normals) < 0:
                self.check_normals = False
            if len(self.uv_coords) < 0:
                self.check_normals = False



            if type(ind) is list:
                v = ind[0]
                self.buffer.append(self.vertices[v])
                self.indices.append(v)
            else:
                v = ind
                self.buffer.append(self.vertices[v])
                self.indices.append(v)

            if len(self.uv_coords) > 0:
                vt = ind[1]
                self.buffer.append(self.uv_coords[vt])
            elif len(self.normals) > 0:
                #self.check_textures = False
                vn = ind[1]
                self.buffer.append(self.normals[vn])

            if len(self.normals) > 0 and len(self.uv_coords) > 0:
                vn = ind[2]
                self.buffer.append(self.normals[vn])


        self.buffer = list(itertools.chain(*self.buffer))
        return np.array(self.buffer, dtype=np.float32), np.array(self.indices, dtype=np.uint32)












# obj = Object_Reader()
# obj.read_obj("cubetex.obj")
#
# buffer = obj.get_buffer()
# indices = obj.get_indices()
# print(buffer.nbytes)



















