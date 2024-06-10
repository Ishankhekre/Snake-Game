from turtle import Turtle, Screen

screen = Screen()
mov = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            screen.update()

        self.head.forward(mov)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
