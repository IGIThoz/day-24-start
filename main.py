import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# TODO 1: Setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

food = Food()
score = Scoreboard()
# TODO 3: control snake with keyboard
screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")



# TODO 2: Snake run
is_run = True
while is_run:
    screen.update()
    time.sleep(0.1)
    snake.move()

# TODO: 4 Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
# TODO: 5 Keep Score



# TODO: 6 Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # is_run = False
        # score.game_over()
        score.reset()
        snake.reset()
# TODO: 7 Detect collision with tail
    for segment in snake.segments[1:]: # use Slice List python
        if snake.head.distance(segment) <10:
            # is_run = False
            # score.game_over()
            score.reset()
            snake.reset()
# screen.exitonclick() sdasdasd