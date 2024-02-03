from singly_linked_list import SinglyLinkedLists

class TestDeleteMethod(object):
    """
    TestDeleteMethod testa os seguintes casos do método delete:

    1. Deletar um elemento de uma lista vazia.
    2. Deletar um elemento de uma lista com um elemento.
    3. Deletar um elemento de uma lista com vários elementos.
    4. Deletar o primeiro elemento da lista.
    5. Deletar o último elemento da lista.
    6. Deletar um elemento que não existe em uma lista com vários elementos.
    7. Deletar um elemento que aparece duas vezes na lista

    """

    def test_delete_from_empty_list(self):
        linked_list = SinglyLinkedLists()

        assert linked_list.delete(1) == False, "A lista está vazia, mas o método delete retornou True"

    def test_delete_the_only_node_in_list(self):
        linked_list = SinglyLinkedLists()

        linked_list.add(1)

        assert linked_list.delete(1) == True, "O método delete retornou False, mas o nó foi deletado"
        assert linked_list.size() == 0, "A lista não está vazia"
        assert linked_list.values() == [], "A lista não está vazia"

    def test_delete_node_from_list(self):
        linked_list = SinglyLinkedLists()

        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)

        assert linked_list.delete(2) == True, "O método delete retornou False, mas o nó foi deletado"
        assert linked_list.size() == 2, "A lista não tem tamanho 2"
        assert linked_list.values() == [1, 3], "A lista não contém os elementos [1, 3]"

    def test_delete_first_node_from_list(self):
        linked_list = SinglyLinkedLists()

        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)

        assert linked_list.delete(1) == True, "O método delete retornou False, mas o nó foi deletado"
        assert linked_list.size() == 2, "A lista não tem tamanho 2"
        assert linked_list.values() == [2, 3], "A lista não contém os elementos [2, 3]"

    def test_delete_last_node_from_list(self):
        linked_list = SinglyLinkedLists()

        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)

        assert linked_list.delete(3) == True, "O método delete retornou False, mas o nó foi deletado"
        assert linked_list.size() == 2, "A lista não tem tamanho 2"
        assert linked_list.values() == [1, 2], "A lista não contém os elementos [1, 2]"

    def test_delete_node_that_doesnt_exist(self):
        linked_list = SinglyLinkedLists()

        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)

        assert linked_list.delete(4) == False, "O método delete retornou True, mas o nó não existe"
        assert linked_list.size() == 3, "A lista não tem tamanho 3"
        assert linked_list.values() == [1, 2, 3], "A lista não contém os elementos [1, 2, 3]"

    def test_delete_node_that_appear_twice(self):
        linked_list = SinglyLinkedLists()

        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)
        linked_list.add(2)

        assert linked_list.delete(2) == True, "O método delete retornou False, mas o nó foi deletado"
        assert linked_list.size() == 3, "A lista não tem tamanho 3"
        assert linked_list.values() == [1, 3, 2], "A lista não contém os elementos [1, 3, 2]"
