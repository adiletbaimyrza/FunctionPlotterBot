import turtle
from constants import ConfigConstants as ct

class Plane:
    def __init__(self):
        self.dimensions = ct.DIMENSIONS
        self.screen_padding = ct.PADDING
        self.tick = ct.TICK
        self.dot_size = ct.DOT_SIZE
        self.font = ct.FONT
        self.zoom = ct.ZOOM
        self.enum = ct.ENUM
        self.zero_pos = ct.ZERO_POS
        self.degree90 = ct.DEGREE90
        self.x_padding = ct.X_PADDING
        self.y_padding = ct.Y_PADDING

        # Set the x and line ranges
        dms = self.dimensions
        self.x_range = range(-dms, dms)
        self.line_range = range(-dms * 2, dms * 2)

        # Initialize turtle object and screen object
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        turtle.delay(ct.DELAY)
    
    def open_screen(self):
        # Set screen coordinates to match dimensions and padding
        dms = self.dimensions + self.screen_padding
        self.screen.setworldcoordinates(-dms, -dms, dms, dms)
    
    def draw_plane(self):
        t = self.turtle

        # Write 0 at (0,0)
        t.penup()
        t.setposition(self.zero_pos)
        t.write('0', font=ct.FONT)

        turned = False

        # Draw lines for positive x values
        for _ in range(0, 2):
            t.setposition(0, 0)
            t.pendown()

            # Draw ticks and dots for positive x values
            for _ in range(self.tick, self.dimensions * 2, self.tick):
                t.forward(self.tick)
                t.dot(self.dot_size)

                temp = t.position()
                if self.enum:
                    num = _ / self.zoom
                    self.enumerate_dots(temp, turned, '+', num)

            t.setposition(0,0)

            # Draw ticks and dots for negative x values
            for _ in range(self.tick, self.dimensions * 2, self.tick):
                t.backward(self.tick)
                t.dot(self.dot_size)

                temp = t.position()
                if self.enum:
                    num = _ / self.zoom
                    self.enumerate_dots(temp, turned, '-', num)

            # Turn turtle 90 degrees for negative y values
            if not turned:
                t.setheading(self.degree90)
                turned = True

    def enumerate_dots(self, pos, turned, sign, num):
        t = self.turtle
        x, y = pos

        if not turned: y += self.y_padding
        if turned: x += self.x_padding

        # Write numbers next to dots
        t.penup()
        t.setposition(x, y)

        if sign == '+':
            t.write(str(num), font=ct.FONT)
        else:
            t.write(sign + str(num), font=ct.FONT)

        # Set initial position and color of turtle pen
        t.setposition(pos)
        t.pendown()

    def make_grid(self):
        t = self.turtle

        # Set initial position and color of turtle pen
        initial_pos = t.pos()
        t.penup()
        t.pencolor('#B1C3C3')

        # Define grid coordinates
        dms = self.dimensions * 2
        xy = 100
        for _ in range(-dms, dms, 10):
            dms = float(dms)
            xy = float(xy)

            # Draw horizontal lines
            t.goto(-dms, xy)
            t.pendown()
            t.goto(dms, xy)
            t.penup()

            # Draw vertical lines
            t.goto(-xy, dms)
            t.pendown()
            t.goto(-xy, -dms)
            t.penup()

            xy = _

        # Reset turtle pen position and color
        t.setposition(initial_pos)
        t.pencolor('black')