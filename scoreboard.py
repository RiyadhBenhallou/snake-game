from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 18, 'normal')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = 0
    self.penup()
    self.goto(0, 270)
    self.color('white')
    self.hideturtle()
    self.update()

  def update(self):
    self.clear()
    self.write(f'Score: {self.score}, Highest Score: {self.high_score}', align= ALIGNMENT, font=FONT)

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
    self.score = 0  
    self.update()

  def increment(self):
    self.score += 1
    self.update()

  # def game_over(self):
  #   self.clear()
  #   self.penup()
  #   self.color('white')
  #   self.hideturtle()
  #   self.goto((0, 0))
  #   self.write('GAME OVER', align= ALIGNMENT, font=FONT)