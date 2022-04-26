from paddle import Paddle
from ball import Ball
from score import Scoreboard, game_on
from screen import screen
import time


paddle = Paddle()
screen.onkey(fun=paddle.left_up, key="w")
screen.onkey(fun=paddle.left_down, key="s")
screen.onkey(fun=paddle.right_up, key="Up")
screen.onkey(fun=paddle.right_down, key="Down")

player1 = Scoreboard()
player1.position((-100, 250))
player2 = Scoreboard()
player2.position((100, 250))

ball = Ball()

while game_on:
    screen.update()
    ball.move()

    for instance in paddle.instances_left:
        if ball.distance(instance.pos()) < 20:
            if ball.heading() == 225:
                ball.change_heading(90)
            elif ball.heading() == 135:
                ball.change_heading(-90)
            ball.increase_speed()
    for instance in paddle.instances_right:
        if ball.distance(instance.pos()) < 20:
            if ball.heading() == 315:
                ball.change_heading(-90)
            elif ball.heading() == 45:
                ball.change_heading(90)
            ball.increase_speed()
    for player in player1, player2:
        if player.score == 10:
            player.game_over()
            game_on = False

    if ball.xcor() >= 400:
        player1.increase_score()
        ball.refresh()
    if ball.xcor() <= -400:
        player2.increase_score()
        ball.refresh()
    time.sleep(0.01)

screen.exitonclick()
