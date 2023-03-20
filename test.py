import unittest
from main import csp_coloring

class Unittesting(unittest.TestCase):
    def Test1(self):
        a1 = csp_coloring({1: [3], 3: [1, 19], 2: [18, 19], 18: [2], 19: [3, 2]}, 3)
        self.assertEqual(a1, {1: 0, 18: 0, 19: 0, 2: 1, 3: 1}, "{1: 0, 18: 0, 19: 0, 2: 1, 3: 1}")
        def TestCases():
    TestCases = unittest.TestSuite() 
    TestCases.addTest(Unittesting('runTest1'))
if _name_ == '_main_':
    runner = unittest.TextTestRunner()
    runner.run(TestCases())
