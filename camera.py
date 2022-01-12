import pyrr
import pygame
import math



class Camera:
    def __init__(self):
        self.camera_pos = pyrr.Vector3([0.0, 0.0, 3.0])
        self.camera_target = pyrr.Vector3([0.0, 0.0, 0.0])
        self.camera_direction = pyrr.vector3.normalize(self.camera_pos - self.camera_target)
        self.up = pyrr.Vector3([0.0, 1.0, 0.0])
        self.camera_right = pyrr.vector3.normalize(pyrr.vector3.cross(self.up, self.camera_direction))
        self.camera_front = pyrr.Vector3([0.0, 0.0, -1.0])
        self.camera_up = pyrr.Vector3([0.0, 1.0, 0.0])

        self.yaw = -90.0
        self.pitch = 0.0


    def get_view(self):
        return pyrr.matrix44.create_look_at(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up)


    def process_input(self, dt, key):
        s = dt * 15

        if key[pygame.K_w]:
            self.camera_pos += s * self.camera_front
        if key[pygame.K_s]:
            self.camera_pos -= s * self.camera_front
        if key[pygame.K_a]:
            self.camera_pos -= pyrr.vector3.normalize(pyrr.vector3.cross(self.camera_front, self.camera_up)) * s
        if key[pygame.K_d]:
            self.camera_pos += pyrr.vector3.normalize(pyrr.vector3.cross(self.camera_front, self.camera_up)) * s

        if key[pygame.K_SPACE]:
            self.camera_pos += s * self.camera_up
        if key[pygame.K_LSHIFT]:
            self.camera_pos -= s * self.camera_up

    def mouse_process(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = event.rel

            xoffset = x
            yoffset = y

            sensitivity = 0.3

            xoffset *= sensitivity
            yoffset *= sensitivity

            self.yaw += xoffset
            self.pitch += yoffset

            if self.pitch > 89.0:
                self.pitch = 89.0
            if self.pitch < -89.0:
                self.pitch = -89.0

            direction = pyrr.Vector3([
                math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch)),
                math.sin(math.radians(-self.pitch)),
                math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))
            ])
            self.camera_front = pyrr.vector3.normalize(direction)









