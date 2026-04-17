from collections import deque
from Queue import Queue


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Binary_Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = TreeNode(data)

        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root]) # Use a queue for Level-Order Traversal

        while queue:
            temp = queue.popleft()

            if temp.left is None: # Check Left Child
                temp.left = new_node
                return

            else:
                queue.append(temp.left)

            if temp.right is None: # Check Right Child
                temp.right = new_node
                return

            else:
                queue.append(temp.right)

    def insert_manual(self, data):
        new_node = TreeNode(data)

        if self.root is None:
            self.root = new_node
            return

        queue = Queue() # 1. Initialize custom Queue
        queue.enqueue(self.root)

        while queue: # 2. While loop - check if custom queue has data
            temp = queue.dequeue() # 3. Use dequeue method (Make sure it returns the node!)

            if temp.left is None:
                temp.left = new_node
                return

            else:
                queue.enqueue(temp.left)

            if temp.right is None:
                temp.right = new_node
                return

            else:
                queue.enqueue(temp.right)

    def print_inorder(self, current_node):
        if current_node is None: # 1. THE BASE CASE (The Exit Door)
            return

        self.print_inorder(current_node.left) # 2. THE RECURSIVE STEP (Go Left)

        print(current_node.data, end=" ") # 3. THE ACTION (Print current data)

        self.print_inorder(current_node.right) # 4. THE RECURSIVE STEP (Go Right)

    def print_preorder(self, current_node):
        if current_node is None:
            return

        print(current_node.data, end=" ")

        self.print_preorder(current_node.left)

        self.print_preorder(current_node.right)


    def print_postorder(self, current_node):
        if current_node is None:
            return

        self.print_postorder(current_node.left)

        self.print_postorder(current_node.right)

        print(current_node.data, end=" ")

    def _get_height(self, current_node):
        if current_node is None: # Base Case: If we hit a dead end, return -1
            return -1

        left_height = self._get_height(current_node.left) # Recursive Step: Ask the children how tall they are
        right_height = self._get_height(current_node.right)

        return (1 + max(left_height, right_height)) # The taller child wins, plus 1 for the current node itself

    def get_height(self):
        return self._get_height(self.root)

    def _get_size(self, current_node):
        if current_node is None:
            return 0

        return (1 + self._get_size(current_node.left) + self._get_size(current_node.right))

    def get_size(self):
        return self._get_size(self.root)

    def _search(self, current_node, key, index=0):
        """Standard search that returns the Node object itself."""
        if current_node is None:
            return None

        if current_node.data==key:
            return current_node, index

        # Search Left: Index becomes (2 * index + 1)
        res = self._search(current_node.left, key, 2*index+1)
        if res:
            return res

        # Search Right: Index becomes (2 * index + 2)
        return self._search(current_node.right, key, 2*index+2)

    def search(self, key):
        """The 'Manager' function that coordinates the specialized tools."""
        result = self._search(self.root, key)

        if not result:
            print(f"Node {key} not found.")
            return

        # Reuse your existing, tested tools!
        target_node, index = result
        height = self._get_height(target_node)
        size = self._get_size(target_node)

        return target_node, height, size, index


if __name__ == '__main__':
    tree = Binary_Tree()
    trees_manual = Binary_Tree()
    # No more manual tree.root.left = Node(5)!
    values = [1, 2, 3, 4, 5, 6]

    for v in values:
        tree.insert(v)

    for v in values:
        trees_manual.insert_manual(v)
    
    print("Inorder of automated tree:")
    tree.print_inorder(tree.root)
    print()
    print("Inorder of automated tree:")
    trees_manual.print_inorder(trees_manual.root)
    print()
    tree.print_postorder(tree.root)
    print()
    # Calling our new public method
    print(f"Tree Height (Edges): {tree.get_height()}")
    
    # If you want to know the number of "Levels/Layers" (Nodes):
    print(f"Number of Levels: {tree.get_height() + 1}")
    print()
    print("Checking search functionality:")
    print("Checking search functionality:")
    # Capture the return values from the manager function
    result = tree.search(2)

    if result:
        # Unpack the tuple: (target_node, height, size, index)
        node, h, s, idx = result
        
        # Now use 'idx' and 'node.data' (the key) for your print
        print(f"Node {node.data} is at Index {idx} (Level-Order position).")
        print(f"Subtree Height: {h}, Subtree Size: {s}")
