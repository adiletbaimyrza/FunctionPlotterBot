import turtle
import constants as ct

class Equation:
    def __init__(self):
        self.dimensions = ct.DIMENSIONS
        self.tick = ct.TICK
        self.dot_size = ct.DOT_SIZE
        self.precision = ct.PRECISION
        self.zoom = ct.ZOOM
        self.mode = ct.LIGHT
        self.font = ct.FONT
        self.font_size = ct.FONT_SIZE
        self.font_type = ct.FONT_TYPE

        dms = self.dimensions
        pcs = self.precision
        self.x_range = range(-dms *  pcs, dms * pcs)

        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        turtle.delay(ct.DELAY)

    def set_dimensions(self, dimensions=ct.DIMENSIONS):
        self.dimensions = dimensions

    def set_tick(self, tick=ct.TICK):
        self.tick = tick

    def set_dot_size(self, dot_size=ct.DOT_SIZE):
        self.dot_size = dot_size

    def set_precision(self, precision=ct.PRECISION):
        self.precision = precision

    def set_zoom(self, zoom=ct.ZOOM):
        self.zoom = zoom

    def set_mode(self, mode=ct.LIGHT):
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

    def write_equation():
        pass

    def draw_plane(self):
        if type == ct.LIGHT:
            self.screen.bgcolor('white')
            self.turtle.pencolor('black')
        elif type == ct.DARK:
            self.screen.bgcolor('black')
            self.turtle.pencolor('green')
        
        self.turtle.showturtle()
        position = self.turtle.position()
        self.turtle.pendown()

        self.turtle.setposition(position)

        x = self.turtle.position()[0]
        y = self.turtle.position()[1]

        x += float(self.tick / 5)
        y += float(self.tick / 5)

        self.turtle.penup()
        self.turtle.setposition(x, y)
        self.turtle.write('0')

        turned = False
        for _ in range(0, 2):
            self.turtle.setposition(position)

            for _ in range(1, self.dimensions, self.tick):
                self.turtle.forward(self.tick)
                self.turtle.dot(self.dot_size)

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

            self.turtle.setposition(position)

            for _ in range(1, self.dimensions, self.tick):
                self.turtle.backward(self.tick)
                self.turtle.dot(self.dot_size)

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

            if not turned:
                self.turtle.setheading(ct.DEGREE90)
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
    
    def write_equation(self, a, c):
        temp = self.turtle.position()
        self.turtle.penup()
        z = self.zoom / 2
        self.turtle.setposition(-self.dimensions + z, self.dimensions - z)
        self.turtle.write(f'y = {a}x + {c}')
        self.turtle.setposition(temp)

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
    
    def write_equation(self, a, b, c):
        temp = self.turtle.position()
        self.turtle.penup()
        z = self.zoom / 2
        self.turtle.setposition(-self.dimensions + z, self.dimensions - z)
        self.turtle.write(f'y = {a}x^2 + {b}x + {c}')
        self.turtle.setposition(temp)

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
    
    def write_equation(self, a, c, type):
        temp = self.turtle.position()
        self.turtle.penup()
        z = self.zoom / 2
        self.turtle.setposition(-self.dimensions + z, self.dimensions - z)
        self.turtle.write(f'y = {a}{type}(x) + {c}')
        self.turtle.setposition(temp)