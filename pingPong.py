import turtle
import time
#import random

win = turtle.Screen()
win.title("Ping Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Global variable
scoreA = 0
scoreB = 0

# Pad A
padA = turtle.Turtle()
padA.speed(0)
padA.shape("square")
padA.color("white")
padA.shapesize(stretch_wid=5, stretch_len=1)
padA.penup()
padA.goto(-350, 0)

# Pad B
padB = turtle.Turtle()
padB.speed(0)
padB.shape("square")
padB.color("white")
padB.shapesize(stretch_wid=5, stretch_len=1)
padB.penup()
padB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A : 0  Player B: 0", align="center", font=("Sans Serif", 17, "normal"))

# Functions
def padA_up():
    y = padA.ycor()
    if y < 250:  # Ensure the paddle doesn't go off the screen
        y += 30
    padA.sety(y)

def padA_down():
    y = padA.ycor()
    if y > -240:  # Ensure the paddle doesn't go off the screen
        y -= 30
    padA.sety(y)

def padB_up():
    y = padB.ycor()
    if y < 250:  # Ensure the paddle doesn't go off the screen
        y += 30
    padB.sety(y)

def padB_down():
    y = padB.ycor()
    if y > -240:  # Ensure the paddle doesn't go off the screen
        y -= 30
    padB.sety(y)

def displayMenu():
    global running
    if not running:
        pen.clear()
        pen.goto(0,0)
        pen.write("Ping Pong Game\nPress Space to Start", align="center",font = ("Sans Serif", 24, "normal"))


def startGame():
    global scoreA, scoreB, running
    scoreB = 0
    scoreA = 0
    pen.clear()
    pen.goto(0, 250)
    pen.write("Player A : 0  Player B : 0",align=("Center"), font = ("Sans Serif", 17, "normal"))
    running = True

def restartGame():
    global running
    pen.clear()
    pen.goto(0,0)
    if scoreA == 10:
        pen.write(f"Player A Wins!\nGame will restart soon", align="center", font=("Sans Serif", 24, "normal"))
    elif scoreB == 10:
        pen.write(f"Player B Wins!\nGame will restart soon", align="center", font=("Sans Serif", 24, "normal"))
    win.update()
    running = False
    win.ontimer(displayMenu, 2000)
# Binding
win.listen()
win.onkeypress(padA_up, "w")
win.onkeypress(padA_down, "s")
win.onkeypress(padB_up, "Up")
win.onkeypress(padB_down, "Down")
win.onkeypress(startGame, "space")

#First Time Menu
running = False
displayMenu()


# Main game loop
while True:
    win.update()
    if not running:
        continue
    
    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Control
        # Y Movement
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
        # X Movement
    if ball.xcor() > 390:
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A : {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Sans Serif", 17, "normal"))
        if scoreA == 10:
            restartGame()

    if ball.xcor() < -390:
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A : {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Sans Serif", 17, "normal"))
        if scoreB == 10:
            restartGame()

        # Pad Collisions
    if (ball.dx > 0) and (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < padB.ycor() + 50 and ball.ycor() > padB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        ball.dx *= 1.1  # Increase speed slightly
        ball.dy *= 1.1

    if (ball.dx < 0) and (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < padA.ycor() + 50 and ball.ycor() > padA.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        ball.dx *= 1.1  # Increase speed slightly
        ball.dy *= 1.1