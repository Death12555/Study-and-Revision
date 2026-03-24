from Doubly_Linked_List import Doubly_Linked_List

def test_dll():
    dll = Doubly_Linked_List()
    
    print("--- Phase 1: Basic Insertion & Symmetry ---")
    dll.extend([10, 20, 30, 40, 50])
    dll.print_forward()
    dll.print_backward() 

    print("\n--- Phase 2: Middle Operations ---")
    dll.insert_at_updated(2, 25) 
    dll.remove_at(4)            
    dll.print_forward()
    dll.print_backward()
    
    print("\n--- Phase 3: The Swap & Reverse ---")
    # Original Production Grade Test (Keeping as requested)
    dll.swapPairs_Production_Grade()
    print("After Production Swap: ", end="")
    dll.print_forward()
    
    # NEW: Testing the updated swapPairs(head) method
    print("After Argument-based Swap: ", end="")
    dll.head = dll.swapPairs(dll.head)
    dll.print_forward()
    
    dll.reverse_list()
    print("After Reverse: ", end="")
    dll.print_forward()
    
    print("\n--- Phase 4: The Edge Cases ---")
    dll.insert_at_end(60)
    dll.swapPairs_Production_Grade()
    dll.print_forward()
    
    print("\nEmptying list...")
    while dll.size > 0:
        dll.remove_at(0)
    
    print(f"Final Results -> Size: {dll.size}, Head: {dll.head}, Rear: {dll.rear}")

if __name__ == "__main__":
    test_dll()