class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        fewestCoins=[amount + 1] * (amount + 1)

        # iterate through coins, each time we only want to add 1 coin
        # each time, we choose what coin to add
        # test all coins

        # edge cases:
        if amount == 0:
            return 0

        for i in range(1, amount + 1): 
            fewestCoins[i] = amount + 1 # most coins possible is amount
            for coin in coins:
                
                if i - coin == 0:
                    fewestCoins[i] = 1
                elif i - coin > 0:
                    if fewestCoins[i - coin] <= (i - coin) and (fewestCoins[i - coin] + 1) < fewestCoins[i]:
                        fewestCoins[i] = fewestCoins[i - coin] + 1
        
        print(fewestCoins)
        if (fewestCoins[amount] > amount):
            return -1
        else:
            return fewestCoins[amount]

# this solution has time complexity O(n * c), where n is the amount and c is the number of types of coins