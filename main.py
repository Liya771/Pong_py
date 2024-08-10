from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("pong")
screen.setup(width=800,height=600)
screen.tracer(0)

r_paddle=Paddle((350, 0))
l_paddle=Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.forward, "Up")
screen.onkey(r_paddle.backward, "Down")
screen.onkey(l_paddle.forward, "w")
screen.onkey(l_paddle.backward, "s")


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision by wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    # R miss the paddle
    if ball.xcor() > 380:
        ball.reset_pos()

    # L miss paddle
    if ball.xcor() < -380:
        ball.reset_pos()


screen.exitonclick()