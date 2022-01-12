from OpenGL.GL import*
from OpenGL.GL.shaders import *

class Shader:
    def __init__(self, filename):
        self.filename = filename
        self.locations_cache = {}
        self.string = open(self.filename).read()
        self.split = self.string.split('// FRAGMENT_SHADER')
        self.vertex_shader = self.split[0]
        self.fragment_shader = self.split[1]

        self.shader = compileProgram(compileShader(self.vertex_shader, GL_VERTEX_SHADER), compileShader(self.fragment_shader, GL_FRAGMENT_SHADER))

    def Bind(self):
        glUseProgram(self.shader)

    @staticmethod
    def Unbind():
        glUseProgram(0)

    # color uniform
    def setUniform4f(self, uniform_name, v0 : float, v1 : float, v2 : float, v3 : float):
        glUniform4f(self.getUniformLocation(uniform_name), v0, v1, v2, v3)

    def setUniform4fv(self, uniform_name, vec):
        glUniform4fv(self.getUniformLocation(uniform_name),1, vec)

    def setUniform3f(self, uniform_name, v0 : float, v1 : float, v2 : float):
        glUniform3f(self.getUniformLocation(uniform_name), v0, v1, v2)

    def setUniform3fv(self, uniform_name, vec):
        glUniform3fv(self.getUniformLocation(uniform_name), 1, vec)

    def setUniform1i(self, uniform_name, value : int):
        glUniform1i(self.getUniformLocation(uniform_name), value)

    def setUniform1f(self, uniform_name, value : float):
        glUniform1f(self.getUniformLocation(uniform_name), value)

    #matrix uniform, name, how many matrices, bool transpose, matrix itself
    def setUniformMatrix4fv(self, uniform_name, matrix):
        glUniformMatrix4fv(self.getUniformLocation(uniform_name), 1, GL_FALSE, matrix)

    def getUniformLocation(self, uniform_name):
        if uniform_name in self.locations_cache:
            return self.locations_cache[uniform_name]

        location = glGetUniformLocation(self.shader, uniform_name)
       # assert location != -1
        self.locations_cache[uniform_name] = location
        return location





