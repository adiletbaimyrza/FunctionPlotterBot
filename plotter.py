import turtle
from tkinter import *

DELAY = 0

class EquationVisual:
    def __init__(self, dimensions=50, tick=1, dot_size=3, precision=5, zoom=-5, mode='light'):
        self.dimensions = dimensions
        self.tick = tick
        self.dot_size = dot_size
        self.zoom = zoom
        self.mode = mode
        
        self.x_range = range(-dimensions *  precision, dimensions * precision)
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.precision = precision
        turtle.delay(DELAY)

    def set_dimensions(self, dimensions):
        self.dimensions = dimensions

    def set_tick(self, tick):
        self.tick = tick

    def set_dot_size(self, dot_size):
        self.dot_size = dot_size

    def set_mode(self, mode='light'):
        self.mode = mode

    def open_screen(self, zoom=-5):
        self.zoom = -zoom
        self.screen.setworldcoordinates(-self.dimensions - self.zoom,
                                            -self.dimensions - self.zoom,
                                            self.dimensions + self.zoom,
                                            self.dimensions + self.zoom)

    def plot_equation(self, a, b, c=None):
        self.turtle.pencolor('red')
        self.turtle.showturtle()
        self.turtle.penup()

        if c == None:
            for x in self.x_range:
                x = float(x) / self.precision
                y = a * x + b

                self.turtle.goto(x, y)
                self.turtle.pendown()
        
        if c != None:
            for x in self.x_range:
                x = float(x) / self.precision
                y = a * pow(x, 2) + b * x + c

                self.turtle.goto(x, y)
                self.turtle.pendown()
        
        self.turtle.hideturtle()
        self.screen.exitonclick()

    def plot_trigonometric(self, a, b, type):
        self.turtle.showturtle()
        self.turtle.penup()
        self.turtle.pencolor("red")

        for x in self.x_range:
            x = float(x) / self.precision
            y = a * type(x) + b

            self.turtle.goto(x, y)
            self.turtle.pendown()
        
        self.turtle.hideturtle()
        self.screen.exitonclick()

    def draw_plane(self):

        if self.mode == 'lihgt':
            self.screen.bgcolor('white')
            self.turtle.pencolor('black')
        elif self.mode == 'dark':
            self.screen.bgcolor('black')
            self.turtle.pencolor('green')

        self.turtle.showturtle()
        position = self.turtle.position()
        self.turtle.pendown()

        turned = False
        for _ in range(0, 2):
            self.turtle.setposition(position)

            for _ in range(0, self.dimensions, self.tick):
                self.turtle.forward(self.tick)
                self.turtle.dot(self.dot_size)

            self.turtle.setposition(position)

            for _ in range(0, self.dimensions, self.tick):
                self.turtle.backward(self.tick)
                self.turtle.dot(self.dot_size)

            if not turned:
                self.turtle.setheading(90)
                turned = True

        self.turtle.hideturtle()

    def download(self):
        canvas = self.turtle.getscreen().getcanvas()
        canvas.postscript(file='C:\\Users\\adile\\OneDrive\\Рабочий стол\\equationsVisualizer\\en.eps')
