import quadratic
import linear
import trigonometric
import math
import interpreter
import plane
import re

eq = interpreter.Input.take_input()
match = interpreter.Input.check_pattern_linear(eq)
res = interpreter.Input.extract_args(match)
print(res)

coordinate_plane = plane.Plane()
coordinate_plane.open_screen()
coordinate_plane.make_grid()
coordinate_plane.draw_plane()

equation = linear.Linear()
equation.plot_graph(res[0],res[1])
equation.write_func_on_graph(res[0], res[1])

