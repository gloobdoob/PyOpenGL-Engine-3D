import itertools
import numpy as np
import re


def read_obj(filename):
    buffer = []
    indices = []
    vertices = []
    uv_coords = []
    normals = []
    faces = []
    obj = list(open(filename).read().split('\n'))
    for line in obj:
        if line.startswith('v '):
            vertices.append([float(i) for i in line.split()[1:]])

        if line.startswith('vt '):
            uv_coords.append([float(i) for i in line.split()[1:]])

        if line.startswith('vn '):
            normals.append([float(i) for i in line.split()[1:]])

        if line.startswith('f '):
            face_lines = line.split(' ')[1:]
            for val in face_lines:

                val = re.findall(r'\d+', val)

                ind = ([int(i)-1 for i in val])

                if len(ind) == 1:
                    faces.append(ind[0])
                else:
                    faces.append(ind)


    for ind in faces:

        if type(ind) is list:
            v = ind[0]
            buffer.append(vertices[v])
            indices.append(v)
        else:
            v = ind
            buffer.append(vertices[v])
            indices.append(v)

        if len(uv_coords) > 0:
            vt = ind[1]
            buffer.append(uv_coords[vt])
        elif len(normals) > 0:
            vn = ind[1]
            buffer.append(normals[vn])

        if len(normals) > 0 and len(uv_coords) > 0:
            vn = ind[2]
            buffer.append(normals[vn])



    buffer = list(itertools.chain(*buffer))

    return np.array(buffer, dtype=np.float32), np.array(indices, dtype=np.uint32)
    #return buffer, indices



