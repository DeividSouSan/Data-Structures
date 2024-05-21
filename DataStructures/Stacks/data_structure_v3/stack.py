

from ...LinkedLists.DoublyLinkedLists.data_structure_v2.linked_list import DoublyLinkedLists


class Stack[T]:
    def __init__(self):
        self.__items: DoublyLinkedLists[T] = DoublyLinkedLists[T]()
        self.__top: T = None

    def push(self, item: T) -> None:
        self.__items.insert_last(item)
        self.__top = item

    def pop(self) -> T:
        if self.is_empty():
            raise EmptyStack("Can't pop empty list")

        removed = self.__items.remove_last()
        self.__top = self.__items.last.value if not self.is_empty() else None

        return removed

    def is_empty(self) -> bool:
        return self.__items.is_empty()

    def peek(self) -> T:
        if self.is_empty():
            return None

        return self.__top


class EmptyStack(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
