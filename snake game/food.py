import pygame
import random
from settings import CELL_SIZE, RED, WIDTH, HEIGHT

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1)
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1)
        return (x, y)

    def draw(self, surface):
        rect = pygame.Rect(self.position[0]*CELL_SIZE,
                           self.position[1]*CELL_SIZE,
                           CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, RED, rect)