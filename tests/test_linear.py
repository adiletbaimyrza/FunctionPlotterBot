import unittest
import linear

test_strings = [
    'f(x) = 0',
    'f(x) = x',
    'f(x) = 1',
    'f(x) = -1',
    'f(x) = 2',
    'f(x) = -3',
    'f(x) = 0.5',
    'f(x) = -0.25',
    'f(x) = 7x',
    'f(x) = -4x',
    'f(x) = 2x + 1',
    'f(x) = -3x + 2',
    'f(x) = 0.1x',
    'f(x) = -0.8x',
    'f(x) = 3x + 4',
    'f(x) = -2x + 5',
    'f(x) = 4x - 3',
    'f(x) = -5x + 6',
    'f(x) = 10x + 2',
    'f(x) = -7x + 9',
    'f(x) = 100',
    'f(x) = -1000x',
    'f(x) = 1000x'
    ]

test_input_values = [
    (0, 0),
    (1, 0),
    (0, 1),
    (0, -1),
    (0, 2),
    (0, -3),
    (0, 0.5),
    (0, -0.25),
    (7, 0),
    (-4, 0),
    (2, 1),
    (-3, 2),
    (0.1, 0),
    (-0.8, 0),
    (3, 4),
    (-2, 5),
    (4, -3),
    (-5, 6),
    (10, 2),
    (-7, 9),
    (0, 100),
    (-1000, 0),
    (1000, 0)
    ]

tests = [(test_strings[i], test_input_values[i]) for i in range(len(test_strings))]


class TestLinear(unittest.TestCase):

    def test_stringify(self):
        for test in tests:
            self.assertEqual(linear.Linear.stringify(self, test[1][0], test[1][1]), test[0])
