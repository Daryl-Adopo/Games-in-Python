# First Game in Python :)

import turtle
import winsound
import time

# Screen
wn = turtle.Screen()
wn.title("Pong by Daryl :)")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = [1, 0]
score_b = [2, 0]

# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -5
ball.dy = 5

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write(f"{score_a[1]} : {score_b[1]}", align="center", font=("Courier", 36, "normal"))


# Function
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)


def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)


def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)


def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(pad_a_up, "z")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")

game_over = False
# Main Game Loop
while not game_over:
    time.sleep(1 / 60)

    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 290:
        winsound.PlaySound("Wall", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        winsound.PlaySound("Wall", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1

    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a[1] += 1
        pen.clear()
        pen.write(f"{score_a[1]} : {score_b[1]}", align="center", font=("Courier", 36, "normal"))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b[1] += 1
        pen.clear()
        pen.write(f"{score_a[1]} : {score_b[1]}", align="center", font=("Courier", 36, "normal"))

    # Border Controls for Paddles
    if pad_a.ycor() > 250:
        pad_a.sety(250)

    elif pad_a.ycor() < -250:
        pad_a.sety(-250)

    elif pad_b.ycor() > 250:
        pad_b.sety(250)

    elif pad_b.ycor() < -250:
        pad_b.sety(-250)

    # Paddle and Ball Collision
    col_a_x = (-350 < ball.xcor() < -340)
    col_a_y = (pad_a.ycor() - 50 < ball.ycor() < pad_a.ycor() + 50)

    col_b_x = (340 < ball.xcor() < 350)
    col_b_y = (pad_b.ycor() - 50 < ball.ycor() < pad_b.ycor() + 50)

    if col_a_x and col_a_y:
        winsound.PlaySound('Wall', winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1

    elif col_b_x and col_b_y:
        winsound.PlaySound('Wall', winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1

    # Win Conditions
    if score_a[1] >= 5 or score_b[1] >= 5:
        game_over = True
        pen.goto(0, 0)
        pen.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
        pen.goto(0, -50)
        if score_a[1] > score_b[1]:
            pen.write(f'Player {score_a[0]} Wins!', align="center", font=("Courier", 36, "normal"))
        else:
            pen.write(f'Player {score_b[0]} Wins!', align="center", font=("Courier", 36, "normal"))
        time.sleep(3)
