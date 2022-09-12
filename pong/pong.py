import turtle
import os


wn = turtle.Screen()
wn.title("Pong By SmashedFrenzy16")
wn.bgcolor("black")
wn.setup(width=800, height=600)

wn.tracer(0)

# Score

score_1 = 0
score_2 = 0

pen  = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.up()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 | Player 2: 0", align="center", font=("Arial Bold", 24, "normal"))

# Player 1

paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.up()
paddle_1.goto(-350, 0)

# Player 2

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.up()
paddle_2.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.up()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Functions

def paddle_1_up():

    y = paddle_1.ycor()

    y += 20

    paddle_1.sety(y)

    if paddle_1.ycor() >= 300:

        y = 300

        paddle_1.sety(y)

def paddle_1_down():

    y = paddle_1.ycor()

    y -= 20

    paddle_1.sety(y)

    if paddle_1.ycor() <= -300:

        y = -300

        paddle_1.sety(y)

def paddle_2_up():

    y = paddle_2.ycor()

    y += 20

    paddle_2.sety(y)

    if paddle_2.ycor() >= 300:

        y = 300

        paddle_2.sety(y)

def paddle_2_down():

    y = paddle_2.ycor()

    y -= 20

    paddle_2.sety(y)

    if paddle_2.ycor() <= -300:

        y = -300

        paddle_2.sety(y)

wn.listen()

wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")
    

while True:

    wn.update()

    # Ball Core Commands

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:

        ball.sety(290)

        ball.dy *= -1

        os.system("afplay pong.mp3&")

    if ball.ycor() < -290:

        ball.sety(-290)

        ball.dy *= -1

        os.system("afplay pong.mp3&")

    if ball.xcor() > 390:

        ball.goto(0, 0)

        ball.dx *= -1

        score_1 += 1

        pen.clear()

        pen.write("Player 1: {} | Player 2: {}".format(score_1, score_2), align="center", font=("Arial Bold", 24, "normal"))

    if ball.xcor() < -390:

        ball.goto(0, 0)

        ball.dx *= -1

        score_2 += 1

        pen.clear()

        pen.write("Player 1: {} | Player 2: {}".format(score_1, score_2), align="center", font=("Arial Bold", 24, "normal"))
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

        os.system("afplay pong.mp3&")

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

        os.system("afplay pong.mp3&")

    if score_1 == 11 or score_2 == 11:

        pen.clear()

        if score_1 > score_2:

            pen.write("Player 1 Wins!", align="center", font=("Arial Bold", 24, "normal"))

        elif score_1 < score_2:

            pen.write("Player 2 Wins!", align="center", font=("Arial Bold", 24, "normal"))

        
        
