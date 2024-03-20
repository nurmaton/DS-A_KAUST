def Ring(Adj_Matrix):
    """/* Input: symmetric matrix $A[0..n-1, 0..n-1]$, $n > 3$ of zeros and ones representing the adjacency matrix of an undirected graph modeling a network. 
       outputMessage: message to be returned saying whether the network is a ring or not.
       counter: counts the number of 1 in the row which is under consideration
       Output: message saying whether the network is a ring or not. */"""
       
    n = len(Adj_Matrix)
    outputMessage = "The network is not a ring"
    
    for i in range(n):
        counter = sum(Adj_Matrix[i])
        if counter != 2:
            return outputMessage
        
    outputMessage = "The network is a ring"
        
    return outputMessage

def main():
    matrix1 = [
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],  
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0]
    ]
    
    matrix2 = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],  
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0]
    ]
    
    print(f"Matrix 1: {Ring(matrix1)}\nMatrix 2: {Ring(matrix2)}")
if __name__ == "__main__":
    main()