import plotter
import math

equation = plotter.Quadratic()

equation.set_dimensions(20)
equation.set_dot_size(3)
equation.set_mode('dark')
equation.set_precision(10)
equation.set_tick(5)
equation.set_zoom(10)

equation.open_screen()

equation.draw_plane()

equation.plot_equation(0.1, 1, 0)
