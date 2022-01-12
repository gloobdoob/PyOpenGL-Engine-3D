from buffer_abstractions import *
from vertex_array import *
from renderer import *
from OBJreader import*
import pyrr

class Mesh:
    def __init__(self, filepath):
        self.m_buffer, self.m_indices = read_obj(filepath)
        self.m_va = Vertex_Array()
        self.m_vb = Vertex_Buffer(self.m_buffer.nbytes, self.m_buffer)
        self.m_ib = Index_Buffer(self.m_indices.nbytes, self.m_indices)
        self.translation = pyrr.Vector3()
        self.r = Renderer()

        self.m_va.Bind()
        b_format = Buffer_Format()
        b_format.push_float(3, False)
        b_format.push_float(2, False)
        b_format.push_float(3, False)
        self.m_va.AddBuffer(self.m_vb, b_format)



    def set_va(self):
        self.m_va.Bind()
        b_format = Buffer_Format()
        b_format.push_float(3, False)
        b_format.push_float(2, False)
        b_format.push_float(3, False)
        self.m_va.AddBuffer(self.m_vb, b_format)

    def set_va_noNormals(self):
        self.m_va.Bind()
        b_format = Buffer_Format()
        b_format.push_float(3, False)
        b_format.push_float(2, False)
        self.m_va.AddBuffer(self.m_vb, b_format)

    def set_va_noUV(self):
        self.m_va.Bind()
        b_format = Buffer_Format()
        b_format.push_float(3, False)
        b_format.push_float(3, False)
        self.m_va.AddBuffer(self.m_vb, b_format)

    def set_va_onlyVerts(self):
        self.m_va.Bind()
        b_format = Buffer_Format()
        b_format.push_float(3, False)
        self.m_va.AddBuffer(self.m_vb, b_format)


    def set_translation(self, vec):
        self.translation = vec
        return pyrr.matrix44.create_from_translation(pyrr.Vector3(self.translation))

    def drawArrays(self, shader):
        self.r.drawArrays(self.m_va, self.m_ib, shader)

    def drawElements(self, shader):
        self.r.drawElements(self.m_va, self.m_ib, shader)

    def get_VertexArray(self):
        return self.m_va

    def get_VertexBuffer(self):
        return self.m_vb

    def get_IndexBuffer(self):
        return self.m_ib






















