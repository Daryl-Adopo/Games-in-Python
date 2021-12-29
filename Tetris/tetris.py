import turtle
import time
import random

# Shapes
S = [[1, 1, 0],
     [0, 1, 1]]

Z = [[0, 1, 1],
     [1, 1, 0]]

I = [[1, 1, 1, 1]]

O = [[1, 1],
     [1, 1]]

J = [[0, 1],
     [0, 1],
     [1, 1]]

L = [[1, 0],
     [1, 0],
     [1, 1]]

T = [[1, 1, 1],
     [0, 1, 0]]

shapes = [S, Z, I, O, J, L, T]
colors = ['black', 'green', 'red', 'lightblue', 'yellow', 'blue', 'orange', 'purple']


class Shape:
    def __init__(self, shape):
        self.y = 0
        self.x = 5

        self.shape = shape
        self.color = shapes.index(shape) + 1

        self.height = len(shape)
        self.width = len(shape[0])

    def can_move_left(self, grid):
        result = True
        for y in range(self.height):
            if self.shape[y][0] == 1:
                if grid[self.y + y][self.x - 1] != 0:
                    result = False
            else:
                if grid[self.y + y][self.x] != 0:
                    result = False
        return result

    def can_move_right(self, grid):
        result = True
        for y in range(self.height):
            for x in range(self.width, 0, -1):
                if self.shape[y][x - 1] == 1:
                    if grid[self.y + y][self.x + x] != 0:
                        result = False
                    break
                else:
                    if grid[self.y + y][self.x + x - 1] != 0:
                        result = False
        return result

    def move_left(self, grid):
        if self.x > 0:
            if self.can_move_left(grid):
                self.erase_shape(grid)
                self.x -= 1

    def move_right(self, grid):
        if self.x < cols - self.width:
            if self.can_move_right(grid):
                self.erase_shape(grid)
                self.x += 1

    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    grid[self.y + y][self.x + x] = self.color

    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if grid[self.y + y][self.x + x] == self.color:
                    grid[self.y + y][self.x + x] = 0

    def can_drop(self, grid):
        result = True
        for x in range(self.width):
            if self.shape[self.height - 1][x] == 1:
                if grid[self.y + self.height][self.x + x] != 0:
                    result = False
            elif self.shape[self.height - 2][x] == 1:
                if grid[self.y + self.height - 1][self.x + x] != 0:
                    result = False
            elif self.shape[self.height - 3][x] == 1:
                if grid[self.y + self.height - 2][self.x + x] != 0:
                    result = False
        return result

    def rotated(self):
        rotated_shape = []
        for x in range(len(self.shape[0])):
            new_row = []
            for y in range(len(self.shape) - 1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)
        return rotated_shape

    def can_rotate(self, grid):
        rotated_shape = self.rotated()

        right_side = self.x + len(rotated_shape[0])
        bottom = self.y + len(rotated_shape)

        cond0 = (bottom < rows)
        cond1 = (right_side - 1 < cols)
        cond2 = [True]
        cond3 = [True]

        if self.width < len(rotated_shape[0]) and cond1:
            for x in range((len(rotated_shape[0]) - 1), self.width - 1, -1):
                cond2.append(grid[self.y][self.x + x] == 0)

        elif self.height < len(rotated_shape) and cond0:
            for y in range((len(rotated_shape) - 1), (self.height - 1), -1):
                cond3.append(grid[self.y + y][self.x] == 0)

        return cond0 and cond1 and (not (False in cond2)) and (not (False in cond3))

    def rotate(self, grid):
        self.erase_shape(grid)
        rotated_shape = self.rotated()

        if self.can_rotate(grid):
            self.shape = rotated_shape
            self.height = len(self.shape)
            self.width = len(self.shape[0])

    def draw_next_rotation(self, pen):
        pen.clear()
        rotated_shape = self.rotated()

        screen_x = -220
        screen_y = -100

        for y in range(len(rotated_shape)):
            for x in range(len(rotated_shape[0])):
                if rotated_shape[y][x] == 1:
                    pen.color('white', colors[self.color])
                    pen.goto(screen_x + x * 20, screen_y - y * 20)
                    pen.stamp()

                    draw(pen, 'Next \nRotation', screen_x, screen_y + 20)

    def drop_shape(self, grid):
        global myShape, nextShape, myScore
        if self.y == rows - self.height:
            myShape = nextShape
            nextShape = get_shape()
            myScore += 5

        elif self.can_drop(grid):
            self.erase_shape(grid)
            self.y += 1

        else:
            myShape = nextShape
            nextShape = get_shape()
            myScore += 5

    def to_the_bottom(self, grid):
        while self.can_drop(grid):
            self.drop_shape(grid)


# Functions
def draw_grid(pen, grid):
    pen.clear()
    top = (rows * 20) / 2
    left = -(cols * 20) / 2

    for y in range(rows):
        for x in range(cols):
            screen_x = left + (x * 20)
            screen_y = top - (y * 20)

            color = int(grid[y][x])
            pen.color('white', colors[color])
            pen.goto(screen_x, screen_y)
            pen.stamp()


def delete_row(grid, row):
    for i in range(cols):
        grid[row][i] = 0
    if row == 0:
        return True
    for r in range(row, 0, -1):
        for i in range(cols):
            grid[r][i] = grid[r - 1][i]
    for i in range(cols):
        grid[0][i] = 0


def delete_full_row(grid):
    for r in range(rows - 1, -1, -1):
        if 0 not in grid[r]:
            delete_row(grid, r)
            return True


def game_over(grid, shape):
    game_over = False
    for c in range(cols - 1):
        if grid[1][c] and grid[0][c] and not shape.can_drop(grid):
            game_over = True
    return game_over


def draw_score(pen, font, score):
    draw(pen, f'Score: {score}', 0, 270, 'yellow', 'center', font)


def draw(pen, text, x, y, color='white', align='left', font=('Arial', 15, 'normal')):
    pen.hideturtle()
    pen.goto(x, y)
    pen.color(color)
    pen.write(text, align=align, font=font)


def draw_next_shape(pen):
    pen.clear()

    screen_x = -220
    screen_y = 100

    for y in range(nextShape.height):
        for x in range(nextShape.width):
            if nextShape.shape[y][x] == 1:
                pen.color('white', colors[nextShape.color])
                pen.goto(screen_x + x * 20, screen_y - y * 20)
                pen.stamp()

                draw(pen, 'Next \nShape', screen_x, screen_y + 20)


def draw_game_over(pen, font):
    draw(pen, 'GAME OVER', 0, -270, 'yellow', 'center', font)


dropping = True


def disable_drop():
    global dropping
    dropping = False


def enable_drop():
    global dropping
    dropping = True


def get_shape():
    return Shape(random.choice(shapes))


# Create Screen
width, height = 480, 600
wn = turtle.Screen()
wn.setup(width, height)
wn.title('Tetris by Daryl :)')
wn.bgcolor('black')
wn.tracer(0)

# Pens
myPen = turtle.Turtle()
myPen.speed(0)
myPen.penup()
myPen.shape('square')
myPen.color('white')

nextPen = turtle.Turtle()
nextPen.speed(0)
nextPen.penup()
nextPen.shape('square')
nextPen.color('white', 'black')

rotationPen = turtle.Turtle()
rotationPen.speed(0)
rotationPen.penup()
rotationPen.shape('square')
rotationPen.color('white', 'black')

# Tetris Grid
myGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

rows = len(myGrid)
cols = len(myGrid[0])

# Initial Shape Object
myShape = get_shape()
nextShape = get_shape()

# Keybindings
wn.onkeypress(lambda: myShape.move_left(myGrid), 'q')
wn.onkeypress(lambda: myShape.move_right(myGrid), 'd')
wn.onkeypress(lambda: myShape.rotate(myGrid), 'space')

wn.onkeypress(lambda: disable_drop(), 'p')
wn.onkeypress(lambda: enable_drop(), 'e')
wn.onkeypress(lambda: myShape.drop_shape(myGrid), 's')
wn.onkeypress(lambda: myShape.to_the_bottom(myGrid), 'x')

# Game Layout
myScore = 0
myFont = ('Arial', 20, 'normal')

# Main Game Loop
while True:
    time.sleep(1 / 20)
    wn.update()
    wn.listen()

    myShape.draw_shape(myGrid)

    draw_grid(myPen, myGrid)

    draw_score(myPen, myFont, myScore)
    draw_next_shape(nextPen)
    myShape.draw_next_rotation(rotationPen)

    if dropping:
        myShape.drop_shape(myGrid)

    if delete_full_row(myGrid):
        myScore += cols * 10

    if game_over(myGrid, myShape):
        draw_game_over(myPen, myFont)
        time.sleep(2)
        break
