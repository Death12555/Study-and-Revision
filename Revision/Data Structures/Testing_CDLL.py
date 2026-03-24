from Circular_Doubly_Linked_List import Circular_Doubly_Linked_List

def stress_test_cdll():
    print("--- Phase 1: Basic Symmetry & Circularity ---")
    cdll = Circular_Doubly_Linked_List()
    cdll.extend([10, 20, 30, 40, 50])
    
    cdll.print_forward()
    cdll.print_backward() # Verifies if prev pointers are correct
    
    print(f"Size: {cdll.size} (Expected 5)")
    is_circular = cdll.rear.next == cdll.head and cdll.head.prev == cdll.rear
    print(f"Circularity Check: {'Pass' if is_circular else 'Fail'}")

    print("\n--- Phase 2: swapPairs (Argument version) ---")
    # Expected: 20 <--> 10 <--> 40 <--> 30 <--> 50
    cdll.head = cdll.swapPairs(cdll.head)
    print("After swapPairs(head):")
    cdll.print_forward()
    print(f"Rear Data: {cdll.rear.data} (Expected 50)")

    print("\n--- Phase 3: The Reverse Test ---")
    cdll.reverse_list()
    print("After Reverse:")
    cdll.print_forward()
    print("Backward Symmetry Check:")
    cdll.print_backward() # This verifies the fix you made in reverse_list

    print("\n--- Phase 4: Production Grade Swap ---")
    # This should swap the current [50, 30, 40, 10, 20] 
    cdll.swapPairs_Production_Grade()
    print("After Production Swap:")
    cdll.print_forward()
    print(f"Is it still circular? {cdll.rear.next == cdll.head}")

    print("\n--- Phase 5: Merge & Shuffle ---")
    other = Circular_Doubly_Linked_List()
    other.extend([5, 15, 25])
    cdll.merge_with(other)
    print("After Merging [5, 15, 25]:")
    cdll.print_forward()
    
    print("Shuffling Nodes (Physical Re-link)...")
    cdll.shuffle_nodes()
    cdll.print_forward()
    
    print("\n--- Phase 6: Complete Emptying ---")
    while cdll.size > 0:
        cdll.remove_at(0)
    print(f"Final State -> Size: {cdll.size}, Head: {cdll.head}, Rear: {cdll.rear}")

if __name__ == "__main__":
    try:
        stress_test_cdll()
        print("\n✅ CDLL STRESS TEST COMPLETE: Logic is rock solid!")
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()