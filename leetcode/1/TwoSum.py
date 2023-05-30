class Solution(object):
    def twoSum(self, nums, target):

        
        sorted_nums = sorted(nums)
        answer = []
        left = 0 
        right = len(nums)-1

        
        while left < right:

            if sorted_nums[left] + sorted_nums[right] > target:
                right -= 1
            elif sorted_nums[left] + sorted_nums[right] < target:
                left += 1
            else:
                answer.append(nums.index(sorted_nums[left]))
                if sorted_nums[left] == sorted_nums[right] :
                    answer.append(nums.index(sorted_nums[right],(nums.index(sorted_nums[left]))+1,len(nums)))
                else:
                    answer.append(nums.index(sorted_nums[right]))

                break
        
        return answer
