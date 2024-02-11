from typing import TypeVar
from Stacks.data_structure.stack import Stack
from .node import Node

T = TypeVar('T')


class SinglyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def add(self, value: T) -> T:
        new_node = Node(value, None)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return new_node.value

        self.tail.next = new_node
        self.tail = new_node
        return new_node.value

    def add_to(self, value: T, index: int) -> T:
        MAX_INDEX = self.size()

        if index < 0 or index > MAX_INDEX:
            raise IndexError("List index out of range")

        if index == 0:
            self.head = Node(value, self.head)
            return self.head.value

        elif index == MAX_INDEX:
            self.add(value)
            return self.tail.value

        else:
            current_node: Node = self.head

            for _ in range(index - 1):
                current_node = current_node.next

            current_node.next = Node(value, current_node.next)
            return current_node.next.value

    def contains(self, value: T) -> bool:
        current_node: Node = self.head

        while (current_node is not None) and (current_node.value != value):
            current_node = current_node.next

        return bool(current_node)

    def delete(self, value):
        if self.head is None:
            return False

        if self.head.value == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return True

            self.head = self.head.next
            return True

        else:
            current_node = self.head

            while (current_node.next is not None) and (current_node.next.value != value):
                current_node = current_node.next

            if current_node.next is not None:
                if current_node.next == self.tail:  # Pré-condição: O próximo nó é o último

                    self.tail = current_node
                    self.tail.next = None
                    return True

                current_node.next = current_node.next.next
                return True

        return False  # Caso 6: O valor procurado não está na lista

    def transverse(self):
        current_node = self.head

        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

    def transverse_reverse(self):
        if self.tail is not None:
            current_node = self.tail

            while current_node != self.head:
                previous_node = self.head

                while previous_node.next != current_node:
                    previous_node = previous_node.next
                    # Previous node vai se tornar o nó anterior ao current node

                yield current_node.value
                current_node = previous_node

            yield current_node.value

    def transverse_reverse_stack(self):
        stack = Stack()

        for item in self.transverse():
            stack.push(item)

        while not stack.is_empty():
            yield stack.pop()

    def size(self):
        size = 0
        for _ in self.transverse():
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
