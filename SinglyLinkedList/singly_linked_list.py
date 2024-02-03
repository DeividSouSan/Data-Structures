from .node import Node


class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        newNode = Node(value, None)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # Note que self.tail é um Node e nós mudamos o next de None para newNode
            self.tail.next = newNode
            self.tail = newNode

    def add_to(self, value, index):
        MAX_INDEX = self.size()
        if index < 0 or index > MAX_INDEX:
            raise IndexError("list index out of range")

        if index == 0:
            self.head = Node(value, self.head)
        elif index == MAX_INDEX:
            self.add(value)
        else:
            currentNode = self.head
            for _ in range(index - 1):
                currentNode = currentNode.next
            currentNode.next = Node(value, currentNode.next)

    def contains(self, value):
        currentNode = self.head

        while (currentNode is not None) and (currentNode.value != value):
            currentNode = currentNode.next

        return True if currentNode else False

    def delete(self, value):
        if self.head is None:  # Caso 1: a lista está vazia
            return False

        elif self.head.value == value:  # Pré-condição: O valor está no primeiro nó
            # Caso 2: o primeiro nó e o último nó são os mesmos (só há um elemento na lista)
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return True

            else:
                # Caso 3: O primeiro nó guarda o valor procurado, mas existem mais nós na lista
                self.head = self.head.next
                return True
            
        else:  # Pré-condição: O valor procurado não está no primeiro nó e a lista não está vazia
            currentNode = self.head

            # Enquanto o proximo valor for não-nulo e enquanto o proximovalor não for o que eu procuro, roda o loop
            while (currentNode.next is not None) and (currentNode.next.value != value):
                currentNode = currentNode.next

            # Pré-condição: o valor do nó atual não é nulo, ou seja, currentNode não é último nó.
            if currentNode.next is not None:
                if currentNode.next == self.tail:  # Pré-condição: O próximo nó é o último
                    # Caso 4: O valor se encontra no último nó
                    self.tail = currentNode
                    self.tail.next = None
                    return True
                else:  # O proximo nó não é o último
                    # Caso 5: O valor se encontra no meio da lista
                    currentNode.next = currentNode.next.next
                    return True

        return False  # Caso 6: O valor procurado não está na lista

    def transverse(self):
        currentNode = self.head

        while (currentNode is not None):
            yield currentNode.value
            currentNode = currentNode.next

    def transverse_reverse(self):
        if self.tail is not None:
            currentNode = self.tail

            while currentNode != self.head:
                previousNode = self.head

                while previousNode.next != currentNode:
                    previousNode = previousNode.next
                    # Previous node vai se tornar o nó anterior ao current node

                yield currentNode.value
                currentNode = previousNode

            yield currentNode.value

    def transverse_reverse_stack(self):
        stack = Stack()

        for item in self.transverse():
            stack.push(item)

        while not stack.isEmpty():
            yield stack.pop()


    def size(self):
        size = 0
        for item in self.transverse():
            size += 1

        return size

    def values(self):
        values = []
        for item in self.transverse():
            values.append(item)

        return values
            
    def display(self):
        for item in self.transverse():
            print(item, end=" ")
        print("")
