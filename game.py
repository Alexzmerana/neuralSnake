import pygame
import random

from snake import Snake
from apple import Apple

class Game:
    def __init__(self) -> None:
        self.window_width = 800
        self.window_height = 800
        self.block_size = 16
        self.width = self.window_width // self.block_size
        self.height = self.window_height // self.block_size

        self.white_color = (255, 255, 255)
        self.black_color = (0, 0, 0)
        self.red_color   = (255, 0, 0)

        self.snake = Snake()
        self.apple = Apple((self.width - 2, self.height - 2))
        self.score = 0

        self.clock = pygame.time.Clock()

        self.game_window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Neural Snake")


        self.clock = pygame.time.Clock()

    def display(self):
        for x, y in self.snake.list:
            pygame.draw.rect(self.game_window, self.white_color, (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
        pygame.draw.rect(self.game_window, self.red_color, (self.apple.coords[0] * self.block_size, self.apple.coords[1] * self.block_size, self.block_size, self.block_size))

    def update(self):
        self.snake.move()
        
    def collision(self):
        head = self.snake.list[0]

        if(head in self.snake.list[1:]): return True

        elif(-1 >= head[0] or head[0] >= self.width): return True

        elif(-1 >= head[1] or head[1] >= self.height): return True

        if head == self.apple.coords:
            self.snake.grow()
            self.score += 1
            while self.apple.coords in self.snake.list:
                self.apple.coords = (random.randint(0, self.width), random.randint(0, self.height))

        return False

    def run_loop(self):
        while not self.collision():
            self.game_window.fill(self.black_color)
            

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return

                # Listening for when a key is pressed down on the keyboard
                elif event.type == pygame.KEYDOWN:
                    # If the UP arrow key is pressed, we're decreasing our y coordinate
                    if event.key == pygame.K_UP and self.snake.direction != 3:
                        self.snake.direction = 1
                    # The DOWN arrow key pressed, on the other hand, increases the position on the Y-axis
                    elif event.key == pygame.K_RIGHT and self.snake.direction != 4:
                        self.snake.direction = 2
                    # The DOWN arrow key pressed, on the other hand, increases the position on the Y-axis
                    elif event.key == pygame.K_DOWN and self.snake.direction != 1:
                        self.snake.direction = 3
                    # The DOWN arrow key pressed, on the other hand, increases the position on the Y-axis
                    elif event.key == pygame.K_LEFT and self.snake.direction != 2:
                        self.snake.direction = 4

            self.display()
            self.update()

            pygame.display.update()

            self.clock.tick(5 + (self.score // 10))

