from .node import Node


class LinkedList:
    def __init__(self):
        self.items = None
        self.head = None
        self.tail = None

    # O(1)
    def add(self, value: int) -> None:
        newNode = Node(value, None, None)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    # O(n)
    def contains(self, value: int) -> None:
        currentNode = self.head

        while currentNode != None and currentNode.value != value:
            currentNode = currentNode.next

        return True if currentNode else False

    def delete(self, value):
        # A lista está vazia
        if self.head is None:
            return False

        if self.head.value == value:
            # O valor está no primeiro nó e último nó ao mesmo tempo
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return True

            # O valor está no primeiro nó mas existem outros
            else:
                self.head = self.head.next
                self.head.prev = None
                return True

        # O valor está no último nó da lista
        if self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            return True

        # O valor não está no promeiro nem no último nó
        currentNode = self.head
        while currentNode != None:
            if currentNode.value == value:
                currentNode.next.prev = currentNode.prev
                currentNode.prev.next = currentNode.next

                return True
            currentNode = currentNode.next

        # O valor procurado não está na lista
        return False

    def transverse(self):
        # mesma implementação do singly linked list
        pass

    def reverseTransverse(self):
        currentNode = self.tail
        while currentNode != None:
            yield currentNode.value
            currentNode = currentNode.prev

    def display(self):
        try:
            currentNode = self.head
            while currentNode.next != None:
                yield currentNode.value
                currentNode = currentNode.next
            yield currentNode.value
        except:
            return
