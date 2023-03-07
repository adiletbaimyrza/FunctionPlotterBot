import turtle
import constants as ct

class Plane:
    def __init__(self):
        self.dimensions = ct.DIMENSIONS
        self.screen_padding = ct.PADDING
        self.tick = ct.TICK
        self.dot_size = ct.DOT_SIZE
        self.mode = ct.MODE
        self.font = ct.FONT
        self.font_size = ct.FONT_SIZE
        self.font_type = ct.FONT_TYPE
        self.zoom = ct.ZOOM
        self.enum = ct.ENUM
        self.zero_pos = ct.ZERO_POS
        self.degree90 = ct.DEGREE90
        self.x_padding = ct.X_PADDING
        self.y_padding = ct.Y_PADDING

        # Calculate the ranges for the plane
        dms = self.dimensions
        self.x_range = range(-dms, dms)
        self.line_range = range(-dms * 2, dms * 2)

        # Set up the turtle
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        turtle.delay(ct.DELAY)
    
    def open_screen(self):
        # Set the screen coordinates
        dms = self.dimensions + self.screen_padding
        self.screen.setworldcoordinates(-dms, -dms, dms, dms)
    
    def draw_plane(self, enumerate=True):
        # Set up the screen and turtle
        self.open_screen()
        t = self.turtle
        t.showturtle()

        # Draw 0 at the position (0,0)
        t.penup()
        t.setposition(self.zero_pos)
        t.write('0')

        # Draw the x and y axes
        turned = False
        for _ in range(0, 2):
            t.setposition(0, 0)
            t.pendown()

            # Draw the positive x/y axis
            for _ in range(self.tick, self.dimensions + 1, self.tick):
                t.forward(self.tick)
                t.dot(self.dot_size)

                temp = t.position()
                if self.enum:
                    num = _ / self.zoom
                    self.enumerate_dots(temp, turned, '+', num)

            # Draw the negative x/y axis
            t.setposition(0,0)
            for _ in range(self.tick, self.dimensions + 1, self.tick):
                t.backward(self.tick)
                t.dot(self.dot_size)

                temp = t.position()
                if self.enum:
                    num = _ / self.zoom
                    self.enumerate_dots(temp, turned, '-', num)

            # Rotate to draw the other axis
            if not turned:
                t.setheading(self.degree90)
                turned = True

        # Hide the turtle
        t.hideturtle()

    def enumerate_dots(self, pos, turned, sign, num):
        # Enumerate dots on the axis
        t = self.turtle
        x, y = pos

        if not turned:
            y += self.y_padding
        if turned:
            x += self.x_padding
        
        t.penup()
        t.setposition(x, y)

        if sign == '+':
            t.write(str(num))
        else:
            t.write(sign + str(num))
        
        t.setposition(pos)
        t.pendown()