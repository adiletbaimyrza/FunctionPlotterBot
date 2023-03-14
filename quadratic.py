from equation import Equation
import turtle
import constants as ct

class Quadratic(Equation):
    def __init__(self):
        super().__init__()

    def stringify(self, a, b, c) -> str:
        res_begin = 'f(x) = '
        aa = ''
        bb = ''
        cc = ''

        if a == 0 and b == 0: cc = f'{c}'
        elif a == 0 and c == 0:
            if b == 1: bb = 'x'
            elif b == -1: bb = '-x'
            else: bb = f'{b}x'
        elif b == 0 and c == 0:
            if a == 1: aa = 'x^2'
            elif a == -1: aa = '-x^2'
            else: aa = f'{a}x^2'
        elif a == 0:
            if b == 1: bb = 'x '
            elif b == -1: bb = '-x '
            else: bb = f'{b}x '

            if c < 0: cc = f'- {abs(c)}'
            else: cc = f'+ {c}'
        elif b == 0:
            if a == 1: aa = 'x^2 '
            elif a == -1: aa = '-x^2 '
            else: aa = f'{a}x^2 '

            if c < 0: cc = f'- {abs(c)}'
            else: cc = f'+ {c}'
        elif c == 0:
            if a == 1: aa = 'x^2 '
            elif a == -1: aa = '-x^2 '
            else: aa = f'{a}x^2 '

            if b == 1: bb = '+ x'
            elif b == -1: bb = '- x'
            else:
                if b < 0: bb = f'- {abs(b)}x'
                else: bb = f'+ {b}x'
                
        else:
            if a == 1: aa = 'x^2 '
            elif a == -1: aa = '-x^2 '
            else: aa = f'{a}x^2 '

            if b == 1: bb = '+ x '
            elif b == -1: bb = '- x '
            elif b < 0: bb = f'- {abs(b)}x '
            else: bb = f'+ {b}x '

            if c < 0: cc = f'- {abs(c)}'
            else: cc = f'+ {c}'

        return res_begin + '0' if a == 0 and b == 0 and c == 0 else res_begin + aa + bb + cc


    def write_func_on_graph(self, a, b, c):
        t = self.turtle

        t.penup()
        initial_pos = t.position()

        dms = self.dimensions
        equation_pos = (-dms, dms - dms * 0.1)
        t.setposition(equation_pos)
        t.write(self.stringify(a, b, c))

        t.setposition(initial_pos)

    def evaluate_y(self, x, a, b, c) -> float:
        return a*pow(x, 2) + b*x + c

    def plot_graph(self, a, b, c):
        t = self.turtle
        self.write_func_on_graph(a, b, c)

        t.showturtle()
        t.pencolor(self.line_color)
        t.penup()

        for x in self.line_range:
            y = self.evaluate_y(x, a, b, c)

            t.goto(self.zoom * x, self.zoom * y)
            t.pendown()
        
        t.hideturtle()
        t.penup()
        turtle.exitonclick()
