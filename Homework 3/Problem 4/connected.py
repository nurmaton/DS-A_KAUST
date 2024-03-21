import numpy as np
import networkx as nx

def Connected(Adj_Matrix):
    """/* Input: Adjacency matrix $A[0..n-1][0..n-1]$ of an undirected graph G
          Output: True if G is connected and False if it is not */"""
       
    n = len(Adj_Matrix)
    if n == 1:
        return True
    
    if not Connected(Adj_Matrix[:-1, :-1]):
        return False
    
    for j in range(n-1):
        if Adj_Matrix[n-1, j] == 1:
            return True    
        
    return 0

def main():
    # An adjacency matrix is a square, binary matrix.
    matrix = np.array([
    [0, 1, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 0],  
    [0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0]
    ])
    
    print(f"Result of the function Connected: {Connected(matrix)}")
    G = nx.from_numpy_array(matrix)
    print(f"Result by using networkx package: {nx.is_connected(G)}")
    
if __name__ == "__main__":
    main()