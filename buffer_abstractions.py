from OpenGL.GL import*
import numpy as np

class Vertex_Buffer:
    def __init__(self, size, data):
        self.size = size
        self.data = data
        self.renderer_ID = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.renderer_ID)
        glBufferData(GL_ARRAY_BUFFER, self.size, self.data, GL_STATIC_DRAW)

    def Bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.renderer_ID)

    @staticmethod
    def Unbind():
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def delete(self):
        self.renderer_ID = glDeleteBuffers(1)



class Index_Buffer:
    def __init__(self, size, data):
        self.size = size
        self.data = data
        self.count = len(self.data)
        self.renderer_ID = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.renderer_ID)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.size, self.data, GL_STATIC_DRAW)

    def Bind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.renderer_ID)

    @staticmethod
    def Unbind():
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)


    def delete(self):
        self.renderer_ID = glDeleteBuffers(1)












