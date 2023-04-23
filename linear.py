#Import Equation class and turtle library
from equation import Equation
import turtle
import constants as ct

#Define Linear class that inherits from Equation class
class Linear(Equation):
    def __init__(self):
        super().__init__()

    # Method to convert the given coefficients to a string representation of the linear equation
    def stringify(self, a, c) -> str:
        # Initialize the result with the prefix
        res_begin = 'f(x) = '
        # Check for special cases where a and c are zero
        if a == 0 and c == 0:
            res = res_begin + f'{a}'
        elif a == 0:
            res = res_begin + f'{c}'
        elif c == 0:
            # Check for special cases where a is 1 or -1
            if a == 1:
                res = res_begin + 'x'
            else:
                res = res_begin + f'{a}x'
        else:
            # Check for cases where a and/or c are negative
            if a < 0 and c < 0:
                res = res_begin + f'{a} ' + '- ' + f'{abs(c)}'
            elif c < 0:
                res = res_begin + f'{a}x ' + '- ' + f'{abs(c)}'
            else:
                res = res_begin + f'{a}x ' + '+ ' + f'{c}'
        
        return res

    # Method to write the linear equation on the graph
    def write_func_on_graph(self, a, c):
        t = self.turtle

        t.penup()
        initial_pos = t.pos()
        # Define the position of the equation on the graph
        dms = self.dimensions
        equation_pos = (float(-dms), float(dms - dms * 0.1))
        t.setposition(equation_pos)
        t.write(self.stringify(a, c), font=ct.FONT)

        t.setposition(initial_pos)

    # Method to evaluate y values for given x and coefficients
    def evaluate_y(self, x, a, c) -> float:
        return a * x + c

    # Method to plot the graph of the linear equation
    def plot_graph(self, a, c):
        t = self.turtle

        self.write_func_on_graph(a, c)

        t.showturtle()
        t.pencolor(self.line_color)
        t.penup()
        t.pensize(self.pen_size)

        # Iterate over the range of x values and evaluate y values for each x
        for x in self.line_range:
            y = self.evaluate_y(x, a, c)

            # Plot the point (x, y) on the graph
            t.goto(self.zoom * x, self.zoom * y)
            t.pendown()
            
        # Hide the turtle after the plot is complete
        t.hideturtle()
        t.penup()