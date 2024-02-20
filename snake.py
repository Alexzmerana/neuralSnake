class Snake:
    def __init__(self) -> None:
        self.list = [(1, 0), (0, 0)]
        self.direction = 2

    def move(self):

        if self.direction == 1:   # Moving north
            self.list.pop()
            oldHead = self.list[0]
            self.list.insert(0, (oldHead[0], oldHead[1] - 1))

        elif self.direction == 2: # Moving east
            self.list.pop()
            oldHead = self.list[0]
            self.list.insert(0, (oldHead[0] + 1, oldHead[1]))

        elif self.direction == 3: # Moving south
            self.list.pop()
            oldHead = self.list[0]
            self.list.insert(0, (oldHead[0], oldHead[1] + 1))

        else:   # Moving west
            self.list.pop()
            oldHead = self.list[0]
            self.list.insert(0, (oldHead[0] - 1, oldHead[1]))

    def grow(self):
        self.list.append(self.list[-1])