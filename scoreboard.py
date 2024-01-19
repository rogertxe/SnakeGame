from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = int(open("data.txt", "r").read())
        self.hideturtle()
        self.setpos(0, 280)
        self.color("white")
        self.print_scoreboard()

    def update_score(self):
        self.score += 1
        self.print_scoreboard()

    def print_scoreboard(self):
        self.clear()
        self.highest_score = int(open("data.txt", "r").read())
        self.write(f"Score: {self.score} Highest score: {self.highest_score}", align="center",
                   font=('Courier', 11, 'bold'))

    def reset(self):
        if self.score > self.highest_score:
            open("data.txt", mode="w").write(str(self.score))
        self.score = 0
        self.print_scoreboard()

    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.write("GAME OVER", align="center", font=('Courier', 16, 'bold'))

