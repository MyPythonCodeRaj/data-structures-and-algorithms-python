import unittest
from data_structures.linked_lists.singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = SinglyLinkedList()

    def test_append(self):
        self.linked_list.append(10)
        self.assertEqual(self.linked_list.head.data, 10)

    def test_prepend(self):
        self.linked_list.append(10)
        self.linked_list.prepend(5)
        self.assertEqual(self.linked_list.head.data, 5)

    def test_delete(self):
        self.linked_list.append(10)
        self.linked_list.delete(10)
        self.assertIsNone(self.linked_list.head)

    def test_search(self):
        self.linked_list.append(10)
        self.assertTrue(self.linked_list.search(10))
        self.assertFalse(self.linked_list.search(20))

if __name__ == '__main__':
    unittest.main()
