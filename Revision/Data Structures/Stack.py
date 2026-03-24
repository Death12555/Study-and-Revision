class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.name = ''
        self._top = None
        self.size = 0

    def is_empty(self) -> bool:
        return self._top is None
    
    def push(self, data) -> None:
        newNode = Node(data)

        newNode.next = self._top
        self._top = newNode

        self.size += 1

    def pop(self) -> any:
        if self.is_empty():
            raise Exception('Stack is empty, cannot pop.')

        node_to_delete = self._top
        self._top = self._top.next
        self.size -= 1

        return node_to_delete.data

    def display(self):
        node = self._top
        while node is not None:
            print(node.data)
            node = node.next

    def search(self, data):
        position = 0
        node = self._top

        while node is not None:
            if node.data==data:
                return position
            node = node.next
            position += 1
        
        return -1
    
    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty, cannot peek.')

        return self._top.data


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.pop()
stack.pop()
stack.pop()

stack.push(5)
stack.push(6)
stack.push(7)

stack.pop()

stack.push(8)
stack.push(9)

stack.display()



# newStack = Stack('my stack') 