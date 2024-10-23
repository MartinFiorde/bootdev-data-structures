class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items = [item] + self.items

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)
