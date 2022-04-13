import pygame
from collections import namedtuple
from random import randint

class Level:

    def __init__(self, display):

        self.snake_head = [720/2, 480/2]
        self.food = None
        self._display = display
        self.block = 20
        self.snake_body = [self.snake_head, [self.snake_head[0] - self.block, self.snake_head[1]], [self.snake_head[0] - 2*self.block, self.snake_head[1]]]

    def _spawn_food(self):   
        
        x = randint(0, (720 - self.block) // self.block) * self.block
        y = randint(0, (480 - self.block) // self.block) * self.block
        self.food = [x, y]
        if self.food in self.snake_body:
            self._spawn_food()


    def render(self):

        self._display.fill((0, 0, 0))

        for block in self.snake:

            pygame.draw.rect(self._display, (0,201,87), pygame.Rect(block[0], block[1], self.block, self.block))

        pygame.draw.rect(self._display, (220,20,60), pygame.Rect(self.food[0], self.food[1], self.block, self.block))

        pygame.display.update()


    

        