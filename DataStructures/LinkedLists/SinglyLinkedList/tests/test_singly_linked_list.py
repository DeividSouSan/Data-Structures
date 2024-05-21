
import unittest

from LinkedLists.SinglyLinkedList.data_structure.singly_linked_list import SinglyLinkedList



class TestSinglyLinkedListMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = SinglyLinkedList()

    def test_add(self):
        added_element = self.linked_list.add(1)

        self.assertEqual(added_element, 1, "Added element should be equal 1")
        self.assertEqual(self.linked_list.values(), [1], "List should contain the element 1")
        self.assertEqual(self.linked_list.size(), 1, "List should have size 1")
