from equation import Equation
import turtle
import constants as ct

class Linear(Equation):
    def __init__(self):
        super().__init__()

    def stringify(self, a, c) -> str:
        return f'y = {a}x + {c}'

    def textify(self, a, c):
        t = self.turtle

        t.penup()

        initial_pos = t.position()
        dms = self.dimensions
        equation_pos = (-dms, dms - dms * ct.PADDING)
        t.setposition(equation_pos)
        t.write(self.stringify(a, c)) # fix correct output
        t.setposition(initial_pos)
    
    def evaluate_y(self, x, a, c) -> float:
        return a * x + c
    
    def plot_graph(self, a, c):
        t = self.turtle

        self.textify(a, c)

        t.showturtle()
        t.pencolor('red')
        t.penup()

        for x in self.x_range:
            y = self.evaluate_y(x, a, c)

            if x in self.equation_range and y in self.equation_range:
                t.goto(ct.ZOOM * x, ct.ZOOM * y)
                t.pendown()
        
        t.hideturtle()
        t.penup()
        turtle.exitonclick()