from player import Player
from camera import Camera
from tree import Tree

import pygame
import sys


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SHOOTER")


clock = pygame.time.Clock()
running = True

player = Player()
camera = Camera(width, height)
tree = Tree()

all_sprites = pygame.sprite.Group(player, tree)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    player.handle_keys()

    camera.update(player)

    for entity in all_sprites:
        screen.blit(entity.image, camera.apply(entity))

    pygame.display.flip()

    clock.tick(60)

    print("FPS: ", clock.get_fps())


pygame.quit()
sys.exit()
