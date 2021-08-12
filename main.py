import pygame
from pygame.locals import *


def draw_block():
    surface.fill((92, 25, 84))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000, 1000))
    surface.fill((92, 25, 84))

    block = pygame.image.load("resources/block.jpg").convert()
    tile_size = block.get_width()
    block_x = 100
    block_y = 100

    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

    running = True
# TODO sort current code into snake and game class for oop
# TODO move methods into classes
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    block_y -= tile_size
                    draw_block()

                if event.key == K_DOWN:
                    block_y += tile_size
                    draw_block()

                if event.key == K_LEFT:
                    block_x -= tile_size
                    draw_block()

                if event.key == K_RIGHT:
                    block_x += tile_size
                    draw_block()

            elif event.type == QUIT:
                running = False
