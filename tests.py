import io
import unittest
import xmlrunner


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(4, 2 + 2)


if __name__ == '__main__':
    with open('./results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output),
                      failfast=False,
                      buffer=False,
                      catchbreak=False)
