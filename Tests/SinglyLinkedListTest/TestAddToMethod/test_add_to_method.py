import SinglyLinkedList

class TestAddToMethod:
    """
    Essa classe testa os seguintes casos do método add_to da classe SinglyLinkedLists

    1. Adicionar um elemento na posição 0 de uma lista vazia.
    2. Adicionar um elemento na posição 0 de uma lista com vários elementos.
    3. Adicionar um elmento em uma posição no meio da lista.
    4. Adicionar um elemento na última posição da lista.
    5. Adicionar um elemento em uma posição que é maior que o tamanho da lista.
    6. Adicionar um elemento em uma posição negativa.

    """

    def test_add_to_first_pos_of_empty_list(self):
        linked_list = SinglyLinkedLists()
        linked_list.add_to(1, 0)

        assert linked_list.size == 1
        assert linked_list.values == [1]
