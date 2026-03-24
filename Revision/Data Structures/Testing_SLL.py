from Singly_Linked_List_Updated import Singly_Linked_List

def test_singly():
    # 1. The Empty/Single Logic Check
    test_ll = Singly_Linked_List()
    test_ll.insert_at_end(10)
    test_ll.remove_at(0)
    print(f"Size after clear: {test_ll.get_length()}") # Should be 0
    print(f"Rear after clear: {test_ll.rear}")         # Should be None

    # 2. The Reverse-Swap-Merge Combo
    list_a = Singly_Linked_List()
    list_a.extend([10, 30, 50])
    list_b = Singly_Linked_List()
    list_b.extend([20, 40, 60])

    list_a.merge_with(list_b) 
    # Now List A is: 10->20->30->40->50->60
    print(f"Merged Size: {list_a.get_length()}") # Should be 6
    print(f"Merged Rear: {list_a.rear.data}")    # Should be 60

    list_a.reverse_list() 
    # Now: 60->50->40->30->20->10
    print(f"Post-Reverse Rear: {list_a.rear.data}") # Should be 10

    # UPDATED: Calling swapPairs with head argument
    list_a.head = list_a.swapPairs(list_a.head)
    # Now: 50->60->30->40->10->20
    list_a.print_list()
    
    print("\n--- Additional Rear Validation ---")
    print(f"Final Rear Data: {list_a.rear.data}") # Should be 20
    print(f"Rear.next is None: {list_a.rear.next is None}") # Verifies end of list

if __name__ == "__main__":
    test_singly()