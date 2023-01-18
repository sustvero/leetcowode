class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy: always look for a new min price
        min_price = prices[0]
        max_profit = 0

        # iterate through array
        for i in range(1, len(prices)):
            # update minimum price if needed
            if prices[i] < min_price:
                min_price = prices[i]
            # update max profit if needed
            elif (prices[i] - min_price) > max_profit:
                max_profit = prices[i] - min_price
        
        return max_profit