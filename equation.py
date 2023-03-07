import turtle
import constants as ct

class Equation:
    def __init__(self):
        self.dimensions = ct.DIMENSIONS
        self.zoom = ct.ZOOM
        self.line_color = ct.LINE_COLOR
        dms = self.dimensions
        self.x_range = range(-dms, dms)
        self.line_range = range(-dms * 2, dms * 2)

        self.turtle = turtle.Turtle()

    def plot_graph(self):
        pass

    def write_func_on_graph(self):
        pass

    def evaluate_y(self):
        pass