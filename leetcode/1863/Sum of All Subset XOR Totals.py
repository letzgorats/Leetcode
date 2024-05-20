from itertools import combinations
class Solution(object):
    def subsetXORSum(self, nums):
      
        def backtracking(index,cur_xor):

            if index == len(nums):
                return cur_xor
            
            # 현재 요소를 포함
            include = backtracking(index+1,cur_xor ^ nums[index])
            
            # 현재 요소를 포함 x
            exclude = backtracking(index+1,cur_xor)

            return include + exclude

        return backtracking(0,0)
        
