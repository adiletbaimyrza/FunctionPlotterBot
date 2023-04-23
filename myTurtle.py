#Import necessary modules
import quadratic
import linear
import trigonometric
import math
import interpreter
import plane
import re
from PIL import Image
import turtle

#Take input equation from the user
eq = interpreter.Input.take_input()

#Check if the equation is linear and extract coefficients
match = interpreter.Input.check_pattern_linear(eq)
res = interpreter.Input.extract_args(match)

#Create a coordinate plane object and draw grid
coordinate_plane = plane.Plane()
coordinate_plane.open_screen()
coordinate_plane.make_grid()
coordinate_plane.draw_plane()

#Plot the linear graph and write function on the graph
equation = linear.Linear()
equation.plot_graph(res[0],res[1])
equation.write_func_on_graph(res[0], res[1])

#Convert the turtle canvas to postscript file and save as jpeg
ts = turtle.Screen().getcanvas()
ts.postscript(file='my_drawing.eps')

img = Image.open('my_drawing.eps')
img.save('my_drawing.jpeg', 'jpeg')

#Finish turtle graphics
turtle.done()