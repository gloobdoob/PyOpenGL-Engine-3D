from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GL.shaders import *
import pygame
from pygame.locals import *
from shader import *
from texture import*
from mesh import*
from camera import *


pygame.init()
WIDTH = 1400
HEIGHT = 800
pygame.display.set_mode((WIDTH, HEIGHT), OPENGL | DOUBLEBUF | RESIZABLE)
clock = pygame.time.Clock()

c = Camera()

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

mTerrain = Mesh("obj/lowpoly.obj")
mCube = Mesh("obj/cubetex.obj")
mCar = Mesh("obj/car low poly.obj")
mTeapot = Mesh("obj/teapot.obj")


object_shader = Shader("object_shader.glsl")
light_shader = Shader("light_cube.glsl")

cube_texture = Texture("textures/crate_diffuse.png")
cube_specular = Texture("textures/crate_specular.png")

car_texture = Texture("textures/texture.png")
car_specular = Texture("textures/Specular_map_carBod.png")

projection = pyrr.matrix44.create_perspective_projection_matrix(90, WIDTH/HEIGHT, 0.1, 1000)

object_shader.Bind()
object_shader.setUniformMatrix4fv("projection", projection)

light_shader.Bind()
light_shader.setUniformMatrix4fv("projection", projection)

glClearColor(0.0, 0.0, 0.0, 1.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)

cube_positions = [
    [ 0.0,  0.0,  0.0],
    [ 2.0,  5.0, -15.0],
    [-1.5, -2.2, -2.5],
    [-3.8, -2.0, -12.3],
    [ 2.4, -0.4, -3.5],
    [-1.7,  3.0, -7.5],
    [ 1.3, -2.0, -2.5],
    [ 1.5,  2.0, -2.5],
    [ 1.5,  0.2, -1.5],
    [-1.3,  1.0, -1.5]
]


renderer = Renderer()

pygame.event.get()
pygame.mouse.get_rel()
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

running = True
while running:
    for event in pygame.event.get():
        c.mouse_process(event)
        if event.type == pygame.QUIT:
            running = False
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                #running = False
                pygame.event.set_blocked(pygame.MOUSEMOTION)
                pygame.mouse.set_visible(True)
                pygame.event.set_grab(False)

        if event.type == pygame.MOUSEBUTTONUP:
            pygame.event.set_allowed(pygame.MOUSEMOTION)
            pygame.mouse.set_visible(False)
            pygame.event.set_grab(True)
            c.mouse_process(event)

        if event.type == pygame.VIDEORESIZE:
            glViewport(0, 0, event.w, event.h)
            projection = pyrr.matrix44.create_perspective_projection_matrix(90, event.w/event.h, 0.1, 1000)
            object_shader.Bind()
            object_shader.setUniformMatrix4fv("projection", projection)
            light_shader.Bind()
            light_shader.setUniformMatrix4fv("projection", projection)



    dt = clock.tick()/1000
    ct = pygame.time.get_ticks()/1000

    key = pygame.key.get_pressed()
    c.process_input(dt, key)

    renderer.clear()
    view = c.get_view()

    object_shader.Bind()
    object_shader.setUniformMatrix4fv("view", view)
    object_shader.setUniform1i("switcher", 0)

    object_shader.setUniform3f("lightColor", 1.0, 1.0, 1.0)
    lightPos = [18 * math.sin(ct), 10 , 18 * math.cos(ct)]
    #lightPos = [0, 0, 5]
    lightDir = [-0.2, -5.0, -0.3]
    object_shader.setUniform3fv("light.position", lightPos)
    #object_shader.setUniform3fv("light.direction", lightDir)
    object_shader.setUniform3f("light.ambient", 0.3, 0.3, 0.3)
    object_shader.setUniform3f("light.diffuse", 0.8, 0.8, 0.8)
    object_shader.setUniform3f("light.specular", 1.0, 1.0, 1.0)
    #attenuation for lighting
    att = (1.0, 0.045, 0.0076)
    object_shader.setUniform1f("light.constant", att[0])
    object_shader.setUniform1f("light.linear", att[1])
    object_shader.setUniform1f("light.quadratic", att[2])


    viewPos = c.camera_pos
    object_shader.setUniform3fv("viewPos", viewPos)

    # rotating projection matrix
    projx = pyrr.Matrix44.from_x_rotation(1.0 * ct)
    projy = pyrr.Matrix44.from_y_rotation(1.4 * ct)
    projxy = pyrr.matrix44.multiply(projx, projy)


    #rotating cube
    cube_texture.Bind(0)
    cube_specular.Bind(1)
    object_shader.setUniform1i("tex_material.diffuse", 0)
    object_shader.setUniform1i("tex_material.specular", 1)
    object_shader.setUniform1f("tex_material.shininess", 64.0)
    for i in range(len(cube_positions)):
        x = pyrr.Matrix44.from_x_rotation(i * 0.1 * ct)
        y = pyrr.Matrix44.from_y_rotation(i * 0.4 * ct)
        xy = pyrr.matrix44.multiply(x, y)
        rot = pyrr.matrix44.multiply(xy, mCube.set_translation(cube_positions[i]))
        object_shader.setUniformMatrix4fv("model", rot)
        mCube.drawArrays(object_shader)

    #car
    object_shader.Bind()
    car_texture.Bind(3)
    car_specular.Bind(4)
    rotcar = pyrr.matrix44.multiply(projxy, mCar.set_translation([13, 0, -2]))
    object_shader.setUniform1i("tex_material.diffuse", 3)
    object_shader.setUniform1i("tex_material.specular", 4)
    object_shader.setUniform1f("tex_material.shininess", 256.0)
    object_shader.setUniformMatrix4fv("model", mCar.set_translation([13, 0, -2]))
    mCar.drawArrays(object_shader)

    #set switcher to one to render colors
    object_shader.setUniform1i("switcher", 1)

    #terrain
    object_shader.setUniform3f("col_material.ambient", 0.1, 0.7, 0.35)
    object_shader.setUniform3f("col_material.diffuse", 0.1, 0.7, 0.35)
    object_shader.setUniform3f("col_material.specular", 0.2, 0.2, 0.2)
    object_shader.setUniform1f("col_material.shininess", 4.0)
    object_shader.setUniformMatrix4fv("model", mTerrain.set_translation([-4, -4, -2]))
    mTerrain.drawArrays(object_shader)

    #teapot
    rotpot = pyrr.matrix44.multiply(projxy, mTeapot.set_translation([18 * math.cos(ct*1.5), 9 , 15 * math.sin(ct*1.5)]))
    object_shader.setUniform3f("col_material.ambient", 0.8, 0.3, 0.7)
    object_shader.setUniform3f("col_material.diffuse", 0.8, 0.3, 0.7)
    object_shader.setUniform3f("col_material.specular", 1.0, 1.0, 1.0)
    object_shader.setUniform1f("col_material.shininess", 256.0)
    object_shader.setUniformMatrix4fv("model", rotpot)
    mTeapot.drawArrays(object_shader)

    #light cube
    light_shader.Bind()
    light_shader.setUniformMatrix4fv("view", view)
    light_shader.setUniformMatrix4fv("model", mCube.set_translation(lightPos))
    mCube.drawArrays(light_shader)


    pygame.display.flip()

pygame.quit()









