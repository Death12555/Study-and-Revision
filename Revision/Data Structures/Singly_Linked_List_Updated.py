from typing import Optional


class Node:
    def __init__(self, data= None, next= None):
        self.data = data
        self.next = next


class Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

        if self.size==0:
            self.rear = new_node
        
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

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
                itr.next = Node(data, itr.next)
                self.size += 1
                return
            
            itr = itr.next
            count += 1

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

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head = self.head.next
            self.size -= 1
            if self.size==0:
                self.rear = None
            return
        
        itr = self.head
        count = 0

        while itr:
            if count==index-1:
                if index==self.size-1:
                    itr.next = None
                    self.rear = itr
                else:
                    itr.next = itr.next.next
                
                self.size -= 1
                return
            
            itr = itr.next
            count += 1

    def print_list(self):
        if self.head is None:
            print("List is Empty.")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print (llstr + "None")

    def update_node(self, index, new_data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head.data= new_data
        
        itr = self.head
        count = 0

        while itr:
            if count==index:
                itr.data = new_data
                return
            
            itr = itr.next
            count += 1

    def reverse_list(self):
        if not self.head:
            return None

        prev = None
        current = self.head
        old_head = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
        self.rear = old_head
        self.rear.next = None
        return prev

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
        # 1. Edge Case: 0 or 1 nodes
        if not head or not head.next:
            return head

        # 2. Handle the first swap manually to set the new head
        first = head
        second = head.next
        next_pair = second.next

        second.next = first
        first.next = next_pair
        
        self.head = second # Update the manager
        prev_pair_end = first
        curr = next_pair

        # 3. Loop for remaining pairs
        while curr and curr.next:
            first = curr
            second = curr.next
            next_pair = second.next

            # Swap
            second.next = first
            first.next = next_pair
            prev_pair_end.next = second

            # Move forward
            prev_pair_end = first
            curr = next_pair

        # 4. Update Rear
        self.rear = prev_pair_end if self.size%2==0 else prev_pair_end.next

        return self.head

    def swapPairs_Production_Grade(self):
        old_head = self.head
        dummy = Node(0, self.head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        self.head = dummy.next

        self.rear = prev if self.size%2==0 else prev.next

    @staticmethod
    def mergeTwoLists(l1_head, l2_head):
        dummy = Node(0)
        tail = dummy

        while l1_head and l2_head:
            if l1_head.data < l2_head.data:
                tail.next = l1_head
                l1_head = l1_head.next
            else:
                tail.next = l2_head
                l2_head = l2_head.next
            tail = tail.next
        

        # Attach the survivors
        tail.next = l1_head or l2_head
    
        return dummy.next

    def merge_with(self, other_list):
        if not other_list.head:
            return # Nothing to merge

        dummy = Node(0)
        tail = dummy
    
        l1 = self.head
        l2 = other_list.head

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach the remaining chain
        tail.next = l1 or l2
    
        # UPDATE THE MANAGER'S DATA
        # 1. Instant Size Update (instead of a count loop)
        self.size += other_list.size 
    
        # 2. Update the Head
        self.head = dummy.next
    
        # 3. Update the Rear (The part you were guessing)
        itr = tail
        while itr and itr.next:
            itr = itr.next
        self.rear = itr

