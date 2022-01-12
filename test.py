from dataclasses import dataclass
from OpenGL.GL import*
import itertools
from OBJreader import read_obj
import re

import numpy as np
from OpenGL.GLU import*
import sys
@dataclass
class poopy:
    x : int
    y : object
    z : int
listofpoop = []
listofpoop.append(poopy(1, 3, 4))
listofpoop.append(poopy(4, GL_UNSIGNED_INT, 6))
listofpoop.append(poopy(2, 6, 7))
def get_list():
    return listofpoop


for poop in range(len(listofpoop)):
    poopoo = listofpoop[poop]

class Test:
    def __init__(self):
        self.num = 0


    def bruh(self, n):
        self.num += n

    def bruhh(self, n):
        self.num *= n

    def getNum(self):
        return self.num

t = Test()

t.bruh(4)
t.bruhh(5)
t.bruh(56)
f = Test()

f.bruh(56)
f.bruhh(4)

num = f.getNum()


bigboilist = []

verts = []
norms = []
uvs = []

verts.append((0, 2, 3))
verts.append((1, 7, 2))
verts.append((6, 5, 9))

norms.append((4, 9, 2))
norms.append((9, 3, 3))
norms.append((3, 3, 8))

uvs.append((4, 9))
uvs.append((9, 3))
uvs.append((3, 3))




for (vert, norm, uv) in itertools.zip_longest(verts, norms, uvs):
    bigboilist.append(vert)
    bigboilist.append(norm)
    bigboilist.append(uv)
out = list(itertools.chain(*bigboilist))



buffer = []
indices = []

vertices = []
uvs = []
normals = []
faces = []


obj = list(open("cubetex.obj").read().split('\n'))

for line in obj:
    if line.startswith('v '):
        vertices.append([float(i) for i in line.split()[1:]])

    if line.startswith('vt '):
        uvs.append([float(i) for i in line.split()[1:]])

    if line.startswith('vn '):
        normals.append([float(i) for i in line.split()[1:]])

    if line.startswith('f '):
        face_lines = line.split(' ')[1:]
        for val in face_lines:
            ind = ([int(i)-1 for i in val.split('/')])
            faces.append(ind)



for ind in faces:
    v = ind[0]
    vt = ind[1]
    vn = ind[2]

    buffer.append(vertices[v])
    buffer.append(uvs[vt])
    buffer.append(normals[vn])
    indices.append(v)

buffer = list(itertools.chain(*buffer))



class Mesh:
    def __init__(self):
        self.buff = []
        self.ind = []
        self.buffer = np.empty(len(self.buff), dtype=np.float32)
        self.indices = np.empty(len(self.ind), dtype=np.uint32)

    def load_model(self, filepath):
        self.buff, self.ind = read_obj(filepath)
        self.buffer = np.array(self.buff, dtype=np.float32)
        self.indices = np.array(self.ind, dtype=np.uint32)




m = Mesh()

m.load_model("cubetex.obj")

print(m.buffer)





