from typing import Self


class DoublyLinkedLists[T]:

    class __Node:
        def __init__(self: Self, value: T, next_node: Self = None, previous_node: Self = None):
            self.__value = value
            self.__next = next_node
            self.__previous = previous_node

        @property
        def value(self) -> T:
            return self.__value

        @value.setter
        def value(self, new_value: T):
            raise Exception("Node 'value' attribute is private.")

        def _set_value(self, new_value) -> None:
            self.__value = new_value

        # next attribute is private, can't be assigned to, but can be modified with setter _set_next(next_node)

        @property
        def next(self) -> Self:
            return self.__next

        @next.setter
        def next(self, next_node: Self):
            raise Exception("Node 'next' attribute is private.")

        def _set_next(self, next_node: Self) -> None:
            self.__next = next_node

        # previous attribute is private, can't be assigned to, but can be modified with setter _set_previous(previous_node)
        @property
        def previous(self) -> Self:
            return self.__previous

        @previous.setter
        def previous(self, previous_node: Self):
            raise Exception("Node 'previous' attribute is private.")

        def _set_previous(self, previous_node) -> None:
            self.__previous = previous_node

        def __str__(self):
            previous = self.previous.__value if self.previous else None
            next = self.next.__value if self.next else None
            return f"<Node v: {self.__value}, p: {previous} n: {next}>"

        def __repr__(self):
            previous = self.previous.__value if self.previous else None
            next = self.next.__value if self.next else None
            return f"<Node v: {self.__value}, p: {previous} n: {next}>"

    first: __Node
    last: __Node

    def __init__(self):
        self.__first = None
        self.__last = None
        self.__length = 0

    @property
    def first(self) -> __Node:
        return self.__first

    @first.setter
    def first(self, new_value: __Node | None):
        raise Exception("DoblyLinkedList 'first' attribute is private.")

    @property
    def last(self) -> __Node:
        return self.__last

    @last.setter
    def last(self, new_value: __Node | None):
        raise Exception("DoblyLinkedList 'last' attribute is private.")

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, nodes_qty: int):
        raise Exception("DoblyLinkedList 'length' attribute is private.")

    def is_empty(self) -> bool:
        return self.first is None and self.length == 0

    def insert_first(self, value: T) -> None:
        new_node = self.__Node(value)

        if self.is_empty():
            self.__first = new_node
            self.__last = new_node
        else:
            new_node._set_next(self.first)
            self.__first._set_previous(new_node)
            self.__first = new_node

        self.__length += 1

    def insert_last(self, value: T) -> None:
        new_node = self.__Node(value)

        if self.is_empty():
            self.__first = new_node
            self.__last = new_node
        else:
            self.__last._set_next(new_node)
            new_node._set_previous(self.__last)

            self.__last = new_node

        self.__length += 1

    def insert_at(self, value: T, pos: int) -> None:
        new_node = self.__Node(value)

        if pos not in [i for i in range(-1, self.__length + 1)]:
            raise Exception("List index out of range.")

        if pos == 0:
            self.__first._set_previous(new_node)
            new_node._set_next(self.first)

            self.__first = new_node
        elif pos == -1:
            self.__last._set_next(new_node)
            new_node._set_previous(self.last)

            self.__last = new_node
        else:
            current_node = self.first
            for i in range(1, self.__length):
                if i == pos:
                    break

                current_node = current_node.next

            new_node._set_next(current_node.next)
            current_node._set_next(new_node)

            new_node._set_previous(current_node)
            current_node.next._set_previous(new_node)

        self.__length += 1

    def remove_first(self) -> __Node:
        if self.is_empty():
            raise Exception("Can't remove from empty list.")

        removed_node = self.__first

        if self.__length == 1:
            self.__first = None
            self.__last = None
        else:
            self.__first = removed_node.next
            self.__first._set_previous(None)

        self.__length -= 1

        return removed_node

    def remove_last(self) -> __Node:
        if self.is_empty():
            raise Exception("Can't remove from empty list.")

        removed_node = self.__last

        if self.__length == 1:
            self.__first = None
            self.__last = None
        else:
            self.__last = removed_node.previous
            self.__last._set_next(removed_node.next)
            
        self.__length -= 1
        
        return removed_node
        
    def transverse(self):
        if self.is_empty():
            raise Exception("Can't tranverse list without items.")

        self.current_node = self.__first

        while self.current_node is not None:
            yield self.current_node.value

            self.current_node = self.current_node.next

    def reversed_transverse(self):
        if self.is_empty():
            raise Exception("Can't tranverse list without items.")

        self.current_node = self.__last

        while self.current_node is not None:
            yield self.current_node.value

            self.current_node = self.current_node.previous

    def get(self, pos: int) -> T:
        if pos == 0:
            return self.__first
        elif pos == -1:
            return self.__last
        else:
            current_node = self.first

            for i in range(1, self.__length + 1):
                current_node = current_node.next

                if i == pos:
                    break

            return current_node

    def swap_next(self, node: __Node) -> None:
        if node.next is None:
            raise Exception("Can't swap the last element.")

        current_node = node
        next_node = node.next

        current_node_value, next_node_value = current_node.value, next_node.value

        current_node._set_value(next_node_value)
        next_node._set_value(current_node_value)

    def sort(self) -> Self:
        count_swap = None

        while count_swap != 0:
            # Bubble Sort ends when there is no swap between elements
            current_node = self.__first
            count_swap = 0

            for _ in range(0, self.__length - 1):
                swap = current_node.value > current_node.next.value
                if swap:
                    count_swap += 1

                    self.swap_next(current_node)

                current_node = current_node.next

    def insert_sorted(self, value: T) -> None:
        self.insert_first(value)
        self.sort()

    def __str__(self):
        return f"<{[item for item in self.transverse()]}>"
