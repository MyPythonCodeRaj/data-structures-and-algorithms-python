import unittest
from data_structures.arrays.single_dimensional_array import SingleDimensionalArray

class TestSingleDimensionalArray(unittest.TestCase):
    def setUp(self):
        self.arr = SingleDimensionalArray(5)
    
    def test_insert(self):
        self.arr.insert(0, 10)
        self.assertEqual(self.arr.array[0], 10)

    def test_delete(self):
        self.arr.insert(0, 10)
        self.arr.delete(0)
        self.assertEqual(self.arr.array[0], None)

    def test_search(self):
        self.arr.insert(0, 10)
        self.assertEqual(self.arr.search(10), 0)
        self.assertEqual(self.arr.search(20), -1)

if __name__ == '__main__':
    unittest.main()
