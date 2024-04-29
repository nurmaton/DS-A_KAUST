def Intersection(A, B):
    """// Implements brute force algorithm in order to find the intersection of two sets $A[0..n - 1]$ and $B[0..n - 1]$
       // Input: Numbers of the sets that are stored in the arrays $A[0..n-1]$ and $B[0..n - 1]$
       // Additional information: Use of Sort() function which is implemented using mergesort.
       // Output: Array $C[0 \ldots m - 1]$ with $m \leq n$ which is the cardinality of set of $C = A\cap B$"""
       
    Sort(A)
    Sort(B)
    
    C = []
    pointerA = 0
    pointerB = 0

    while pointerA < len(A) and pointerB < len(B):
        if A[pointerA] == B[pointerB]:
            C.append(A[pointerA])
            pointerA += 1
            pointerB += 1
        elif A[pointerA] < B[pointerB]:
            pointerA += 1
        else:
            pointerB += 1

    return C

def Sort(A):
    """Soring procedure using Mergesort algorithm"""
    # First dividing A into a left half L and a right half R
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

        # Conquering L and R by solving them recursively
        Sort(L)
        Sort(R)

        # Combining solutions of L and R
        Merge(A, L, R)

    return A

def Merge(A, L, R):
    """Merging procedure for the Mergesort algorithm"""
    i = j = k = 0
    # Copying data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1



def main():
    # Example
    A = [5, 1, 4, 2, 2]
    B = [8, 4, 3, 2]
    print("The intersection is:", Intersection(A, B))
    
if __name__ == "__main__":
    main()