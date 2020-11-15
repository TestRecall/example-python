import unittest

class TestCircle(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(5, 2 + 2)

    def test_sum_again(self):
        self.assertEqual(4, 2 + 2)

    def test_sum_equal(self):
        self.assertEqual(4, 2 + 2)

class TestSquare(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(4, 2 + 2)

    def test_sum_again(self):
        self.assertEqual(4, 2 + 2)

    def test_sum_equal(self):
        self.assertEqual(4, 2 + 2)
