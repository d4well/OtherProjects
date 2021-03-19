from turtle import Turtle, position

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(0, 3):
            sn = Turtle(shape="square")
            sn.color("white")
            sn.penup()
            sn.goto(START_POS[i])
            self.snake.append(sn)


    def move(self):
        for num in range(len(self.snake)-1, 0, -1):
            new_pos = self.snake[num - 1].pos()
            self.snake[num].goto(new_pos)
        self.head.forward(MOVE_DIS)


    def change_heading_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def change_heading_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def change_heading_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def change_heading_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def check_collision(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 \
            or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
    
    def check_self_collision(self):
        for seg in self.snake[1::]:   
            if self.head.distance(seg) < 10:
                return True

    def extend_snake(self):
        sn = Turtle(shape="square")
        sn.color("white")
        sn.penup()
        sn.setheading(self.snake[-1].heading())
        if self.head.heading() == LEFT:
            sn.goto(self.snake[-1].xcor() + 20, self.snake[-1].ycor())
        elif self.head.heading() == RIGHT:
            sn.goto(self.snake[-1].xcor() - 20, self.snake[-1].ycor())
        elif self.head.heading() == DOWN:
            sn.goto(self.snake[-1].xcor(), self.snake[-1].ycor() + 20)
        elif self.head.heading() == UP:
            sn.goto(self.snake[-1].xcor(), self.snake[-1].ycor() - 20)
        self.snake.append(sn)
        

