import unittest

from change import Change

class TestChange(unittest.TestCase):

    def test_1(self):
        ch = Change(15.00, 17.00)
        self.assertEqual([(1, 2.00)], ch.change)

    def test_2(self):
        ch = Change(167.73, 175.00)
        self.assertEqual([(5, 1.00), (1, 2.00), (0.25, 1.00), (.01, 2.00)], ch.change)

    def test_3(self):
        ch = Change(100.00, 275.75)
        self.assertEqual([(100, 1.00), (50, 1.00), (20, 1.00), (5, 1.00), (0.25, 3.00)], ch.change)
        