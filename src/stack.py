# Operation 	Big O 	Description
# push 	        O(1) 	Add an item to the top of the stack
# pop 	        O(1) 	Remove and return the top item from the stack
# peek 	        O(1) 	Return the top item from the stack without modifying the stack
# size 	        O(1) 	Return the number of items in the stack
# 
# Stack operations are limited: no searching, no sorting, no random access


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        pass

    def pop(self):
        pass
