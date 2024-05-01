def Min_Heapify(A, i, heap_size):
    """Helper function to ensure the min-heap property is maintained/See Part 1""" 
    
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i

    if left < heap_size and A[left] < A[smallest]:
        smallest = left
    if right < heap_size and A[right] < A[smallest]:
        smallest = right

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        Min_Heapify(A, smallest, heap_size)

def Find_and_Delete_Largest(A):
    """//Finds and removes the largest element in a min-heap. After removing the largest element, the function ensures the min-heap property is restored.
       //Inputs: A - Array representing a min-heap.
       //Output: Modified min-heap array after deleting the largest element."""
       
    n = len(A)
    if n == 0:
        return None  # Returning None if the heap is empty

    # Identifying the range of leaf nodes
    first_leaf_index = n // 2  # First leaf node is the child of the last parent node

    # Finding the largest element among the leaf nodes
    largest_index = first_leaf_index
    for i in range(first_leaf_index, n):
        if A[i] > A[largest_index]:
            largest_index = i

    # Swapping and removing the largest element
    A[largest_index], A[-1] = A[-1], A[largest_index]
    largest_element = A.pop()

    # Restoring the min-heap property if necessary
    if largest_index < len(A):  # Checking if the swapped element was not already the last one
        Min_Heapify(A, largest_index, len(A))

    return largest_element


def main():
    min_heap = [2, 5, 3, 7, 6, 12, 17, 25, 21, 10, 18, 14]
    largest_removed = Find_and_Delete_Largest(min_heap)
    print("Largest Removed:", largest_removed)
    print("Heap after removal:", min_heap)
    
if __name__ == "__main__":
    main()
