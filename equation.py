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
        self.pen_size = ct.PEN_SIZE

        # Create a turtle object for the class instance
        self.turtle = turtle.Turtle()

    # Define a method to plot the graph
    def plot_graph(self):
        pass

    # Define a method to write the function on the graph
    def write_func_on_graph(self):
        pass

    # Define a method to evaluate y value
    def evaluate_y(self):
        pass