import unittest
from data_structures.arrays.dynamic_array import DynamicArray

class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        self.dyn_arr = DynamicArray()

    def test_append(self):
        self.dyn_arr.append(10)
        self.assertEqual(self.dyn_arr.array[0], 10)

    def test_insert(self):
        self.dyn_arr.append(10)
        self.dyn_arr.insert(1, 20)
        self.assertEqual(self.dyn_arr.array[1], 20)

    def test_delete(self):
        self.dyn_arr.append(10)
        self.dyn_arr.delete(10)
        self.assertEqual(self.dyn_arr.array, [])

    def test_search(self):
        self.dyn_arr.append(10)
        self.assertEqual(self.dyn_arr.search(10), 0)
        self.assertEqual(self.dyn_arr.search(20), -1)

if __name__ == '__main__':
    unittest.main()
