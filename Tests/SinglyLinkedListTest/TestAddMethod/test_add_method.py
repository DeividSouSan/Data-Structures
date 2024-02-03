
from SinglyLinkedList.singly_linked_list import SinglyLinkedList

class TestAddMethod(object):
    """
    TestAddMethod testa os seguintes casos do método add:

    1. Adição de um valor a uma lista vazia
    2. Adição de um valor a uma lista com valores
    """

    def test_add_to_empty_list(self):
        linked_list = SinglyLinkedList()

        linked_list.add(1)

        assert linked_list.size() == 1, "The item was not added to the list"
        assert linked_list.values() == [1], "The added value is different from the parameter passed"

    def test_add_to_not_empty_list(self):
        linked_list = SinglyLinkedList()

        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)

        assert linked_list.size() == 3, "Not all items where added to the list"
        assert linked_list.values() == [1, 2, 3], "Not all items where added to the list"
