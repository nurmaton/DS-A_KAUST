def Star(Adj_Matrix):
    """/* Input: symmetric matrix $A[0..n-1, 0..n-1]$, $n > 3$ of zeros and ones representing the adjacency matrix of an undirected graph modeling a network. 
       isCenter: is True if the network is a star, and False otherwise.
       outputMessage: message to be returned saying whether the network is a star or not.
       counter: counts the number of 1 in the row which is under consideration
       Output: message saying whether the network is a star or not. */"""
       
    n = len(Adj_Matrix)
    isCenter = False
    outputMessage = "The network is not a star"
    
    for i in range(n):
        counter = sum(Adj_Matrix[i])
        if counter == n - 1:
            if isCenter is True:  # Detected more than one center
                return outputMessage
            isCenter = True
        elif counter != 1:
            return outputMessage
            
    if isCenter is True:
        outputMessage = "The network is a star"
        
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
    [0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0],  
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0]
    ]
    
    print(f"Matrix 1: {Star(matrix1)}\nMatrix 2: {Star(matrix2)}")
if __name__ == "__main__":
    main()