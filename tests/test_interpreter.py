import unittest
import interpreter

test_linears = [
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
    'f(x) = 1000x',
    ]

class TestInput(unittest.TestCase):

    def test_check_pattern_linear(self):
        for test in test_linears:
            
            self.assertTrue(interpreter.Input.check_pattern_linear(test), msg=test)
    
            