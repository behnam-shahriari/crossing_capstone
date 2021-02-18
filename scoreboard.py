from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align="center", font=FONT)

