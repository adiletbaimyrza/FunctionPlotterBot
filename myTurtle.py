import plotter
import math

equation = plotter.EquationVisual(dimensions=100, tick=2, dot_size=3, precision=10, zoom=-5, mode='light') # default values: 100, 2, 3, 10, -5, 'light'

equation.open_screen(zoom=90) # default value: -5
equation.set_mode('dark') # default value: 'light'
equation.draw_plane()

# equation.plot_equation(2, -5) # linear equation
# equation.plot_equation(-1, 2, 1) # quadratic equation
# equation.plot_trigonometric(2, 0, math.cos) # trigonometric equation