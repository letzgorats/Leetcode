# O(n)
# right - left + 1 개의 새로운 서브어레이가 존재(조합)

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):

        if k <= 1:
            return 0
            
        answer = 0

        i, j = 0, 0
        tmp = 1
        
        for j in range(len(nums)):

            tmp *= nums[j]

            while tmp >= k:
                tmp /= nums[i]
                i += 1
            
            answer += (j-i) + 1

        return answer

            

# TLE
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):

        answer = 0

        i, j = 0, 1
        
        while i < j and j <= len(nums) and i < len(nums):
           
            tmp = 1
            for s in range(i,j):

                tmp *= nums[s]

            if tmp < k and j <= len(nums):
          
                answer += 1
                j += 1
                if j > len(nums):
                    i += 1
                    j = (i+1)
            else:
                i += 1
                j = (i + 1)

        return answer

        
