import unittest
from data_structures.linked_lists.circular_linked_list import CircularLinkedList

class TestCircularLinkedList(unittest.TestCase):
    def setUp(self):
        self.circular_linked_list = CircularLinkedList()

    def test_append(self):
        self.circular_linked_list.append(10)
        self.assertEqual(self.circular_linked_list.head.data, 10)

    def test_prepend(self):
        self.circular_linked_list.append(10)
        self.circular_linked_list.prepend(5)
        self.assertEqual(self.circular_linked_list.head.data, 5)

    def test_delete(self):
        self.circular_linked_list.append(10)
        self.circular_linked_list.delete(10)
        self.assertIsNone(self.circular_linked_list.head)

    def test_search(self):
        self.circular_linked_list.append(10)
        self.assertTrue(self.circular_linked_list.search(10))
        self.assertFalse(self.circular_linked_list.search(20))

if __name__ == '__main__':
    unittest.main()
