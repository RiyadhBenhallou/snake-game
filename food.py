from turtle import Turtle
from random import randint

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.shapesize(0.5, 0.5)
    self.color('blue')
    self.penup()
    self.refresh()

  def refresh(self):
    x = randint(-280, 280)
    y = randint(-280, 280)
    self.goto(x, y)