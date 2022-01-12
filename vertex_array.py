from OpenGL.GL import*
from OpenGL.GLU import*
from dataclasses import dataclass
import numpy as np



def typesize_switch(datatype):
    switcher = {
        GL_FLOAT : np.dtype(np.float32).itemsize,
        GL_INT   : np.dtype(np.int32).itemsize,
        GL_UNSIGNED_INT   : np.dtype(np.uint32).itemsize,
        GL_BYTE   : np.dtype(np.byte).itemsize,
        GL_UNSIGNED_BYTE   : np.dtype(np.ubyte).itemsize,
        GL_SHORT   : np.dtype(np.short).itemsize,
        GL_UNSIGNED_SHORT   : np.dtype(np.ushort).itemsize,
    }
    return switcher.get(datatype)


@dataclass
class Buffer_Element:
    count : int
    type  : object
    normalized : bool

class Buffer_Format:
    def __init__(self):
        self.buffer_elements = []
        self.stride = 0

    def push_float(self, count, norm):
        self.buffer_elements.append(Buffer_Element(count, GL_FLOAT, norm))
        self.stride += count * typesize_switch(GL_FLOAT)

    def push_int(self, count, norm):
        self.buffer_elements.append(Buffer_Element(count, GL_INT, norm))
        self.stride += count * typesize_switch(GL_INT)

    def push_uInt(self, count, norm):
        self.buffer_elements.append(Buffer_Element(count, GL_UNSIGNED_INT, norm))
        self.stride += count * typesize_switch(GL_UNSIGNED_INT)

    def push_byte(self, count, norm):
        self.buffer_elements.append(Buffer_Element(count, GL_BYTE, norm))
        self.stride += count * typesize_switch(GL_BYTE)

    def push_uByte(self, count, norm):
        self.buffer_elements.append(Buffer_Element(count, GL_UNSIGNED_BYTE, norm))
        self.stride += count * typesize_switch(GL_UNSIGNED_BYTE)

    def push_short(self, count, norm):
        self.buffer_elements.append(Buffer_Element(count, GL_SHORT, norm))
        self.stride += count * typesize_switch(GL_SHORT)

    def push_uShort(self, count, norm):
        self.buffer_elements.append(Buffer_Element(count, GL_UNSIGNED_SHORT, norm))
        self.stride += count * typesize_switch(GL_UNSIGNED_SHORT)

    def get_stride(self):
        return self.stride

    def get_elements(self):
        return self.buffer_elements

class Vertex_Array:
    def __init__(self):
        self.renderer_ID = glGenVertexArrays(1)

    def Bind(self):
        glBindVertexArray(self.renderer_ID)

    @staticmethod
    def Unbind():
        glBindVertexArray(0)

    @staticmethod
    def AddBuffer(vb, buffer_format):
        vb.Bind()
        stride = buffer_format.get_stride()
        elements = buffer_format.get_elements()
        offset = 0

        for i in range(len(elements)):
            element = elements[i]
            glVertexAttribPointer(i, element.count, element.type, element.normalized, stride, ctypes.c_void_p(offset))
            glEnableVertexAttribArray(i)
            offset += element.count * typesize_switch(element.type)




