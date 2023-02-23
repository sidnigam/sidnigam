from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(0,275)

    def update_scoreboard(self):
        self.clear()
        self.text = ("Arial", 20, "bold")
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.write(arg=f"Your score: {self.score}, High score: {self.high_score} ", move=False, align="center", font=self.text)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode = "w") as file:
                file.write(str(self.score))                
        self.score = 0
        self.update_scoreboard()
