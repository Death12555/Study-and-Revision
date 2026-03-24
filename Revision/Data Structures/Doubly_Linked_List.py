class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    def insert_at_beginning(self, data):
        if self.head is None:
            new_node = Node(data, None, None)
            self.head = self.rear = new_node
        
        else:
            new_node = Node(data, self.head, None)
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1

    def insert_at_end(self, data):
        if self.head is None:
            new_node = Node(data, None, None)
            self.head = self.rear = new_node
        
        else:
            new_node = Node(data, None, self.rear)
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1

    def _get_node_at(self, index):
        """Internal helper to find a node by walking from the closest end."""
        if index < self.size / 2:
            # Start from Head and go Forward
            itr = self.head
            for _ in range(index):
                itr = itr.next
        else:
            # Start from Rear and go Backward
            itr = self.rear
            # We need to walk (Size - 1) - Index steps to get back there
            for _ in range(self.size - 1 - index):
                itr = itr.prev
        return itr

    def get_length(self):
        return self.size

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_beginning(data)
            return

        if index==self.size:
            self.insert_at_end(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count==index-1:
                new_node = Node(data, itr.next, itr)
                
                if itr.next:
                    itr.next.prev = new_node

                itr.next = new_node
                self.size += 1
                return
            
            itr = itr.next
            count += 1

    def insert_at_updated(self, index, data):
        if index<0 or index>self.size:
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_beginning(data)
            return

        if index==self.size:
            self.insert_at_end(data)
            return

        target = self._get_node_at(index)
        before_node = target.prev

        new_node = Node(data, target, before_node)
        before_node.next = new_node

        target.prev = new_node

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

    def print_forward(self):
        if self.head is None:
            print("List is Empty.")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' <--> '
            itr = itr.next
        print("Forward: " + llstr + "None")

    def print_backward(self):
        if self.rear is None:
            print("List is Empty.")
            return
        
        itr = self.rear
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' <--> '
            itr = itr.prev # Following the "Back" button
        print("Backward: " + llstr + "None")

    def remove_at(self, index):
            if index<0 or index>=self.get_length():
                raise Exception("Invalid Index")
            
            if index==0:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.rear = None
                self.size -= 1
                return

            if index==self.size -1:
                self.rear = self.rear.prev
                self.rear.next = None
                self.size -= 1
            
            target = self._get_node_at(index)
            # Bridge the gap: Tell the node before to point to the node after
            target.prev.next = target.next
    
            # Bridge the gap: Tell the node after to point to the node before
            target.next.prev = target.prev

            self.size -= 1

            if self.size==0:
                self.head = self.rear = None

    def update_node(self, index, new_data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head.data= new_data
        
        target = self._get_node_at(index)

        target.data = new_data

    def reverse_list(self):
        if not self.head:
            return
        
        curr = self.head
        temp = None

        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp

            curr = curr.prev
        
        if temp:
            self.rear = self.head
            self.head = temp.prev


    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slow = head
        fast = head.next

        while slow!=fast:
            if fast is None or fast.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next
        
        return True

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                break
        else:
            return None
        
        slow = head
        
        while slow!=fast:
            slow = slow.next
            fast = fast.next

        return slow

    def swapPairs(self, head: Optional[Node]) -> Optional[Node]:
        if not head or not head.next:
            return head

        # Handle first pair
        first = head
        second = head.next
        next_pair = second.next

        second.next = first
        second.prev = None
        first.prev = second
        first.next = next_pair
        if next_pair:
            next_pair.prev = first

        self.head = second
        prev_pair_end = first
        curr = next_pair

        # Handle rest
        while curr and curr.next:
            first = curr
            second = curr.next
            next_pair = second.next

            # Swap
            second.next = first
            second.prev = prev_pair_end
            first.next = next_pair
            first.prev = second
            if next_pair:
                next_pair.prev = first
            
            prev_pair_end.next = second

            prev_pair_end = first
            curr = next_pair

        # Update Rear
        self.rear = prev_pair_end if self.size%2==0 else prev_pair_end.next

        return self.head

    def swapPairs_Production_Grade(self):
        if not self.head or not self.head.next:
            return

        dummy = Node(0, self.head)
        anchor = dummy

        while anchor.next and anchor.next.next:
            first = anchor.next
            second = anchor.next.next

            # 1. Point 'first' past 'second'
            first.next = second.next
            if second.next:
                second.next.prev = first

            # 2. Point 'second' back to 'first'
            second.next = first
            first.prev = second

            # 3. Connect the anchor to the new 'second'
            anchor.next = second
            second.prev = anchor

            # 4. Move the anchor two steps (to 'first')
            anchor = first

        # FINAL MANAGER UPDATES
        self.head = dummy.next
        self.head.prev = None

        self.rear = anchor if self.size%2==0 else anchor.next

    @staticmethod
    def mergeTwoLists(l1_head, l2_head):
        dummy = Node(0)
        tail = dummy

        while l1_head and l2_head:
            if l1_head.data < l2_head.data:
                chosen = l1_head
                l1_head = l1_head.next
            else:
                chosen = l2_head
                l2_head = l2_head.next
            
            tail.next = chosen
            chosen.prev = tail
            tail = tail.next

        # Attach the survivors
        survivor = l1_head or l2_head

        if survivor:
            tail.next = survivor
            survivor.prev = tail
        
        new_head = dummy.next
        
        if dummy.next:
            new_head.prev = None

        return dummy.next

    def merge_with(self, other_list):
        if not other_list.head:
            return # Nothing to merge

        dummy = Node(0)
        tail = dummy
    
        l1, l2 = self.head, other_list.head

        while l1 and l2:
            if l1.data < l2.data:
                chosen = l1
                l1 = l1.next
            else:
                chosen = l2
                l2 = l2.next
            tail.next = chosen
            chosen.prev = tail
            tail = tail.next

        # Attach the remaining chain
        survivor = l1 or l2

        if survivor:
            tail.next = survivor
            survivor.prev = tail

        # UPDATE THE MANAGER'S DATA
        # 1. Instant Size Update (instead of a count loop)
        self.size += other_list.size
        self.head = dummy.next

        # 2. Update the Head
        if self.head:
            self.head.prev = None

        # 3. Update the Rear (The part you were guessing)
        itr = tail
        while itr and itr.next:
            itr = itr.next

        self.rear = itr
