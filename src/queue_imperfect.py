# Operation 	Big O 	Description
# push 	O(1) 	Add an item to the back of the queue (items[0] position)
# pop 	O(1) 	Remove and return the front item from the queue (items[-1] position)
# peek 	O(1) 	Return the front item from the queue without modifying the queue
# size 	O(1) 	Return the number of items in the queue
# 
# Our current Queue class has a problem... take a look at the push method:
# 
# def push(self, item):
#     self.items.insert(0, item)
# 
# It's O(n), not O(1)! The List's insert method has to shift ALL other items down in the list to make room for the new item.

class QueueImperfect:
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

class QueueMatchmaking:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self):
        return f"[{', '.join(self.items)}]"
