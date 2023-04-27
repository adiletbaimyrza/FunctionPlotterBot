import matplotlib.pyplot
import numpy as np

class Plotter:
    def __init__(self, equation, x_range):
        self.equation = equation
        self.x_range = x_range
        self.samples = self.x_range * 10
        self.x = np.linspace(-self.x_range, self.x_range, self.samples)
        self.y = eval(self.equation, {'x': self.x})
        self.plt = matplotlib.pyplot
    
    def coordinate_plane(self):
        self.plt.gca().spines['top'].set_visible(False)
        self.plt.gca().spines['right'].set_visible(False)
        self.plt.gca().spines['bottom'].set_visible(False)
        self.plt.gca().spines['left'].set_visible(False)
        self.plt.grid(True)
        self.plt.axhline(0, color='gray')
        self.plt.axvline(0, color='gray')
        self.plt.xlabel('x axis')
        self.plt.ylabel('y axis')
        self.plt.tick_params(axis='both', length=0)

    def plot(self):
        self.plt.plot(self.x, self.y)

    def save(self, filename):
        self.plt.savefig(filename)

    def clear(self):
        self.plt.clf()        