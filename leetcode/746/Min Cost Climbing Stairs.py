# bottom-up dp time : O(n) , space : O(n)

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        n = len(cost)
        dp = [0] * n
        # [0,0,0,0,0,0,0,0,0,0,0]

        # prev2 = cost[0]
        # prev1 = cost[1]
        

        for i in range(n):

            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        
        # print(dp)

        return min(dp[n-1],dp[n-2])

# Fine Tuning - time : O(n) , space : O(1)

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        
        n = len(cost)

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2,n):
            temp = cost[i] + min(prev1,prev2)
            prev2 = prev1
            prev1 = temp   
        
        return min(prev1,prev2)
    

