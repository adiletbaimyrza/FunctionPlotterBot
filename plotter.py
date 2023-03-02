import turtle

DIMENSIONS = 100
TICK = 1
DOT_SIZE = 3
PRECISION = 10
ZOOM = -5
LIGHT = 'light'
DARK = 'dark'
DELAY = 0
DEGREE90 = 90
FONT = 'Arial'
FONT_SIZE = 12
FONT_TYPE = 'normal'

class Equation:
    def __init__(self):
        self.dimensions = DIMENSIONS
        self.tick = TICK
        self.dot_size = DOT_SIZE
        self.precision = PRECISION
        self.zoom = ZOOM
        self.mode = LIGHT
        self.font = FONT
        self.font_size = FONT_SIZE
        self.font_type = FONT_TYPE

        dms = self.dimensions
        pcs = self.precision
        self.x_range = range(-dms *  pcs, dms * pcs)

        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        turtle.delay(DELAY)

    def set_dimensions(self, dimensions=DIMENSIONS):
        self.dimensions = dimensions

    def set_tick(self, tick=TICK):
        self.tick = tick

    def set_dot_size(self, dot_size=DOT_SIZE):
        self.dot_size = dot_size

    def set_precision(self, precision=PRECISION):
        self.precision = precision

    def set_zoom(self, zoom=ZOOM):
        self.zoom = zoom

    def set_mode(self, mode=LIGHT):
        self.mode = mode

    def open_screen(self):
        zoom = -self.zoom
        dms = self.dimensions
        self.screen.setworldcoordinates(-dms - zoom,
                                        -dms - zoom,
                                         dms + zoom,
                                         dms + zoom)

    def plot_equation(self):
        pass

    def draw_plane(self):
        if self.mode == LIGHT:
            self.screen.bgcolor('white')
            self.turtle.pencolor('black')
        elif self.mode == DARK:
            self.screen.bgcolor('black')
            self.turtle.pencolor('green')

        self.turtle.showturtle()
        position = self.turtle.position()
        self.turtle.pendown()

        turned = False
        for _ in range(0, 2):
            self.turtle.setposition(position)

            for _ in range(0, self.dimensions, self.tick):
                temp = self.turtle.position()
                if not turned:
                    x = self.turtle.position()[0]
                    y = self.turtle.position()[1]
                    y += float(self.tick / 5)
                    self.turtle.penup()
                    self.turtle.setposition(x, y)
                    self.turtle.write(_)
                    self.turtle.setposition(temp)
                    self.turtle.pendown()
                if turned:
                    x = self.turtle.position()[0]
                    y = self.turtle.position()[1]
                    x += float(self.tick / 5)
                    self.turtle.penup()
                    self.turtle.setposition(x, y)
                    self.turtle.write(_)
                    self.turtle.setposition(temp)
                    self.turtle.pendown()

                self.turtle.forward(self.tick)
                self.turtle.dot(self.dot_size)

            self.turtle.setposition(position)

            for _ in range(0, self.dimensions, self.tick):
                temp = self.turtle.position()
                if not turned:
                    x = self.turtle.position()[0]
                    y = self.turtle.position()[1]
                    y += float(self.tick / 5)
                    self.turtle.penup()
                    self.turtle.setposition(x, y)
                    self.turtle.write(-_)
                    self.turtle.setposition(temp)
                    self.turtle.pendown()
                if turned:
                    x = self.turtle.position()[0]
                    y = self.turtle.position()[1]
                    x += float(self.tick / 5)
                    self.turtle.penup()
                    self.turtle.setposition(x, y)
                    self.turtle.write(-_)
                    self.turtle.setposition(temp)
                    self.turtle.pendown()
                self.turtle.backward(self.tick)
                self.turtle.dot(self.dot_size)

            if not turned:
                self.turtle.setheading(DEGREE90)
                turned = True

        self.turtle.hideturtle()

class Linear(Equation):
    def __init__(self):
        super().__init__()
    
    def plot_equation(self, a, c):
        self.turtle.pencolor('red')
        self.turtle.showturtle()
        self.turtle.penup()

        for x in self.x_range:
            x = float(x) / self.precision
            y = a * x + c

            self.turtle.goto(x, y)
            self.turtle.pendown()
        
        self.turtle.hideturtle()
        self.screen.exitonclick()

class Quadratic(Equation):
    def __init__(self):
        super().__init__()

    def plot_equation(self, a, b, c):
        self.turtle.pencolor('red')
        self.turtle.showturtle()
        self.turtle.penup()

        for x in self.x_range:
            x = float(x) / self.precision
            y = a * pow(x, 2) + b * x + c

            self.turtle.goto(x, y)
            self.turtle.pendown()
        
        self.turtle.hideturtle()
        self.screen.exitonclick()

class Trigonometric(Equation):
    def __init__(self):
        super().__init__()

    def plot_equation(self, a, c, type):
        self.turtle.pencolor('red')
        self.turtle.showturtle()
        self.turtle.penup()

        for x in self.x_range:
            x = float(x) / self.precision
            y = a * type(x) + c

            self.turtle.goto(x, y)
            self.turtle.pendown()
        
        self.turtle.hideturtle()
        self.screen.exitonclick()