from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Score: {self.points}", align=ALIGN, font=FONT)

    def update_score(self):
        self.points += 1
        self.clear()
        self.scoreboard()

    def endgame(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGN, font=("Courier", 20, "normal"))