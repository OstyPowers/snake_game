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
    block_x = 100
    block_y = 100

    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    block_y -= 10
                    draw_block()

                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()

                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()

                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            elif event.type == QUIT:
                running = False

