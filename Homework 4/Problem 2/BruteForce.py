def Intersection(A, B):
    """// Implements brute force algorithm in order to find the intersection of two sets $A[0..n - 1]$ and $B[0..n - 1]$
       // Input: Numbers of the sets that are stored in the arrays $A[0..n-1]$ and $B[0..n - 1]$
       // Output: Array $C[0 \ldots m - 1]$ with $m \leq n$ which is the cardinality of set of $C = A\cap B$"""
       
    C = []
    for a in A:
        for b in B:
            if a == b:
                C.append(a)
    return C


def main():
    # Example
    A = [1, 3, 4, 6, 7]
    B = [2, 3, 5, 7]
    print("The intersection is:", Intersection(set(A), set(B)))
 
if __name__ == "__main__":
    main()