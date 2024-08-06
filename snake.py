from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.last_position = (-40, 0)
    
    
    
  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)
    self.head = self.segments[0]

  def add_segment(self, position):
    new_segment = Turtle()
    new_segment.penup()
    new_segment.color('white')
    new_segment.shape('square')
    new_segment.goto(position)
    self.segments.append(new_segment)

  def extend(self):
    self.add_segment(self.segments[-1].position())

  def move(self):
    for i in range(len(self.segments) - 1, 0, -1):
      x = self.segments[i - 1].xcor()
      y = self.segments[i - 1].ycor()
      self.segments[i].goto(x, y)

    self.head.forward(10)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
    # screen.update()
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
    # screen.update()
  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
    # screen.update()
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
    # screen.update()