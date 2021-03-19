from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake = Snake()
food = Food()
text = Turtle()
text.goto(0, 270)
text.color("white")
text.hideturtle()
screen.listen()
screen.onkey(snake.change_heading_up, "Up")
screen.onkey(snake.change_heading_down, "Down")
screen.onkey(snake.change_heading_left, "Left")
screen.onkey(snake.change_heading_right, "Right")
screen.onkey(snake.extend_snake, "c")  
score = 0
text.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    if snake.check_collision() or snake.check_self_collision():
        print("wall collision")
        text.goto(0,0)
        text.write(f"GAME OVER", align="center", font=("Arial", 26, "normal"))
        game_on = False
    if snake.head.distance(food) < 15:
        score += 1
        food.change_position()
        snake.extend_snake()
        text.clear()
        text.write(f"Score: {score}", align="center", font=("Arial", 14, "normal"))
        
    snake.move()

screen.exitonclick()