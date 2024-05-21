class Stack[T]:
    def __init__(self):
        self.__items: list[T] = []
        self.__top: T = None

    def push(self, item: T) -> None:
        self.__items.append(item)
        self.__top = item

    def pop(self) -> T:
        if self.is_empty():
            raise EmptyStack("Can't pop empty list")

        removed = self.__items.pop()
        self.__top = self.__items[-1] if not self.is_empty() else None

        return removed

    def is_empty(self) -> bool:
        return len(self.__items) < 1

    def peek(self) -> T:
        if self.is_empty():
            return None

        return self.__top


class EmptyStack(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
