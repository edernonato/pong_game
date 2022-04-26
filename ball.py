from turtle import Turtle
from random import choice

HEADINGS = [45, 135, 225, 315]



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(choice(HEADINGS))
        self.settiltangle(self.heading())
        self.move_speed = 2

    def move(self):
        self.forward(self.move_speed)
        if self.ycor() >= 280 or self.ycor() <= -280:
            current_heading = self.heading()
            if current_heading == 225 and self.ycor() <= -250 or current_heading == 45 and self.ycor() >= 250:
                self.change_heading(-90)
            else:
                self.change_heading(45)

    def change_heading(self, angle):
        current_heading = self.heading()
        self.setheading(current_heading + angle)
        self.settiltangle(self.heading())
        print(self.heading())

    def refresh(self):
        self.goto(0, 0)
        self.setheading(choice(HEADINGS))
        self.move_speed = 2

    def increase_speed(self):
        self.move_speed += 2
