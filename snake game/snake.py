import pygame
from settings import CELL_SIZE, GREEN

class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)
        self.grow_flag = False

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0],
                    head[1] + self.direction[1])

        self.body.insert(0, new_head)

        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False

    def grow(self):
        self.grow_flag = True

    def draw(self, surface):
        for segment in self.body:
            rect = pygame.Rect(segment[0]*CELL_SIZE,
                               segment[1]*CELL_SIZE,
                               CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, GREEN, rect)

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:]