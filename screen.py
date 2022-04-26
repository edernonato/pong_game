from turtle import Turtle, Screen
# Todo: 1 - Create the screen

tim = Turtle()
tim.color("white")
tim.penup()
tim.pensize(5)
tim.goto(0, 300)
tim.right(90)
for _ in range(40):
    tim.pendown()
    tim.forward(15)
    tim.penup()
    tim.forward(15)

screen = Screen()
screen.listen()
screen.tracer(0)

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
