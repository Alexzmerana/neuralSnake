from board import Board
from snake import Snake
from apple import Apple
import os
from pynput import keyboard
import time

class Game:


    def __init__(self) -> None:
        self.FPS = 10
        self.width = 40
        self.height = self.width // 2
        self.score = 0
        self.snake = Snake()
        self.apple = Apple((self.width // 2, self.height // 2))
        self.board = Board(self.snake, self.apple, self.width, self.height)


    def clearScreen(self):
        print("\033[H\033[3J", end="")

    def update(self):
        self.snake.move()
        self.board.update()

    def collision(self):
        head = self.snake.list[0]

        if(head in self.snake.list[1:]): return True

        elif(-1 >= head[0] or head[0] >= self.width): return True

        elif(-1 >= head[1] or head[1] >= self.height): return True

        if head == self.apple.coords:
            self.snake.grow()
            self.score += 1
            self.apple.coords = self.board.set.difference(set(self.snake.list)).pop()

        return False

    def run(self):
        while not self.collision():
            self.board.render()

            self.update()

            time.sleep(1/(self.FPS + self.score // 2))
            self.clearScreen()
        os.system('clear')
        print("Score:", self.score)

game = Game()

def on_press(key):
    if key == keyboard.Key.right and game.snake.direction != 4:
        game.snake.direction = 2
    elif key == keyboard.Key.left and game.snake.direction != 2:
        game.snake.direction = 4
    elif key == keyboard.Key.up and game.snake.direction != 3:
        game.snake.direction = 1
    elif key == keyboard.Key.down and game.snake.direction != 1:
        game.snake.direction = 3



listener = keyboard.Listener(
    on_press=on_press)
listener.start()

game.run()
