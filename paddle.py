from turtle import Turtle
# Todo: 2 - Create and move a paddle

START_POSITIONS = (- 370, 370)


class Paddle:
    def __init__(self):
        self.instances_left = []
        self.instances_right = []
        self.sides = []
        for position in START_POSITIONS:
            self.create_paddle(position)
        self.paddle_left_up = self.instances_left[0]
        self.paddle_left_down = self.instances_left[len(self.instances_left) - 1]
        self.paddle_right_up = self.instances_right[0]
        self.paddle_right_down = self.instances_right[len(self.instances_left) - 1]

    def left_up(self):
        self.paddle_move_up("left")

    def left_down(self):
        self.paddle_move_down("left")

    def right_up(self):
        self.paddle_move_up("right")

    def right_down(self):
        self.paddle_move_down("right")

    def paddle_move_up(self, side):
        if side == "left":
            self.paddle_left_up.setheading(90)
            if self.paddle_left_up.ycor() < 300:
                for instance in range(len(self.instances_left) - 1, 0, -1):
                    new_pos = self.instances_left[instance - 1].pos()
                    self.instances_left[instance].goto(new_pos)
                self.paddle_left_up.forward(20)
        elif side == "right":
            self.paddle_right_up.setheading(90)
            if self.paddle_right_up.ycor() < 300:
                for instance in range(len(self.instances_right) - 1, 0, -1):
                    new_pos = self.instances_right[instance - 1].pos()
                    self.instances_right[instance].goto(new_pos)
                self.paddle_right_up.forward(20)

    def paddle_move_down(self, side):
        if side == "left":
            self.paddle_left_down.setheading(270)
            if self.paddle_left_down.ycor() > -280:
                for instance in range(0, len(self.instances_left) - 1, 1):
                    new_pos = self.instances_left[instance + 1].pos()
                    self.instances_left[instance].goto(new_pos)
                self.paddle_left_down.forward(20)
        elif side == "right":
            self.paddle_right_down.setheading(270)
            if self.paddle_right_down.ycor() > -280:
                for instance in range(0, len(self.instances_right) - 1, 1):
                    new_pos = self.instances_right[instance + 1].pos()
                    self.instances_right[instance].goto(new_pos)
                self.paddle_right_down.forward(20)

    def create_paddle(self, side):
        y = 20
        for _ in range(5):
            paddle = Turtle(shape="square")
            paddle.speed("fastest")
            paddle.color("white")
            paddle.penup()
            if side == -370:
                paddle.goto(side, y)
                self.instances_left.append(paddle)
            elif side == 370:
                paddle.goto(side, y)
                self.instances_right.append(paddle)
            y -= 20
