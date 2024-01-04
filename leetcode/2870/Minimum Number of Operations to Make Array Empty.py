# TLE solution

class Solution(object):
    def minOperations(self, nums):

        answer = 0

        command_case = [2,3]
        nums_set = list(set(nums))

        max_cnt = 0
        for i in nums_set:
            max_cnt = max(max_cnt,nums.count(i))

        max_val = float('inf')

        dp = [max_val] * (max_cnt+1)
        dp[0] = 0
      
        for i in range(2):
            for j in range(command_case[i],max_cnt+1):
                dp[j] = min(dp[j],dp[j-command_case[i]] + 1)
        # print(dp)
        
        for n in nums_set:
            cnt = nums.count(n)
            if dp[cnt] == max_val:
                return -1
            else:
                answer += dp[cnt]

        return answer


# 1 -> 0
# 2 -> 1
# 3 -> 1
------
# 4 -> 2
# 5 -> 2
# 6 -> 2
------
# 7 -> 3
# 8 -> 3
# 9 -> 3
------
# 10 -> 4
# 11 -> 4
# 12 -> 4
------
# 13 -> 5
# 14 -> 5
# 15 -> 5
------
# 16 -> 6
# 17 -> 6
# 18 -> 6
------
# 19 -> 7
# 20 -> 7
# 21 -> 7
------
# 22 -> 8
# ...

# Finding out the reules...from 4 -> The increasing value is continuously repeated three times.

# solution

class Solution(object):
    def minOperations(self, nums):

        if len(nums) == 2:
            if nums[0] != nums[1]:
                return -1
            else:
                return 1

        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        
        answer = 0
        for count in counts.values():

            if count == 1:
                return -1
            if count % 3 == 0:
                answer += (count // 3) 
            else:
                answer += (count // 3) + 1

    return answer 


