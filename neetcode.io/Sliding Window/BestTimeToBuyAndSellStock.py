# Leetcode question 121 - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Time - O(n), where n is len(prices) | Space - O(1)
def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    minPrice = float("inf")
    maxProfit = 0
    
    for currPrice in prices:
        minPrice = min(minPrice, currPrice)
        currProfit = currPrice - minPrice
        maxProfit = max(maxProfit, currProfit)
    
    return maxProfit