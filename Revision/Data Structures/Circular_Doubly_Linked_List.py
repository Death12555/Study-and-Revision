import random

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Circular_Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.rear = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.rear
            self.head.prev = new_node
            self.rear.next = new_node
            self.head = new_node

        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.rear = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.rear
            self.head.prev = new_node
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def _get_node_at(self, index):
        """Internal helper to find a node by walking from the closest end."""
        if index < self.size // 2:
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

        while True:
            llstr += str(itr.data) + ' <--> '
            itr = itr.next
            if itr==self.head:
                break
        print("Forward: " + llstr + "(Head)")

    def print_backward(self):
        if self.rear is None:
            print("List is Empty.")
            return
        
        itr = self.rear
        llstr = ''

        while True:
            llstr += str(itr.data) + ' <--> '
            itr = itr.prev # Following the "Back" button
            if itr==self.rear:
                break
        print("Backward: " + llstr + "(Rear)")

    def remove_at(self, index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if self.size==1:
            self.head = self.rear = None
            self.size = 0
            return

        target = self._get_node_at(index)
        before = target.prev
        after = target.next

        if index==0:
            self.head = after
            self.rear.next = self.head
            self.head.prev = self.rear

        elif index==self.size-1:
            self.rear = before
            self.rear.next = self.head
            self.head.prev = self.rear

        else:
            before.next = after
            after.prev = before

        self.size -= 1

    def update_node(self, index, new_data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        target = self._get_node_at(index)
        target.data = new_data

    def reverse_list(self):
        if not self.head or self.size<=1:
            return self.head

        current = self.head

        for _ in range(self.size):
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            current = next_node

        temp = self.head
        self.head = self.rear
        self.rear = temp

        return self.head

    def hasCycle(self):
        # A circular list is, by definition, a cycle.
        # If it's not empty, it has a cycle.
        return self.head is not None

    def detectCycle(self):
        return self.head # The racetrack always starts at the starting line.

    def swapPairs(self, head: Optional[Node]) -> Optional[Node]:
        if not head or self.size<2:
            return head

        old_rear = head.prev
        first, second = head, head.next
        next_pair = second.next

        second.next, second.prev = first, old_rear
        first.next, first.prev = next_pair, second
        old_rear.next = second
        if next_pair:
            next_pair.prev = first

        self.head = second
        prev_pair_end = first
        curr = next_pair

        for _ in range((self.size//2 )-1):
            if not curr or not curr.next:
                break

            first, second = curr, curr.next
            next_pair = second.next

            second.next, second.prev = first, prev_pair_end
            first.next, first.prev = next_pair, second
            if next_pair:
                next_pair.prev = first

            prev_pair_end.next = second

            prev_pair_end = first
            curr = next_pair

        # Instead of walking, we use the size to decide the rear
        if self.size%2==0:
            self.rear = prev_pair_end

        else:
            self.rear = prev_pair_end.next

        self.rear.next = self.head
        self.head.prev = self.rear

        return self.head

    def swapPairs_Production_Grade(self):
        if self.size<2:
            return

        dummy = Node(0, self.head, self.rear)
        anchor = dummy

        for _ in range(self.size//2):
            first = anchor.next
            second = first.next
            next_pair = second.next

            first.next = next_pair
            second.next = first
            anchor.next = second

            second.prev = anchor
            first.prev = second
            if next_pair:
                next_pair.prev = first

            anchor = first

        self.head = dummy.next

        self.rear = anchor if self.size%2==0 else anchor.next

        self.rear.next = self.head
        self.head.prev = self.rear

    @staticmethod
    def mergeTwoLists(l1_head, l1_size, l2_head, l2_size):
        if not l1_head: return l2_head, l2_head.prev if l2_head else None, l2_size
        if not l2_head: return l1_head, l1_head.prev if l1_head else None, l1_size

        dummy = Node(0)
        tail = dummy
        c1, c2 = 0, 0

        while c1<l1_size and c2<l2_size:
            if l1_head.data<=l2_head.data:
                chosen = l1_head
                l1_head = l1_head.next
                c1 += 1
            else:
                chosen = l2_head
                l2_head = l2_head.next
                c2 += 1

            tail.next = chosen
            chosen.prev = tail
            tail = tail.next

        for _ in range(l1_size-c1):
            tail.next = l1_head
            l1_head.prev = tail
            l1_head = l1_head.next
            tail = tail.next

        for _ in range(l2_size-c2):
            tail.next = l2_head
            l2_head.prev = tail
            l2_head = l2_head.next
            tail = tail.next

        new_head = dummy.next
        new_head.prev = tail
        tail.next = new_head

        return new_head, tail, (l1_size+l2_size)

    def merge_with(self, other_list):
        if not other_list:
            return

        # If user only sends other_list.head as argument change other_list.rear to other_list.prev and use loop to find size
        if not self.head:
            self.head, self.rear, self.size = other_list.head, other_list.rear, other_list.size
            return

        self.head, self.rear, self.size = self.mergeTwoLists(
            self.head, self.size, other_list.head, other_list.size
        )

    def shuffle(self):
        if self.size<2:
            return

        data_pool = []
        itr = self.head
        for _ in range(self.size):
            data_pool.append(itr.data)
            itr = itr.next

        random.shuffle(data_pool)

        itr = self.head
        for data in data_pool:
            itr.data = data
            itr = itr.next

    def shuffle_nodes(self):
        if self.size<2:
            return

        for _ in range(self.size):
            target_idx = random.randint(0, self.size-1)
            data = self._get_node_at(target_idx).data

            self.remove_at(target_idx)

            self.insert_at_beginning(data)
