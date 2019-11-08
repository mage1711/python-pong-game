import turtle
import winsound
wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
score_a = 0
score_b = 0
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)

player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("white")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 6
ball.dy = 6

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player 1: 0 player 2: 0", align="center",
          font=("courier", 24, "normal"))


def player1_up():
    y = player1.ycor()
    y += 45
    player1.sety(y)


def player1_down():
    y = player1.ycor()
    y -= 45
    player1.sety(y)


def player2_up():
    y = player2.ycor()
    y += 45
    player2.sety(y)


def player2_down():
    y = player2.ycor()
    y -= 45
    player2.sety(y)


wn.listen()
wn.onkey(player1_up, "w")
wn.onkey(player1_down, "s")
wn.onkey(player2_up, "Up")
wn.onkey(player2_down, "Down")


while True:
    wn.update
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("pong wall.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("pong wall.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound("pong wall.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("player 1: {} player 2: {}".format(score_a, score_b),
                  align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound("pong wall.wav", winsound.SND_ASYNC)
        pen.clear()

        pen.write("player 1: {} player 2: {}".format(score_a, score_b),
                  align="center", font=("courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pong wall.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pong wall.wav", winsound.SND_ASYNC)
    if score_a == 5:
        score_a = 0
        score_b = 0
        ball.dx = 0
        ball.dy = 0
        pen.clear()
        pen.write("you won", align="center", font=("courier", 24, "normal"))
        winsound.PlaySound("win.wav", winsound.SND_ASYNC)
    if score_b == 5:
        score_a = 0
        score_b = 0
        ball.dx = 0
        ball.dy = 0
        pen.clear()
        pen.write("you won", align="center", font=("courier", 24, "normal"))
        winsound.PlaySound("win.wav", winsound.SND_ASYNC)


delay = raw_input("press enter to quit")
