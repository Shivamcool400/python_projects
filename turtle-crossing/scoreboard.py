from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.lev()

    def lev(self):
        self.write(f"level: {self.level}", align="left", font=FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.lev()
    def gameover(self):
        self.goto(-10, 0)
        self.write("gameover", align="left", font=FONT)


