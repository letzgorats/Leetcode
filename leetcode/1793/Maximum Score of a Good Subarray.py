class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        minVal = answer = nums[k]

        left , right = k, k

        while left > 0 or right < len(nums)-1:

            if left == 0:
                right += 1
         
            elif right == len(nums)-1:
                left -= 1

            elif nums[left-1] > nums[right+1] :
                left -= 1
            
            else:
                right += 1

            minVal = min(minVal,min(nums[left],nums[right]))
            answer = max(answer,minVal * (right-left + 1))

        return answer
