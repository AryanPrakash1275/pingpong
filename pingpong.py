import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(paddle1.go_up, "w")
screen.onkeypress(paddle1.go_down, "s")
screen.onkeypress(paddle2.go_up, "Up")
screen.onkeypress(paddle2.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(paddle2) < 50 and ball.xcor() > 320) or (ball.distance(paddle1) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    if ball.xcor() > 380:  # for paddle 1
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -380:  # for paddle 2
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()
