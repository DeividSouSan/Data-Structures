from typing import Optional, TypeVar


T = TypeVar('T')


class Stack:
    def __init__(self):
        self.items: list[T] = []
        self.top: Optional[T] = None
        self.size: int = 0

    def push(self, item: T) -> T:
        self.items.append(item)
        self.top = item
        self.size += 1
        return item

    def pop(self) -> T:
        if self.is_empty():
            raise EmptyStack("Can't pop empty list")

        removed = self.items.pop()
        self.size -= 1
        self.top = self.items[-1] if not self.is_empty() else None

        return removed

    def is_empty(self) -> bool:
        return self.size == 0

    def peek(self) -> T:
        if self.is_empty():
            return None

        return self.top


class EmptyStack(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
