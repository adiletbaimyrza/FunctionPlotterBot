import time
import matplotlib.pyplot as plt
import numpy as np
import os

from old_plotter import linear
from old_plotter import interpreter
from old_plotter import plane
from PIL import Image
import turtle

import plotter

this_path = os.path.dirname(os.path.realpath(__file__))
results_dir = os.path.join(this_path, 'results')
graphs_dir = os.path.join(results_dir, 'graphs')

old_equations = [
    'f(x) = 2x + 1',
    'f(x) = -3x + 2',
    'f(x) = 0.1x',
    'f(x) = -0.8x',
    'f(x) = 3x + 4',
    'f(x) = -2x + 5',
    'f(x) = 4x - 3',
    'f(x) = -5x + 6',
    'f(x) = 10x + 2',
    'f(x) = -7x + 9'
]

new_equations = [
    '2*x + 1',
    '-3*x + 2',
    '0.1*x',
    '-0.8*x',
    '3*x + 4',
    '-2*x + 5',
    '4*x - 3',
    '-5*x + 6',
    '10*x + 2',
    '-7*x + 9'
]

time_old = []
time_new = []

for eq in old_equations:

    start_time_old = time.time()

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
    file_path = os.path.join(results_dir, 'old_graph.eps')
    ts.postscript(file=file_path)

    img = Image.open(file_path)
    file_path = os.path.join(graphs_dir, 'old(' + eq + ').jpeg')
    img.save(file_path, 'jpeg')

    turtle.Screen().clear()

    end_time_old = time.time()

    elapsed_time_old = end_time_old - start_time_old

    time_old.append(elapsed_time_old)

for eq in new_equations:

    start_time_new = time.time()

    my_plotter = plotter.Plotter(eq, 10)
    my_plotter.coordinate_plane()
    my_plotter.plot()
    file_path = os.path.join(graphs_dir, 'new(' + eq + ').png')
    my_plotter.save(file_path)
    my_plotter.clear()

    end_time_new = time.time()

    elapsed_time_new = end_time_new - start_time_new

    time_new.append(elapsed_time_new)


file_path = os.path.join(results_dir, 'old_time_results.txt')
with open(file_path, "w") as f:
    for t in time_old:
        f.write(str(t) + "\n")

file_path = os.path.join(results_dir, 'new_time_results.txt')
with open(file_path, "w") as f:
    for t in time_new:
        f.write(str(t) + "\n")

data = {
    'Old Plotter': time_old,
    'New Plotter': time_new,
}

x = np.arange(len(time_new))
width = 0.25
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in data.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1

ax.set_ylabel('Time (s)')
ax.set_title('Measurement Of Execution Time Of Graph Plotting Modules ')
ax.set_xticks(x + (width / 2))
ax.set_xticklabels(['eq' + str(i) for i in range(1, 11)])
ax.legend(loc='upper left', ncols=2)
ax.set_ylim(0, 15)

file_path = os.path.join(results_dir, 'graph_time_results.jpg')
plt.savefig(file_path)