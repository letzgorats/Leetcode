class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        
        # sliding window

        count = {0:1}
        curr_sum = 0
        answer = 0

        for num in nums:

            curr_sum += num
            if curr_sum - goal in count:
                answer += count[curr_sum - goal]
            count[curr_sum] = count.get(curr_sum,0) + 1
        
        # print(count)
        
        return answer

        



        # answer = 0
        # i = 0
        # while i < len(nums):
            
        #     candi = 0

        #     for j in range(i,len(nums)):

        #         candi += nums[j]
        #         if candi == goal:
        #             answer += 1
        #         elif candi > goal:
        #             break

        #     i += 1
        
        # return answer
