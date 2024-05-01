def Build_Min_Heap(A):
    """//Converts an arbitrary array into a min-heap. 
       //Additional Information: The function works by applying the Min-Heapify procedure to each non-leaf node in reverse level order, starting from the last parent node down to the root.
       //Inputs: A - An array of elements that will be rearranged into a min-heap.
       //Output: Array A is modified to represent a min-heap."""
       
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        Min_Heapify(A, i)

def Min_Heapify(A, i):
    """//Inputs: A - Array representing the heap, i - index of the node to apply Min-Heapify.
       //Output: Subtree rooted at index i is adjusted to satisfy the min-heap property."""
       
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    
    if left < len(A) and A[left] < A[smallest]:
        smallest = left
    if right < len(A) and A[right] < A[smallest]:
        smallest = right
        
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        Min_Heapify(A, smallest)


def main():
    # Example
    ArrayX = [3, 25, 17, 5, 10, 14, 2, 7, 21, 6, 18, 12]
    Build_Min_Heap(ArrayX)
    print(ArrayX)
    
if __name__ == "__main__":
    main()

