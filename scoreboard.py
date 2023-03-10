from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.notescore()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        #self.clear()
        self.update_scoreboard()

    def reset(self):

        if self.score > self.high_score:
            with open("text.txt", mode="w") as file:
            #with open("C:\\Users\dangtb\Desktop\dtext.txt", mode="w") as file:
                file.write(f"{self.score}")
            #self.high_score = self.score
        self.score = 0
        self.high_score = self.notescore()
        self.update_scoreboard()

    def notescore(self):
        file = open("text.txt","r")
        #file = open("C:\\Users\dangtb\Desktop\dtext.txt", "r")
        contents = file.read()
        file.close()
        return int(contents)