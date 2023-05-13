class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_sum = 0
        right_sum = 0
        flag = False
        pivot = 0
        
        while pivot < len(nums):    # pivot from zero to the end

            left_sum = sum(nums[:pivot])    # Sum of elements to the left relative to the pivot
            right_sum = sum(nums[pivot+1:]) # Sum of elements to the right relative to the pivot
   
            if left_sum == right_sum :    # if both variable is the same,
                flag = True
                break
            
            pivot += 1

        if flag == False:           # if it wasn't renewd, set pivot to -1
            pivot = -1             

        return pivot
