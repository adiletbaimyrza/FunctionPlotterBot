from equation import Equation
import turtle
import constants as ct

class Linear(Equation):
    def __init__(self):
        super().__init__()

    def stringify(self, a, c) -> str:
        res_begin = 'f(x) = '

        if a == 0 and c == 0:
            res = res_begin + f'{a}'
        elif a == 0:
            res = res_begin + f'{c}'
        elif c == 0:
            if a == 1:
                res = res_begin + 'x'
            else:
                res = res_begin + f'{a}x'
        else:
            if a < 0 and c < 0:
                res = res_begin + f'{a} ' + '- ' + f'{abs(c)}'
            elif c < 0:
                res = res_begin + f'{a}x ' + '- ' + f'{abs(c)}'
            else:
                res = res_begin + f'{a}x ' + '+ ' + f'{c}'
        
        return res

    def write_func_on_graph(self, a, c):
        t = self.turtle

        t.penup()
        initial_pos = t.pos()

        dms = self.dimensions
        equation_pos = (float(-dms), float(dms - dms * 0.1))
        t.setposition(equation_pos)
        t.write(self.stringify(a, c), font=ct.FONT)

        t.setposition(initial_pos)
    
    def evaluate_y(self, x, a, c) -> float:
        return a * x + c
    
    def plot_graph(self, a, c):
        t = self.turtle

        self.write_func_on_graph(a, c)

        t.showturtle()
        t.pencolor(self.line_color)
        t.penup()
        t.pensize(self.pen_size)

        for x in self.line_range:
            y = self.evaluate_y(x, a, c)

            t.goto(self.zoom * x, self.zoom * y)
            t.pendown()
        
        t.hideturtle()
        t.penup()