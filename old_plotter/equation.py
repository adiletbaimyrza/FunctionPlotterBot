import turtle
from old_plotter import constants

class Equation:
    def __init__(self):
        self.dimensions = constants.ConfigConstants.DIMENSIONS
        self.zoom = constants.ConfigConstants.ZOOM
        self.line_color = constants.ConfigConstants.LINE_COLOR
        dms = self.dimensions
        self.x_range = range(-dms, dms)
        self.line_range = range(-dms * 2, dms * 2)
        self.pen_size = constants.ConfigConstants.PEN_SIZE

        self.turtle = turtle.Turtle()

    def plot_graph(self):
        pass

    def write_func_on_graph(self):
        pass

    def evaluate_y(self):
        pass