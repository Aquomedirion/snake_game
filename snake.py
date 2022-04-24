from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for snake_loop in STARTING_POSITIONS:
            new_snake = Turtle()
            new_snake.shape("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(snake_loop)
            self.snake_body.append(new_snake)

    def move(self):
        for snake_step in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_step - 1].xcor()
            new_y = self.snake_body[snake_step - 1].ycor()
            self.snake_body[snake_step].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
