import copy

class Board:
    def __init__(self, snakey, apple, width=5, height=10):
        self.width = width
        self.height = height
        self.snake = snakey
        self.apple = apple
        self.board = [["." for i in range(width)] for j in range(height)]
        self.set = set()
        self.border = "X" * (self.width + 4)
        self.update()
        for i in range(width):
            for k in range(height):
                self.set.add((i,k))

    def update(self):
        for i in range(self.height):
            for j in range(self.width):
                if (j,i) in self.snake.list:
                    if (j, i) == self.snake.list[0]:
                        self.board[i][j] = "S"
                    else:
                        self.board[i][j] = "s"
                elif (j, i) == self.apple.coords:
                    self.board[i][j] = "A"
                else:
                    self.board[i][j] = "."

    def render(self):
        print(self.border)
        for row in self.board:
            print("X ", end="")
            for col in row:
                print(col, end="")
            print(" X")
        print(self.border)