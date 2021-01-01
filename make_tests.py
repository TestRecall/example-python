import os


def make_test_files(path, current_level, target_level, width, i):
    path = path + "/level_" + str(current_level) + "_" + str(i)
    try:
        os.mkdir(path)
    except OSError:
        print("dir already exists")
    else:
        print("Successfully created the directory %s " % path)

    f = open(path + "/__init__.py", "w")
    f.close()

    f = open(path + "/test_quadrilateral.py", "w")
    f.write(
        """import unittest

class TestCircle(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(4, 2 + 2)

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
"""
    )
    f.close()

    f = open(path + "/test_triangle.py", "w")
    f.write(
        """import unittest

class TestTriangle(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(4, 2 + 2)

    def test_sum_again(self):
        self.assertEqual(4, 2 + 2)

    def test_sum_equal(self):
        self.assertEqual(4, 2 + 2)
"""
    )
    f.close()

    if current_level < target_level:
        make_test_dir(path, current_level + 1, target_level, width)


def make_test_dir(path, current_level, target_level, width):
    for i in range(width):
        make_test_files(path, current_level, target_level, width, i)


cwd = os.getcwd()
base = cwd + "/test"

target_level = 1
width = 9

make_test_dir(base, 0, target_level, width)

tests_created = 0
for i in range(target_level + 1):
    tests_created += 9 ** (i + 2)

print("created {} tests".format(tests_created))
