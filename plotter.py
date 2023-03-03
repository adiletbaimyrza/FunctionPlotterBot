import turtle
import constants as ct

class Equation:
    def __init__(self):
        self.dimensions = ct.DIMENSIONS
        self.tick = ct.TICK
        self.dot_size = ct.DOT_SIZE
        self.precision = ct.PRECISION
        self.mode = ct.LIGHT
        self.font = ct.FONT
        self.font_size = ct.FONT_SIZE
        self.font_type = ct.FONT_TYPE

        dms = self.dimensions
        pcs = self.precision
        self.x_range = range(-dms, dms)
        self.line_range = range(-dms - int(dms*0.2) // 1, dms + int(dms*0.2))

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

    def set_mode(self, mode=ct.LIGHT):
        self.mode = mode

    def open_screen(self):
        dms = self.dimensions + (self.dimensions * ct.PADDING) // 1
        self.screen.setworldcoordinates(-dms, -dms, dms, dms)

    def draw(self):
        pass

    def write_equation():
        pass

    def draw_plane(self, enumerate=False):
        t = self.turtle
        t.showturtle()
        t.pendown()

        def enumurate_dots(a, b, turned, sign, temp, num):
            x = a
            y = b

            if not turned:
                y += ct.NUMPADDING_Y
            if turned:
                x += ct.NUMPADDING_X

            t.penup()
            t.setposition(x, y)
            t.write(sign + str(num))
            t.setposition(temp)
            t.pendown()
            
        if type == ct.LIGHT:
            self.screen.bgcolor('white')
            t.pencolor('black')
        elif type == ct.DARK:
            self.screen.bgcolor('black')
            t.pencolor('green')

        t.penup()
        t.setposition(ct.ZERO_POS)
        t.write('0')

        turned = False
        for _ in range(0, 2):
            t.setposition(ct.HOME_POS)
            t.pendown()

            for _ in range(ct.TICK, self.dimensions + 1, ct.TICK):
                t.forward(ct.TICK)
                t.dot(ct.DOT_SIZE)

                temp = t.position()
                if enumerate:
                    enumurate_dots(t.position()[0], t.position()[1], turned, '', temp, _)

            t.setposition(ct.HOME_POS)

            for _ in range(ct.TICK, self.dimensions + 1, ct.TICK):
                t.backward(ct.TICK)
                t.dot(ct.DOT_SIZE)

                temp = t.position()
                if enumerate:
                    enumurate_dots(t.position()[0], t.position()[1], turned, '-', temp, _)
            
            if not turned:
                t.setheading(ct.DEGREE90)
                turned = True

        t.hideturtle()
        t.penup()




