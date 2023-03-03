# from plotter import Equation
# import turtle
# import constants as ct

# class Trigonometric(Equation):
#     def __init__(self):
#         super().__init__()

#     def draw(self, a, c, type):
#         self.turtle.pencolor('red')
#         self.turtle.showturtle()
#         self.turtle.penup()

#         for x in self.x_range:
#             x = float(x) / self.precision
#             y = a * type(x) + c

#             self.turtle.goto(x, y)
#             self.turtle.pendown()
        
#         self.turtle.hideturtle()
#         self.screen.exitonclick()
    
#     def write_equation(self, a, c, type):
#         temp = self.turtle.position()
#         self.turtle.penup()
#         z = self.zoom / 2
#         self.turtle.setposition(-self.dimensions + z, self.dimensions - z)
#         self.turtle.write(f'y = {a}{type}(x) + {c}')
#         self.turtle.setposition(temp)