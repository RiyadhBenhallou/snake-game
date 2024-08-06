import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen

WALL_POSITIONS = [300, -300]

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.right, 'd')
screen.onkey(snake.left, 'a')
screen.listen()

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.125)

  snake.move()
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increment()


  if snake.head.xcor() in WALL_POSITIONS or snake.head.ycor() in WALL_POSITIONS:
    scoreboard.game_over()  
    game_is_on = False

  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      scoreboard.game_over()  
      game_is_on = False
    

screen.exitonclick()