import pygame
import pathlib
from os import walk

def import_folder(path):
    surface_list = []

    for img_file in path.glob("*.png"):
        image_surf = pygame.image.load(img_file).convert_alpha()
        surface_list.append(image_surf)

    return surface_list

    # for _, __, img_files in walk(path):
    #     print(img_files)
    #     for img in img_files:
    #         full_path = path + "/" + img
    #         print(full_path)
    #         # Note styles need to be image files as png or jpg.
    #         image_surf = pygame.image.load(full_path).convert_alpha()
    #         surface_list.append(image_surf)
    #         print(surface_list)

    # return surface_list