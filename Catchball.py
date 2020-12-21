import turtle
import time
from time import sleep


wn = turtle.Screen()
wn.title("Catch It")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#scores
score = 0


# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.color("white")
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#ball movement
ball.dx = 0.2
ball.dy = 0.2
#how to make balistic mv/gravity effect

# Functions

def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)
    if paddle.xcor() > 350:
        paddle.setx(350)

def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)
    if paddle.xcor() < -350:
        paddle.setx(-350)



wn.listen()
wn.onkeypress(paddle_right, "6")
wn.onkeypress(paddle_left, "4")





# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Your Score: 0", align="center", font=("Courier", 24, "normal"))

#main loop
while True:
    wn.update()
    # moving the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.ycor() < -300:
        ball.goto(0, 300)
        pen.clear()
        score = 0
        sleep(1)
        pen.write("You lost. Get ready for another round!", align="center",
                  font=("Courier", 24, "normal"))
        sleep(1)
        pen.clear()
        pen.write("Your Score: 0", align="center", font=("Courier", 24, "normal"))
        sleep(1)
        continue

#Paddle-ball collision
    if ball.ycor() < -240 and ball.xcor() > -250 and (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() -50):
        ball.sety(-240)
        ball.dy *= -1
        score += 1
        pen.clear()
        pen.write("Your Score: {}".format(score), align="center",
                  font=("Courier", 24, "normal"))
    if score == 3:
        ball.goto(0, 0)
        pen.clear()
        pen.write("You Won!", align="center", font=("Courier", 24, "normal"))
        sleep(2)
        break


















