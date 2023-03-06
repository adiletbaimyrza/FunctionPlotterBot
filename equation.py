import turtle
import constants as ct

class Equation:
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

        dms = self.dimensions
        pcs = self.precision
        self.x_range = range(-dms * pcs, dms * pcs)
        self.equation_range = range(-dms * 10, dms * 10)

        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        turtle.delay(ct.DELAY)

    def draw(self):
        pass

    def write_equation():
        pass