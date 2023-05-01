import matplotlib.pyplot
import numpy as np

from exceptions import InvalidEquationError

class Plotter:
    def __init__(self, equation, x_range):
        if '=' in equation:
            equation = equation.split('=')[1]
            
        self.equation = equation
        self.x_range = x_range
        self.samples = 100
        self.x = np.linspace(-self.x_range, self.x_range, self.samples)

        try:
            self.y = eval(self.equation, {'x': self.x})
        except Exception:
            raise InvalidEquationError

        self.plt = matplotlib.pyplot

    def set_equation(self, equation):
        if '=' in equation:
            equation = equation.split('=')[1]
            
        self.equation = equation
        self.samples = 100
        self.x = np.linspace(-self.x_range, self.x_range, self.samples)

        try:
            self.y = eval(self.equation, {'x': self.x})
        except Exception:
            raise InvalidEquationError

        self.plt = matplotlib.pyplot
    
    def set_x_range(self, x_range):
        self.x_range = x_range
        self.samples = 100
        self.x = np.linspace(-self.x_range, self.x_range, self.samples)

        try:
            self.y = eval(self.equation, {'x': self.x})
        except Exception:
            raise InvalidEquationError

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

        try:
            self.plt.plot(self.x, self.y)
        except Exception:
            raise InvalidEquationError

    def save(self, filename):
        self.plt.savefig(filename)

    def clear(self):
        self.plt.clf()        