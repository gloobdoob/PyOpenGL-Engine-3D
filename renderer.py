from OpenGL.GL import*
import numpy as np

class Renderer:
    @staticmethod
    def drawElements(vertex_array, index_buffer, shader):
        vertex_array.Bind()
        index_buffer.Bind()
        shader.Bind()
        glDrawElements(GL_TRIANGLES, index_buffer.count, GL_UNSIGNED_INT, None)

    @staticmethod
    def drawArrays(vertex_array, index_buffer, shader):
        vertex_array.Bind()
        index_buffer.Bind()
        shader.Bind()
        glDrawArrays(GL_TRIANGLES, 0, index_buffer.count)

    @staticmethod
    def clear():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
    @staticmethod
    def set_viewport(width: object, height: object) -> object:
        glViewport(0, 0, width, height)






