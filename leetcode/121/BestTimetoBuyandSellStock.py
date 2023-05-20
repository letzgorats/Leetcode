class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # is_reversed_sorted = all(prices[i] >= prices[i+1] for i in range(len(prices)-1))
        # print(is_reversed_sorted)
        # if is_reversed_sorted:
        #     return 0

        # i = 0
        # profit = -10001

        # while i < len(prices)-1 :
        #     for j in range(i+1,len(prices)):
        #         if prices[i] < prices[j] :
        #             profit = max(profit,prices[j] - prices[i])
        #     i += 1

        
        # # # print(profit)
        # return profit    

        minVal = max(prices)
        maxProfit = 0

        for p in prices:
            minVal = min(minVal,p)
            maxProfit = max(maxProfit,p-minVal)
        return maxProfit
