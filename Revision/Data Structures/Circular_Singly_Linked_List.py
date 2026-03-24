import random


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Circular_Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.rear = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.rear.next = self.head

        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.rear = new_node
            new_node.next = self.head
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.head

        self.size += 1

    def get_length(self):
        return self.size

    def _get_node_at(self, index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        itr = self.head
        for _ in range(index):
            itr = itr.next

        return itr

    def get_circular_node(self, index):
        if self.get_length()==0:
            raise Exception("List is Empty")

        actual_index = index % self.size

        itr = self.head
        for _ in range(actual_index):
            itr = itr.next

        return itr

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_beginning(data)
            return

        if index==self.size:
            self.insert_at_end(data)
            return

        prev = self._get_node_at(index-1)
        new_node = Node(data, prev.next)
        prev.next = new_node
        self.size += 1

    def insert_values(self, data_list):
        """The 'Reset' Button: Wipes everything and starts fresh."""
        self.head = None
        self.rear = None
        self.size = 0
        self.extend(data_list) # Reuses the logic below!

    def extend(self, data_list):
        """The 'Append' Button: Keeps old values and adds new ones to the back."""
        for data in data_list:
            self.insert_at_end(data)

    def print_list(self):
        if self.head is None:
            print("List is Empty.")
            return

        itr = self.head
        llstr = ''

        while itr: #Or while True
            llstr += str(itr.data) + '-->'
            itr = itr.next
            if itr==self.head:
                break

        print(llstr + "(Head)")

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            if self.size==1:
                self.head = self.rear = None
            else:
                self.head = self.head.next
                self.rear.next = self.head
            self.size -= 1
            return

        if index==self.size-1:
            new_rear = self._get_node_at(self.size-2)
            new_rear.next = self.head
            self.rear = new_rear
            self.size -= 1
            return

        prev = self._get_node_at(index-1)
        prev.next = prev.next.next

        self.size -= 1

    def update_node(self, index, new_data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head.data= new_data
        
        target = self._get_node_at(index)
        target.data = new_data

    def reverse_list(self):
        if not self.head or self.size<=1:
            return self.head

        old_head = self.head
        old_rear = self.rear
        prev = self.rear
        current = self.head

        for _ in range(self.size):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = old_rear
        self.rear = old_head

        return self.head

    def hasCycle(self):
        # A circular list is, by definition, a cycle.
        # If it's not empty, it has a cycle.
        return self.head is not None

    def detectCycle(self):
        return self.head # The racetrack always starts at the starting line.

    def swapPairs(self, head: Optional[Node]) -> Optional[Node]:
        if not head or self.size < 2:
            return head

        # Handle first pair
        first = head
        second = head.next
        next_pair = second.next

        second.next = first
        first.next = next_pair
        
        self.head = second
        prev_pair_end = first
        curr = next_pair

        # Use size to control the loop
        for _ in range((self.size // 2) - 1):
            if not curr or not curr.next: break
            
            first = curr
            second = curr.next
            next_pair = second.next

            second.next = first
            first.next = next_pair
            prev_pair_end.next = second

            prev_pair_end = first
            curr = next_pair

        # Update Rear and Close the Circle
        self.rear = prev_pair_end if self.size%2==0 else prev_pair_end.next

        self.rear.next = self.head # Re-stitch the circle
        
        return self.head

    def swapPairs_Production_Grade(self):
        if self.size<2:
            return

        dummy = Node(0, self.head)
        anchor = dummy

        for _ in range(self.size // 2):
            first = anchor.next
            second = first.next

            first.next = second.next
            second.next = first
            anchor.next = second

            anchor = first

        self.head = dummy.next
        self.rear = anchor if self.size%2==0 else anchor.next
        self.rear.next = self.head

    @staticmethod
    def mergeTwoLists(l1_head, l1_size, l2_head, l2_size):
        # We must return (Head, Rear, Size) in every scenario!
        # Note: Finding the rear of a passed head requires a walk if it's not provided.
        # But for your extend/merge logic, these are safe:
        if not l1_head: 
            itr = l2_head
            for _ in range(l2_size - 1): itr = itr.next
            return l2_head, itr, l2_size
            
        if not l2_head:
            itr = l1_head
            for _ in range(l1_size - 1): itr = itr.next
            return l1_head, itr, l1_size

        dummy = Node(0)
        tail = dummy
        count1, count2 = 0, 0

        while count1<l1_size and count2<l2_size:
            if l1_head.data<=l2_head.data:
                tail.next = l1_head
                l1_head = l1_head.next
                count1 += 1
            else:
                tail.next = l2_head
                l2_head = l2_head.next
                count2 += 1

            tail = tail.next

        while count1<l1_size:
            tail.next = l1_head
            l1_head = l1_head.next
            count1 += 1
            tail = tail.next

        while count2<l2_size:
            tail.next = l2_head
            l2_head = l2_head.next
            count2 += 1
            tail = tail.next

        new_head = dummy.next
        tail.next = new_head
        new_size = l1_size+l2_size

        return new_head, tail, new_size

    def merge_with(self, other_list):
        if not other_list.head:
            return

        if not self.head:
            self.head = other_list.head
            self.rear = other_list.rear
            self.size = other_list.size
            return

        # If user only sends other_list.head as argument change other_list.rear to other_list.prev and use loop to find size
        new_head, new_rear, total_size = self.mergeTwoLists(
            self.head, self.size, 
            other_list.head, other_list.size
        )

        self.head = new_head
        self.rear = new_rear
        self.size = total_size

    def shuffle(self):
        if self.size < 2:
            return

        # 1. Collect all data
        data_pool = []
        itr = self.head
        for _ in range(self.size):
            data_pool.append(itr.data)
            itr = itr.next

        # 2. Scramble
        random.shuffle(data_pool)

        # 3. Refill the nodes with new data
        itr = self.head
        for data in data_pool:
            itr.data = data
            itr = itr.next

    def shuffle_nodes(self):
        if self.size < 2:
            return
            
        for i in range(self.size):
            # Pick a random index
            target_idx = random.randint(0, self.size - 1)
            
            # Pop the data out of that spot
            # (Note: We'll use data to make it easier, 
            # but we are physically changing the list structure)
            data = self._get_node_at(target_idx).data
            self.remove_at(target_idx)
            
            # Put it at the front
            self.insert_at_beginning(data)