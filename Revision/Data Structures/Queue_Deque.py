from collections import deque

# Initialize the queue
queue = deque()

# Enqueue (Adding to the "Rear")
queue.append(10)
queue.append(20)

# Dequeue (Removing from the "Front")
first_item = queue.popleft() 

print(first_item) # Output: 10