import pygame
import pathlib
from support import import_folder

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.5

        dust_path = pathlib.Path.cwd().joinpath("graphics", "character", "dust_particles")
        if type == "jump":
            self.frames = import_folder(dust_path.joinpath("jump"))
        if type == "land":
            self.frames = import_folder(dust_path.joinpath("land"))

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self, x_shift):
        self.animate()
        self.rect.x += x_shift