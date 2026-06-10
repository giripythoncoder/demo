import pygame
from settings import WIDTH, HEIGHT, FPS
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()
    game = Game()

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.snake.direction != (0, 1):
                    game.snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and game.snake.direction != (0, -1):
                    game.snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and game.snake.direction != (1, 0):
                    game.snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and game.snake.direction != (-1, 0):
                    game.snake.direction = (1, 0)

        if not game.update():
            print("Game Over!")
            running = False

        game.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()