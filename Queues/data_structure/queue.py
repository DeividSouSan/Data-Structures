class Queue[T]:
    def __init__(self):
        self.items: list[T] = []
        self.size = 0

    def enqueue(self, item: T) -> None:
        self.items.append(item)
        self.size += 1

    def dequeue(self) -> T:
        if self.size == 0:
            raise EmptyQueue("Can't deque from empty queue.")
        
        self.size -= 1
        return self.items.pop(0)

    def peek(self) -> T:
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0


class EmptyQueue(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        