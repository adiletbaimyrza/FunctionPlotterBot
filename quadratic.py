from equation import Equation
import turtle
import constants as ct

class Quadratic(Equation):
    def __init__(self):
        super().__init__()

    def stringify(self, a, b, c) -> str: #fix the stringify
        res_begin = 'f(x) = '

        if a == 0:
            aa = ''
        elif a == 1:
            aa = 'x^2'
        elif a == -1:
            aa = '-x^2'
        else:
            aa = f'{a}x^2'
        
        if not b == 0 and not c == 0:
            aa += ' '

        if b == 0:
            bb = ''
        elif b == 1:
            bb = '+ x '
        elif a == -1:
            bb = '- x '
        elif b < 0:
            bb = f'- {abs(b)}x '
        else: 
            bb = f'+ {b}x'
        


        if c == 0:
            cc = ''
        elif c < 0 and not c == -1:
            cc = f'- {abs(c)}'
        else:
            if a == 0 and b == 0:
                cc = f'{c}'
            else:
                cc = f'+ {abs(c)}'
        
        return res_begin + '0' if a == 0 and b == 0 and c == 0 else res_begin + aa + bb + cc


    def write_func_on_graph(self, a, b, c):
        t = self.turtle
        t.penup()
        initial_pos = t.position()

        dms = self.dimensions
        equation_pos = (-dms, dms - dms * ct.PADDING)
        t.setposition(equation_pos)
        t.write(self.stringify(a, b, c))
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
