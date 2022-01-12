from OpenGL.GL import*
from OpenGL.GL.shaders import *
from PIL import Image
import numpy as np

class Texture:
    def __init__(self, filepath):
        self.filepath = filepath
        self.rendererID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.rendererID)

        # set texture filter parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        # set texture wrapping parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        self.image = Image.open(filepath)
        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        self.img_data = self.image.convert("RGBA").tobytes()

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.image.width, self.image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.img_data)
        glBindTexture(GL_TEXTURE_2D, 0)


    def Bind(self, slot=0):
        glActiveTexture(GL_TEXTURE0 + slot)
        glBindTexture(GL_TEXTURE_2D, self.rendererID)

    @staticmethod
    def Unbind():
        glBindTexture(GL_TEXTURE_2D, 0)

    def delete(self):
        self.rendererID = glDeleteTextures(1)





