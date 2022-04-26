from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 30, 'normal')
game_on = True


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.color("white")

    def position(self, position):
        self.setpos(position)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align="Center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
