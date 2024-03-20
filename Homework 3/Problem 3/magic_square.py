def generatePermutations(ListX):
    """Input: ListX of elements (numbers, letters, etc.)
       Output: List of all permutations"""
    if len(ListX) == 1:
        return [ListX]
    
    permutations = []
    for i in range(len(ListX)):
        # Excluding element List[i] in order to find permutations of the remaining elements
        remaining = ListX[:i] + ListX[i+1:]
        for j in generatePermutations(remaining):
            permutations.append([ListX[i]] + j)
            
    return permutations

def isMagicSquare(SquareX, n, magicConstant):
    """Input: SquareX which is n x n List of Lists of numbers, magicConstant is magic constant, n is n
       Output: True if SquareX is magic and False otherwise"""
    
    # Checking rows and columns
    for i in range(n):
        if sum(SquareX[i]) != magicConstant:
            return False
        if sum(SquareX[j][i] for j in range(n)) != magicConstant:
            return False

    # Checking diagonals
    if sum(SquareX[i][i] for i in range(n)) != magicConstant:
        return False
    if sum(SquareX[i][n-i-1] for i in range(n)) != magicConstant:
        return False

    return True

def generateMagicSquares(n):
    """Input: n
       Output: All possible magic squares of order n"""
    magicConstant = n * (n**2 + 1) // 2
    numbers = list(range(1, n * n + 1))

    for perm in generatePermutations(numbers):
        # Generating a square from the permutation
        SquareX = [perm[i:i+n] for i in range(0, len(perm), n)]
        if isMagicSquare(SquareX, n, magicConstant) is True:
            yield SquareX
            
            
def main():
    # Example for 3x3 magic square
    n = 3
    for SquareX in generateMagicSquares(n):
        for row in SquareX:
            print(row)
        print("\n")
        
if __name__ == "__main__":
    main()