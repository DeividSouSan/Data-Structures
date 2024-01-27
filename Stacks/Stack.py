class Stack():
    def __init__(self):
        self.items = []
        self.top = None

    def push(self, item):
        self.items.append(item)
        self.top = item
        return item

    def pop(self):
        if self.isEmpty(): return
        
        removed = self.items.pop()
        
        if not self.isEmpty():
            self.top = self.items[-1]

        return removed

    def peek(self):
        if self.isEmpty():
            return
        
        return self.top
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
