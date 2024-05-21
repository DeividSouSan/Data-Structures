class Queue[T]:
    def __init__(self):
        self.items: list[T] = []
        self.start: T = None
        self.end: T = None

        self.size = 0
        
    def enqueue(self, item: T) -> None:
        if self.size == 0:
            self.start = item
            self.end = item
        else:
            self.end = item
            
        self.items.append(item)
        self.size += 1

    def dequeue(self) -> T:
        if self.size == 0:
            raise EmptyQueue("Can't deque from empty queue.")
        
        self.size -= 1
        
        if self.size == 0:
            self.start = None
            self.end = None
        else:
            self.start = self.items[1]
            
        return self.items.pop(0)

    def peek(self) -> T:
        return self.start

    def is_empty(self) -> bool:
        return len(self.items) == 0


class EmptyQueue(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        