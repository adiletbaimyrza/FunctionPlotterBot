from equation import Equation
import turtle
import constants as ct

class Trigonometric(Equation):
    def __init__(self):
        super().__init__()

    def draw(self, a, c, type):
        self.open_screen()
        self.draw_plane(enumerate=True)
        self.write_equation(a, c, 'sin')

        self.turtle.showturtle()
        self.turtle.pencolor('red')

        for x in self.x_range:
            x = float(x) / self.precision
            y = a * type(x) + c

            self.turtle.goto(x, y)
            self.turtle.pendown()
        
        self.turtle.hideturtle()
        self.screen.exitonclick()
    
    def write_equation(self, a, c, type):
        temp = self.turtle.position()
        self.turtle.penup()
        dms = self.dimensions
        equation_pos = (-dms, dms - dms * ct.PADDING)
        self.turtle.setposition(equation_pos)
        self.turtle.write(f'y = {a}{type}(x) + {c}')
        self.turtle.setposition(temp)