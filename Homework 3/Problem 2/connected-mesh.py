def ConnectedMesh(Adj_Matrix):
    """/* Input: symmetric matrix $A[0..n-1, 0..n-1]$, $n > 3$ of zeros and ones representing the adjacency matrix of an undirected graph modeling a network. 
       outputMessage: message to be returned saying whether the network is a ring or not.
       counter: counts the number of 1 in the row which is under consideration
       Output: message saying whether the network is a fully connected mesh or not. */"""
       
    n = len(Adj_Matrix)
    outputMessage = "The network is not a connected-mesh"
    
    for i in range(n):
        counter = sum(Adj_Matrix[i])
        if counter != n - 1:
            return outputMessage
        
    outputMessage = "The network is a connected-mesh"
        
    return outputMessage

def main():
    matrix1 = [
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],  
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0]
    ]
    
    matrix2 = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],  
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0]
    ]
    
    print(f"Matrix 1: {ConnectedMesh(matrix1)}\nMatrix 2: {ConnectedMesh(matrix2)}")
if __name__ == "__main__":
    main()