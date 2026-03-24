from Circular_Singly_Linked_List import Circular_Singly_Linked_List

def stress_test():
    cll = Circular_Singly_Linked_List()
    cll.extend([10, 30, 50])
    cll2 = Circular_Singly_Linked_List()
    cll2.extend([20, 40, 60])
    
    print("--- Phase 1: Merge ---")
    cll.merge_with(cll2)
    cll.print_list() 
    
    print("\n--- Phase 2: Swap Pairs ---")
    # Testing Production Grade
    cll.swapPairs_Production_Grade()
    print("Production Swap: ", end="")
    cll.print_list()
    
    # NEW: Testing updated swapPairs(head)
    cll.head = cll.swapPairs(cll.head)
    print("Argument Swap:   ", end="")
    cll.print_list() 
    
    print("\n--- Phase 3: Reverse ---")
    cll.reverse_list()
    cll.print_list() 
    
    print("\n--- Phase 4: Verification ---")
    print(f"Size: {cll.size} (Expected 6)")
    # Critical check for circularity after the argument-based swap
    print(f"Rear points to Head: {cll.rear.next == cll.head}")
    print(f"Rear Data: {cll.rear.data}")

if __name__ == "__main__":
    stress_test()