class Node:
    def __init__(self, data= None, next= None):
        self.data = data
        self.next = next


class Singly_Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def get_length(self):
        count = 0

        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        
        return count

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head

        while itr:
            if count==index-1:
                itr.next = Node(data, itr.next)
                return
            
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        # self.head = None, Keep this line if you want to keep old values in the memory other wise Garbage collector will remove it from RAM automatically
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0

        while itr:
            if count==index-1:
                itr.next = itr.next.next
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

        print (llstr)

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
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
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

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        curr = head

        while curr and curr.next:
            # THE FIX: Save the next pair's entrance
            next_pair = curr.next.next 
            temp = curr.next 

            # THE SWAP: Flip the current two
            temp.next = curr
            curr.next = next_pair

            # THE CONNECTION: Link the previous pair to this one
            if prev:
                prev.next = temp
            else:
                head = temp # Update our local "head" variable

            # THE JUMP: Move precisely to the next pair
            prev = curr
            curr = next_pair 

        return head # Return the new start to the caller

    def swapPairs_Production_Grade(self):
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


if __name__== '__main__':
    ll = Singly_Linked_List()
    ll.insert_at_beginning(56)
    ll.insert_at_beginning(90)
    ll.insert_at_beginning(100)
    ll.print_list()
    ll.insert_at_end(67)
    ll.insert_at_end(92)
    ll.insert_at_end(36)
    ll.print_list()
    ll.insert_values([34, 78, 89, 675])
    ll.print_list()
    ll.insert_at(3, 85)
    ll.print_list()
    ll.remove_at(4)
    ll.print_list()
    ll.update_node(2, 64)
    ll.print_list()
    ll.reverse_list()
    ll.print_list()
    ll.head = ll.swapPairs(ll.head)
    ll.print_list()
