import linear
import interpreter
import plane
from PIL import Image
import turtle

eq = interpreter.Input.take_input()
match = interpreter.Input.check_pattern_linear(eq)
res = interpreter.Input.extract_args(match)


coordinate_plane = plane.Plane()
coordinate_plane.open_screen()
coordinate_plane.make_grid()
coordinate_plane.draw_plane()

equation = linear.Linear()
equation.plot_graph(res[0],res[1])
equation.write_func_on_graph(res[0], res[1])

ts = turtle.Screen().getcanvas()
ts.postscript(file='my_drawing.eps')

img = Image.open('my_drawing.eps')
img.save('my_drawing.jpeg', 'jpeg')

turtle.done()