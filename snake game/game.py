import pygame
from settings import *
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def update(self):
        self.snake.move()

        # Check food collision
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.position = self.food.random_position()
            self.score += 1

        # Wall collision
        head = self.snake.body[0]
        if (head[0] < 0 or head[0] >= WIDTH // CELL_SIZE or
            head[1] < 0 or head[1] >= HEIGHT // CELL_SIZE):
            return False

        # Self collision
        if self.snake.check_collision():
            return False

        return True

    def draw(self, screen):
        screen.fill(BLACK)
        self.snake.draw(screen)
        self.food.draw(screen)

        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))