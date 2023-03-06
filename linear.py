from equation import Equation
import turtle
import constants as ct

class Linear(Equation):
    def __init__(self):
        super().__init__()

    def write_equation(self, a, c):
        t = self.turtle
        initial_pos = t.position()

        dms = self.dimensions
        equation_pos = (-dms, dms - dms * ct.PADDING)
        t.setposition(equation_pos)
        t.write(f'y = {a}x + {c}')
        t.setposition(initial_pos)
    
    def draw(self, a, c):
        t = self.turtle
        self.write_equation(a, c)

        t.showturtle()
        t.pencolor('red')
        t.penup()

        for x in self.x_range:
            y = a * x + c # fix zoom

            if x in self.equation_range and y in self.equation_range:
                t.goto(ct.ZOOM * x, ct.ZOOM * y)
                t.pendown()
        
        t.hideturtle()
        t.penup()
        turtle.exitonclick()