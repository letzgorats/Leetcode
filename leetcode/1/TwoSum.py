# first solution
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


# second solution
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict = defaultdict(list)
        for idx, num in enumerate(nums):
            nums_dict[num].append(idx)

        answer = []
        for k, v in nums_dict.items():

            if target - k in nums_dict.keys():

                if target - k == k and len(nums_dict[k]) != 1:
                    return nums_dict[k]
                elif target - k != k:

                    answer.append(nums_dict[k][0])
                    answer.append(nums_dict[target - k][0])
                    break

        return answer
