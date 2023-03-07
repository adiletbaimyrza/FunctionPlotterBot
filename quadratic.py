from equation import Equation
import turtle
import constants as ct

class Quadratic(Equation):
    def __init__(self):
        super().__init__()

    def textify(self, a, b, c):
        t = self.turtle
        t.penup()
        initial_pos = t.position()

        dms = self.dimensions
        equation_pos = (-dms, dms - dms * ct.PADDING)
        t.setposition(equation_pos)
        t.write(f'y = {a}x^2 + {b}x + {c}') # fix correct output
        t.setposition(initial_pos)

    def evaluate_y(self, x, a, b, c) -> float:
        return a*pow(x, 2) + b*x + c

    def plot_graph(self, a, b, c):
        t = self.turtle
        self.textify(a, b, c)

        t.showturtle()
        t.pencolor('red')
        t.penup()

        for x in self.x_range:
            
            y = self.evaluate_y(x, a, b, c)

            if x in self.x_range and y in self.x_range:
                t.goto(ct.ZOOM * x, ct.ZOOM * y)
                t.pendown()
        
        t.hideturtle()
        t.penup()
        turtle.exitonclick()
