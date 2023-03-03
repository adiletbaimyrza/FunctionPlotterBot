from plotter import Equation
import turtle
import constants as ct

class Linear(Equation):
    def __init__(self):
        super().__init__()
    
    def draw(self, a, c):
        t = self.turtle

        self.open_screen()
        self.draw_plane(enumerate=True)
        self.write_equation(a, c)

        t.showturtle()
        t.pencolor('red')

        for x in self.x_range:
            y = a * x + c

            if x in self.line_range and y in self.line_range:
                t.goto(x, y)
                t.pendown()
        
        t.hideturtle()
        t.penup()
        turtle.exitonclick()
    
    def write_equation(self, a, c):
        t = self.turtle
        initial_pos = t.position()

        dms = self.dimensions
        equation_pos = (-dms, dms - dms * ct.PADDING)
        t.setposition(equation_pos)
        t.write(f'y = {a}x + {c}')
        t.setposition(initial_pos)