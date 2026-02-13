from turtle import Turtle

class ScoreBoard:
    def __init__(self):
        self.__score = Turtle()
        self.__score.hideturtle()
        self.__score.penup()
        self.__score.color("white")
        self.__score.goto(0,260)
        self.score(0)

    def score(self, score):
        self.__score.clear()
        self.__score.write(
        f"Score: {score}",
        align="center",
        font=("Arial", 24, "bold")
        )

    def game_over(self):
        self.__score.goto(0,0)
        self.__score.write(
            f"GameOver!",
            align="center",
            font=("Arial", 24, "bold")
        )