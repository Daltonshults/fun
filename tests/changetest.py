import unittest

from change import Change

class TestChange(unittest.TestCase):

    def test_1(self):
        ch = Change(15.00, 17.00)
        self.assertEqual([(1, 2)], ch.change)

    def test_2(self):
        ch = Change(167.73, 175.00)
        self.assertEqual([(5, 1), (1, 2), (0.25, 1), (.01, 2)], ch.change)

    def test_3(self):
        ch = Change(100, 275.75)
        self.assertEqual([(100, 1), (50, 1), (20, 1), (5, 1), (0.25, 3)], ch.change)
        
    def test_negative_change(self):
        ch = Change(175.00, 100.00)
        self.assertEqual([], ch.change)

    def test_equal_change(self):
        ch = Change(10.00, 10.00)
        self.assertEqual([], ch.change)
    