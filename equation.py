import turtle
from constants import ConfigConstants as config

class Equation:
    def __init__(self):
        self.dimensions = config.DIMENSIONS
        self.zoom = config.ZOOM
        self.line_color = config.LINE_COLOR
        dms = self.dimensions
        self.x_range = range(-dms, dms)
        self.line_range = range(-dms * 2, dms * 2)
        self.pen_size = config.PEN_SIZE

        self.turtle = turtle.Turtle()

    def plot_graph(self):
        pass

    def write_func_on_graph(self):
        pass

    def evaluate_y(self):
        pass