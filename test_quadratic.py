import unittest
import quadratic

test_strings = [
    # Zero coefficients
    'f(x) = 0',
    'f(x) = 1',
    'f(x) = -1',
    'f(x) = -x^2',
    'f(x) = x',
    'f(x) = -x',
    'f(x) = x^2',
    
    # Extreme input values
    'f(x) = x + 1',
    'f(x) = -x + 1',
    'f(x) = 1000x + 1',
    'f(x) = -1000x + 1',
    'f(x) = x^2 + 1',
    'f(x) = -x^2 + 1',
    'f(x) = x^2 + x - 1',
    'f(x) = -x^2 - x + 1',
    'f(x) = x^2 - x + 1',
    'f(x) = x^2 - x - 1',
    'f(x) = -x^2 - 1',
    
    # Quadratic functions with multiple terms
    'f(x) = x^2 + 2x + 1',
    'f(x) = 2x^2 - 3x + 1',
    'f(x) = -3x^2 + 2x - 1',
    'f(x) = 0.1x^2 - 0.2x + 0.3',
    'f(x) = -0.8x^2 + 1.6x - 2.4',
    'f(x) = 4x^2 - 3x - 2',
    'f(x) = -5x^2 + 6x + 7',
    'f(x) = 10x^2 + 2x + 1',
    'f(x) = -7x^2 + 9x - 11',
    'f(x) = 100x^2',
    'f(x) = -1000x^2',
    'f(x) = 1000x^2'
]

test_input_values = [
    # Zero coefficients
    (0, 0, 0),
    (0, 0, 1),
    (0, 0, -1),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (1, 0, 0),
    
    # Extreme input values
    (0, 1, 1),
    (0, -1, 1),
    (0, 1000, 1),
    (0, -1000, 1),
    (1, 0, 1),
    (-1, 0, 1),
    (1, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, -1, -1),
    (-1, 0, -1),
    
    # Quadratic functions with multiple terms
    (1, 2, 1),
    (2, -3, 1),
    (-3, 2, -1),
    (0.1, -0.2, 0.3),
    (-0.8, 1.6, -2.4),
    (4, -3, -2),
    (-5, 6, 7),
    (10, 2, 1),
    (-7, 9, -11),
    (100, 0, 0),
    (-1000, 0, 0),
    (1000, 0, 0)
]

tests = [(test_strings[i], test_input_values[i]) for i in range(len(test_strings))]


class TestQuadratic(unittest.TestCase):

    def test_stringify(self):
        for test in tests:
            self.assertEqual(quadratic.Quadratic.stringify(self, test[1][0], test[1][1], test[1][2]), test[0])
