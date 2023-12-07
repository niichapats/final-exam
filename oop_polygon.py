import turtle
import random

class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.border_size = random.randint(1, 10)
        self.a_location = []
        self.a_size = 0

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

        turtle.speed(100)
    turtle.bgcolor('black')
    turtle.tracer(100)
    turtle.colormode(255)

    # def color(self):
    #     return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    #use for drawing a smaller polygon inside the one above
    def advance_location(self):
        reduction_ratio = 0.618
        turtle.penup()
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.right(90)
        self.a_location[0] = turtle.pos()[0]
        self.a_location[1] = turtle.pos()[1]

    #use for drawing a smaller polygon inside the one above
    def advance_size(self):
        reduction_ratio = 0.618
        self.a_size *= reduction_ratio

    def draw_advance_polygon(self):
        turtle.penup()
        turtle.goto(self.a_location[0], self.a_location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.a_size)
            turtle.left(360/self.num_sides)
        turtle.penup()

        turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)



###### main #######

input = int(input(('Which art do you want to generate? Enter a number between 1 to 8, inclusive: ')))

if input == 1:
    while True:
        turtle.clear()
        for i in range(10):
            object1 = Polygon(3)
            object1.draw_polygon()
        turtle.update()
    turtle.done()
elif input == 2:
    while True:
        turtle.clear()
        for i in range(10):
            object1 = Polygon(4)
            object1.draw_polygon()
        turtle.update()
    turtle.done()
elif input == 3:
    while True:
        turtle.clear()
        for i in range(10):
            object1 = Polygon(5)
            object1.draw_polygon()
        turtle.update()
    turtle.done()

#
# while True:
#     turtle.clear()
#     for i in range(10):
#         object1 = Polygon(4)
#         object1.draw_polygon()
#     turtle.update()
# turtle.done()

# while True:
#     turtle.clear()
#     for i in range(10):
#         object1 = Polygon(4)
#         object1.draw_advance_polygon()
#     turtle.update()
# turtle.done()

