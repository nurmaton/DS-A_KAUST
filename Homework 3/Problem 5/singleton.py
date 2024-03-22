def FindSingleton(ListX):
    global initialListX
        
    n = len(ListX)
    k = (n - 1) // 2
    
    # Singleton not found
    if n == 0:
        return None, None
    
    # If we're looking at a single element, we've found the singleton
    if n == 1:
        return initialListX.index(ListX[0]), ListX[0]
    
    else:
        if ListX[2 * (k // 2)] == ListX[2 * (k // 2) + 1]:
            return FindSingleton(ListX[2 * (k // 2) + 2 : ])
        else:
            return FindSingleton(ListX[0 : 2 * (k // 2) + 1])
    
def main():
    global initialListX
    # Examples
    A = [2, 2, 5, 5, 9, 9, 13, 16, 16, 18, 18, 23, 23, 30, 30]
    B = [1, 1, 6, 6, 8, 8, 9, 9, 14, 14, 17]
    C = [3, 8, 8, 11, 11, 21, 21, 25, 25, 36, 36]
    D = [4, 4, 7, 9, 9]
    for el in [A, B, C, D]:
        initialListX = el.copy()
        print(f"The index of the singleton in {el} is {FindSingleton(el)[0]} and its value is {FindSingleton(el)[1]}\n")
        
if __name__ == "__main__":
    main()