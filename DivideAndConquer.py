def MostProfit(P):
    """// Implements algorithm to find out when there is the best time to buy and then the best time to sell the stock in order to make the most profit.
       // Input: Array of stocks' prices P[0..n-1]
       // Additional information: Use of function MostProfitRecursive(l, r) that do the same thing as our function MostProfit()
       // Output: A profit itself with a pair of days such that profit is positive and maximum, or if there is no way to make a profit, the corresponding message."""
    
    def MostProfitRecursive(start, end):
        """// Implements divide and conquer algorithm to find out when there is the best time to buy and then the best time to sell the stock in order to make the most profit.
           // Input: Starting and ending points of the subarray
           // Additional information: Use of standard min, max and index functions for arrays.
           // Output: A profit itself with a pair of days such that profit is positive and maximum, or if there is no way to make a profit, the corresponding message."""
 
        # Base case: only one day, no transaction can be made
        if start == end:
            return 0, (start, end)
        
        # Finding midpoint of the current subarray
        mid = (start + end) // 2
        
        # Finding recursively the maximum profit in the left and right subarrays
        leftProfit, leftDays = MostProfitRecursive(start, mid)
        rightProfit, rightDays = MostProfitRecursive(mid + 1, end)
        
        # Finding the minimum price in the left subarray and the maximum price in the right subarray with their indecies
        minLeftPrice = min(P[start:mid+1])
        maxRightPrice = max(P[mid+1:end+1])
        minLeftDay = P[start:mid+1].index(minLeftPrice) + start
        maxRightDay = P[mid+1:end+1].index(maxRightPrice) + mid + 1
        
        # Finding the crossing profit which is the maximum profit if we buy in the left and sell in the right
        crossProfit = maxRightPrice - minLeftPrice
        crossDays = (minLeftDay, maxRightDay)
        
        # Determining which of the three profits from above has the maximum profit and returning profit with pair of days
        maxProfits = max(leftProfit, crossProfit, rightProfit)
        if leftProfit == maxProfits:
            return leftProfit, leftDays
        elif crossProfit == maxProfits:
            return crossProfit, crossDays
        else:
            return rightProfit, rightDays
            
    maxProfit, (buyDay, sellDay) = MostProfitRecursive(0, len(P) - 1)
    if maxProfit <= 0:
        return "No way to make a profit"
    return maxProfit, (buyDay + 1, sellDay + 1)


def main():
    # Example
    Prices = [1, 1, 1, 1, 10]
    result = MostProfit(Prices)
    if "No way" in result:
        print(result)
    else:
        profit, days = result
        print(f"A pair of days is ({days[0]}, {days[1]}) and the profit is ${profit}")
    
    
if __name__ == "__main__":
    main()