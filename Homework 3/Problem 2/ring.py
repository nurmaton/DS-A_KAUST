import numpy as np
from collections import defaultdict

def Ring(Adj_Matrix):
    """/* Input: symmetric matrix $A[0..n-1, 0..n-1]$, $n > 3$ of zeros and ones representing the adjacency matrix of an undirected graph modeling a network. 
       outputMessage: message to be returned saying whether the network is a ring or not.
       counter: counts the number of 1 in the row which is under consideration.
       adjacencyDictionary: same as adjacency list of nodes, but presented using dictionary (a collection of key-value pairs, which is changeable and do not allow duplicates).
       colored: list that stores information about nodes to be discovered or not in the process of DFS.
       all(colored): function that checks if every element in the list "colored" is True or not.
       Output: message saying whether the network is a ring or not. */"""
    
    # Part 1
    n = len(Adj_Matrix)
    outputMessage = "The network is not a ring"
    
    # Initializing adjacency dictionary
    adjacencyDictionary = defaultdict(list)
    
    # Filling adjacency dictionary and checking every node to have exactly two connections
    for i in range(n):
        for j in range(n):
            if Adj_Matrix[i, j] == 1:
                adjacencyDictionary[i].append(j)
        counter = len(adjacencyDictionary[i])
        if counter != 2:
            return outputMessage 
        
    # Part 2
    # Checking connectivity by performing DFS
    # Coloring all the nodes to False (White)
    colored = [False] * n
    
    # Creating function for DFS traversal from a given node
    def dfs(u):
        colored[u] = True
        for v in adjacencyDictionary[u]:
            if not colored[v]:
                dfs(v)
                
    # Performing DFS from the first node
    dfs(0)

    # Checking if all nodes were discovered (colored)
    if all(colored) is True:
        outputMessage = "The network is a ring"
        
    return outputMessage

def main():
    # Two rings
    matrix1 = np.array([
        [0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0]
    ])
    # Ring
    matrix2 = np.array([
        [0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0]
    ])
    # Not ring
    matrix3 = np.array([
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 0]
    ])

    print(f"Matrix 1: {Ring(matrix1)}\nMatrix 2: {Ring(matrix2)}\nMatrix 3: {Ring(matrix3)}")
    
if __name__ == "__main__":
    main()
