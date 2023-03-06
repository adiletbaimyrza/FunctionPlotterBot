from equation import Equation
import turtle
import constants as ct

class Quadratic(Equation):
    def __init__(self):
        super().__init__()

    def write_equation(self, a, b, c):
        t = self.turtle
        initial_pos = t.position()

        dms = self.dimensions
        equation_pos = (-dms, dms - dms * ct.PADDING)
        t.setposition(equation_pos)
        t.write(f'y = {a}x^2 + {b}x + {c}')
        t.setposition(initial_pos)

    def draw(self, a, b, c):
        t = self.turtle

        self.open_screen()
        self.draw_plane(enumerate=True)
        self.write_equation(a, b, c)
        
        t.showturtle()
        t.pencolor('red')

        for x in self.x_range:
            y = a*pow(x, 2) + b*x + c

            if x in self.line_range and y in self.line_range:
                t.goto(x, y)
                t.pendown()
        
        t.hideturtle()
        t.penup()
        turtle.exitonclick()
