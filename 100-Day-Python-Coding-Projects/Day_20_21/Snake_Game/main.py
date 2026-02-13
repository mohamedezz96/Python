from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)
game_is_on = True

my_snake = Snake()
head_of_snake = my_snake.head()
my_food = Food()
my_food_item = my_food.food()
my_score = ScoreBoard()
score = 0

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.Down, "Down")
my_screen.onkey(my_snake.Right, "Right")
my_screen.onkey(my_snake.Left, "Left")


while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()
    distance = head_of_snake.distance(my_food_item)
    if distance <= 15:
        my_food.change_food_position()
        my_snake.increase_snake()
        score += 1
        my_score.score(score)

    if head_of_snake.xcor() > 280 or head_of_snake.ycor() > 280 or head_of_snake.xcor() < -280 or head_of_snake.ycor() < -280:
        game_is_on = False
        my_score.game_over()

    if my_snake.detect_collision():
        game_is_on = False
        my_score.game_over()


    

my_screen.exitonclick()
