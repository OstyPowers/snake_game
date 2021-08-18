import pygame
from pygame.locals import *
import time


class Snake:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100
        self.tile_size = self.block.get_width()
        self.direction = 'down'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def draw(self):
        self.parent_screen.fill((92, 25, 84))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def walk(self):
        if self.direction == 'up':
            self.y -= self.tile_size

        if self.direction == 'down':
            self.y += self.tile_size

        if self.direction == 'left':
            self.x -= self.tile_size

        if self.direction == 'right':
            self.x += self.tile_size

        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 1000))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            time.sleep(0.2)



if __name__ == "__main__":
    game = Game()
    game.run()


