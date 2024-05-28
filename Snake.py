from tkinter import *
import random

# Constants (Can Change them According to will)
GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 100              # Lower number, faster game
SPACE_SIZE = 50         # 800/50 = 16 possible locations for food
BODY_PARTS = 3          # Initial Body parts of snake
SNAKE_COLOR = "#00FF00"
FOOD_COLOUR = "#FF0000"
BG_COLOUR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Creating Coordinates
        self.coordinates.append([100, 100])  # Head at (100, 100)

        # Creating subsequent body parts, positioned to the right
        for i in range(1, BODY_PARTS):
            self.coordinates.append([100 - SPACE_SIZE * i, 100])

        # Creating squares
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="Snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]       # Giving Random Coordinates for food to spawn
        
        # Creating Food Object
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag="food")

def nextTurn(snake, food):
    x, y = snake.coordinates[0]

    if dir == "up":
        y -= SPACE_SIZE
    elif dir == "down":
        y += SPACE_SIZE
    elif dir == "left":
        x -= SPACE_SIZE
    elif dir == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score : {}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if checkCollisions(snake):
        gameOver()
    else:
        win.after(SPEED, nextTurn, snake, food)

def changeDir(newDir):
    global dir

    if newDir == 'left':
        if dir != 'right':
            dir = newDir
    elif newDir == 'right':
        if dir != 'left':
            dir = newDir
    elif newDir == 'up':
        if dir != 'down':
            dir = newDir
    elif newDir == 'down':
        if dir != 'up':
            dir = newDir

def checkCollisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for bodyPart in snake.coordinates[1:]:
        if x == bodyPart[0] and y == bodyPart[1]:
            return True

    return False

def gameOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=("Sans Serif", 40), text="Game Over!", fill="red", tag="over")
    win.update()

win = Tk()
win.title("Snake Game")
win.resizable(False, False)         # Game won't be resizable

score = 0
dir = "down"
label = Label(win, text="Score : {}".format(score), font=('Sans Serif', 40))
label.pack()
canvas = Canvas(win, bg=BG_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
win.update()

win_width = win.winfo_width()
win_height = win.winfo_height()
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# Making the window Centered
x = int((screen_width / 2) - (win_width / 2))
y = int((screen_height / 2) - (win_height / 2))
win.geometry(f"{win_width}x{win_height}+{x}+{y}")

win.bind('<Left>', lambda event: changeDir('left'))
win.bind('<Right>', lambda event: changeDir('right'))
win.bind('<Up>', lambda event: changeDir('up'))
win.bind('<Down>', lambda event: changeDir('down'))

snake = Snake()
food = Food()
nextTurn(snake, food)

win.mainloop()
