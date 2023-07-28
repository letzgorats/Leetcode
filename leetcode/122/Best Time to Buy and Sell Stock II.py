# solution direction
# If the next day is a higher point, I don't sell it, 
# but if it is a lower point the next day, I applied the principle of selling it today.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minVal = max(prices)    # set the minVal
        profit = 0              # current_profit
        total = 0

        for idx,p in enumerate(prices):

            minVal = min(p,minVal)

            print(idx,p)
            if idx == len(prices)-1 and minVal != 10001:    # the last day, we must sell
                total += (p - minVal)
                break

            if (p-minVal) > profit: # renew
                if prices[idx+1] < p :
                    total += (p-minVal)
                    minVal = 10001      # set minVal to initial value
                    profit = 0          # set profit to initial value


        return total



# someone's code - more simple (same principle)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit





  
