import unittest
from data_structures.arrays.multi_dimensional_array import Matrix

class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix(3, 3)

    def test_insert(self):
        self.matrix.insert(0, 0, 5)
        self.assertEqual(self.matrix.get_value(0, 0), 5)

    def test_transpose(self):
        self.matrix.insert(0, 1, 2)
        self.matrix.insert(1, 0, 4)
        transposed = self.matrix.transpose()
        self.assertEqual(transposed[1][0], 2)
        self.assertEqual(transposed[0][1], 4)

if __name__ == '__main__':
    unittest.main()