from itertools import combinations


# 길이 2인 subsequence 도 포함해서 다 더해주고 마지막 길이가 2인 subsequence 경우 빼주는 solution
class Solution(object):
    def numberOfArithmeticSlices(self, nums):

        
        res, n = 0, len(nums)

        dp = [defaultdict(int) for _ in range(n)]

        # dp[i][diff] => #(num) of subseq ending at i, with diff

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += (1 + dp[j][diff])
                res += (dp[j][diff] + 1)
 
        return res - (n *(n-1) // 2)

# res에 길이가 2인 subsequence 는 더해주지 않고 길이가 3 이상인 경우만 subsequence 만 더해주는 경우 - 이전 값이 있는 경우(값 영향을 받는 지점)에서 이전값을 더해주면 되는 셈.

class Solution(object):
    def numberOfArithmeticSlices(self, nums):

        
        res, n = 0, len(nums)

        dp = [defaultdict(int) for _ in range(n)]

        # dp[i][diff] => #(num) of subseq ending at i, with diff

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += (1 + dp[j][diff])
                res += (dp[j][diff])
 
        return res 

        # res = (0) + (0 + 1) + (0 + 0 + 0) + (0 + 0 + 0 + 1) 
        #     + (0 + 0 + 0 + 1 + 1)

        #  [2,3,4,10,16,22]
        #  "diff"   1 2 6 7 8 12 13 14 18 19 20  
        #  i     0| 0
        #        1| 1       
        #        2| 2 1
        #        3|     1 1 1
        #        4|     2      1  1  1 
        #        5|     3      1        1  1  1


        # [defaultdict(<type 'int'>, {8: 0, 1: 0, 2: 0, 20: 0, 14: 0}), 
        # defaultdict(<type 'int'>, {1: 1, 19: 0, 13: 0, 7: 0}), 
        # defaultdict(<type 'int'>, {1: 2, 2: 1, 12: 0, 18: 0, 6: 0}),
        # defaultdict(<type 'int'>, {8: 1, 12: 0, 6: 1, 7: 1}), 
        # defaultdict(<type 'int'>, {6: 2, 12: 1, 13: 1, 14: 1}), 
        # defaultdict(<type 'int'>, {12: 1, 18: 1, 19: 1, 20: 1, 6: 3})]

        # res - (n *(n-1) // 2)



# Q. 왜 i가 5일 때, res에 (dp[j][diff]) 부분을 더하는 부분에서 0,0,0,1,2 가 더해지는 것이 아니라 0,0,0,0,2 가 더해지는지 모르겠어.
# 앞전에 순회한 것을 직접 그려보면서 계산해봤는데, dp[4][12] 가 1이니까 dp[5][12] 가 2가 되면서 res 에는 1이 더해져야 하는 것이 아니야?

# -> j = 3: diff = nums[5] - nums[3] = 22 - 10 = 12. 이 경우 dp[3][12]는 이전에 설정되지 않았으므로 res에는 0이 더해진다. 무조건 이전 값이 아니라 j의 위치 잘 확인!



