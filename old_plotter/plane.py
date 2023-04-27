import turtle
from old_plotter import constants

class Plane:
    def __init__(self):
        self.dimensions = constants.ConfigConstants.DIMENSIONS
        self.screen_padding = constants.ConfigConstants.PADDING
        self.tick = constants.ConfigConstants.TICK
        self.dot_size = constants.ConfigConstants.DOT_SIZE
        self.font = constants.ConfigConstants.FONT
        self.zoom = constants.ConfigConstants.ZOOM
        self.enum = constants.ConfigConstants.ENUM
        self.zero_pos = constants.ConfigConstants.ZERO_POS
        self.degree90 = constants.ConfigConstants.DEGREE90
        self.x_padding = constants.ConfigConstants.X_PADDING
        self.y_padding = constants.ConfigConstants.Y_PADDING

        dms = self.dimensions
        self.x_range = range(-dms, dms)
        self.line_range = range(-dms * 2, dms * 2)

        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        turtle.delay(constants.ConfigConstants.DELAY)
    
    def open_screen(self):
        dms = self.dimensions + self.screen_padding
        self.screen.setworldcoordinates(-dms, -dms, dms, dms)
    
    def draw_plane(self):
        t = self.turtle

        t.penup()
        t.setposition(self.zero_pos)
        t.write('0', font=constants.ConfigConstants.FONT)

        turned = False
        for _ in range(0, 2):
            t.setposition(0, 0)
            t.pendown()

            for _ in range(self.tick, self.dimensions * 2, self.tick):
                t.forward(self.tick)
                t.dot(self.dot_size)

                temp = t.position()
                if self.enum:
                    num = _ / self.zoom
                    self.enumerate_dots(temp, turned, '+', num)

            t.setposition(0,0)

            for _ in range(self.tick, self.dimensions * 2, self.tick):
                t.backward(self.tick)
                t.dot(self.dot_size)

                temp = t.position()
                if self.enum:
                    num = _ / self.zoom
                    self.enumerate_dots(temp, turned, '-', num)

            if not turned:
                t.setheading(self.degree90)
                turned = True

    def enumerate_dots(self, pos, turned, sign, num):
        t = self.turtle
        x, y = pos

        if not turned: y += self.y_padding
        if turned: x += self.x_padding
        
        t.penup()
        t.setposition(x, y)

        if sign == '+':
            t.write(str(num), font=constants.ConfigConstants.FONT)
        else:
            t.write(sign + str(num), font=constants.ConfigConstants.FONT)
        
        t.setposition(pos)
        t.pendown()

    def make_grid(self):
        t = self.turtle

        initial_pos = t.pos()
        t.penup()
        t.pencolor('#B1C3C3')

        dms = self.dimensions * 2
        xy = 100
        for _ in range(-dms, dms, 10):
            dms = float(dms)
            xy = float(xy)
            
            t.goto(-dms, xy)
            t.pendown()
            t.goto(dms, xy)
            t.penup()
            t.goto(-xy, dms)
            t.pendown()
            t.goto(-xy, -dms)
            t.penup()

            xy = _
        
        t.setposition(initial_pos)
        t.pencolor('black')