def MostProfit(P):
    """// Implements brute force algorithm to find out when there is the best time to buy and then the best time to sell the stock in order to make the most profit.
       // Input: Array of stocks' prices P[0..n-1]
       // Output: A profit itself with a pair of days such that profit is positive and maximum, or if there is no way to make a profit, the corresponding message."""
    
    n = len(P)
    maxProfit = 0
    buyDay = 0
    sellDay = 0

    for i in range(n-1):
        for j in range(i+1, n):
            if P[j] - P[i] > maxProfit:
                maxProfit = P[j] - P[i]
                buyDay = i
                sellDay = j

    if maxProfit <= 0:
        return "No way to make a profit"
    else:
        return maxProfit, (buyDay + 1, sellDay + 1)


def main():
    # Example
    Prices = [1, 1, 0, 0, 10]
    result = MostProfit(Prices)
    if "No way" in result:
        print(result)
    else:
        profit, days = result
        print(f"A pair of days is ({days[0]}, {days[1]}) and the profit is ${profit}")
 
if __name__ == "__main__":
    main()