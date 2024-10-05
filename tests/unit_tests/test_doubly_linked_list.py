import unittest
from data_structures.linked_lists.doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.doubly_linked_list = DoublyLinkedList()

    def test_append(self):
        self.doubly_linked_list.append(10)
        self.assertEqual(self.doubly_linked_list.head.data, 10)

    def test_prepend(self):
        self.doubly_linked_list.append(10)
        self.doubly_linked_list.prepend(5)
        self.assertEqual(self.doubly_linked_list.head.data, 5)

    def test_delete(self):
        self.doubly_linked_list.append(10)
        self.doubly_linked_list.delete(10)
        self.assertIsNone(self.doubly_linked_list.head)

    def test_search(self):
        self.doubly_linked_list.append(10)
        self.assertTrue(self.doubly_linked_list.search(10))
        self.assertFalse(self.doubly_linked_list.search(20))

if __name__ == '__main__':
    unittest.main()
