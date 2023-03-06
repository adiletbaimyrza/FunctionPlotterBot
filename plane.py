import turtle
import constants as ct

class Plane:
    def __init__(self):
        self.dimensions = ct.DIMENSIONS
        self.tick = ct.TICK
        self.dot_size = ct.DOT_SIZE
        self.precision = ct.PRECISION
        self.mode = ct.DARK
        self.font = ct.FONT
        self.font_size = ct.FONT_SIZE
        self.font_type = ct.FONT_TYPE
        self.zoom = ct.ZOOM
        self.enum = ct.ENUM

        dms = self.dimensions
        pcs = self.precision
        self.x_range = range(-dms * pcs, dms * pcs)
        self.equation_range = range(-dms * 2, dms * 2)  # the range for equation line is 2 times larger

        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        turtle.delay(ct.DELAY)
    
    def open_screen(self):
        padding = (self.dimensions * ct.PADDING) // 1   # conversion to int
        dms = self.dimensions + padding
        self.screen.setworldcoordinates(-dms, -dms, dms, dms)

    def draw_plane(self, enumerate=True):
        self.open_screen()
        t = self.turtle

        t.showturtle()

        def enumurate_dots(a, b, turned, sign, initial_pos, num):
            x = a
            y = b

            if not turned:
                y += ct.NUMPADDING_Y
            if turned:
                x += ct.NUMPADDING_X

            t.penup()
            t.setposition(x, y)

            if sign == '+':
                t.write(str(num))
            else:
                t.write(sign + str(num))

            t.setposition(initial_pos)
            t.pendown()
            
        if self.mode == 'light':
            self.screen.bgcolor('white')
            t.pencolor('black')
        elif self.mode == 'dark':
            self.screen.bgcolor('#282828')
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
                    num = _ / ct.ZOOM
                    enumurate_dots(t.position()[0], t.position()[1], turned, '+', temp, num)

            t.setposition(ct.HOME_POS)

            for _ in range(ct.TICK, self.dimensions + 1, ct.TICK):
                t.backward(ct.TICK)
                t.dot(ct.DOT_SIZE)

                temp = t.position()
                if enumerate:
                    num = _ / ct.ZOOM
                    enumurate_dots(t.position()[0], t.position()[1], turned, '-', temp, num)
            
            if not turned:
                t.setheading(ct.DEGREE90)
                turned = True

        t.hideturtle()
        t.penup()