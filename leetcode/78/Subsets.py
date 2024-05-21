class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        answer = []

        def backtracking(index,cur_list):

            answer.append(cur_list[:])
        
            for i in range(index,len(nums)):

                cur_list.append(nums[i])
                backtracking(i+1,cur_list)
                cur_list.pop()

        backtracking(0,[])

        return answer
            
