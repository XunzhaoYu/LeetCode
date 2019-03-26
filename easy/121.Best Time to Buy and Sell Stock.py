"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                 Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


def maxProfit(prices):  # system error, test running time in the future.
    """
    :type prices: List[int]
    :rtype: int
    """
    days = len(prices)
    if days < 2:
        return 0
    buy, sell = prices[0:2]
    max_profit = max(sell - buy, 0)
    for i in range(1, days):
        if prices[i] < buy:
            max_profit = max(max_profit, sell - buy)
            buy = sell = prices[i]
        elif prices[i] > sell:
            sell = prices[i]
    return max(max_profit, sell - buy)


def maxProfit2(prices):
    if len(prices)<2:
        return 0
    lowest = prices[0]
    rst = 0
    for price in prices:
        if price<lowest:
            lowest = price
        rst = max(rst, price-lowest)
    return rst
