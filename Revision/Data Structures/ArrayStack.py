class ArrayStack:
    def __init__(self):
        self.stack = [] # Using a simple Python list

    def push(self, data):
        self.stack.append(data) # Adds to the "end" (which is our top)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop() # Removes and returns the last item
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1] # Look at the last item