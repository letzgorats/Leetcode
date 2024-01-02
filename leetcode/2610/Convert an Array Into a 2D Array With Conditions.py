class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        
        row = list(set(nums))

        while len(nums) != len(row):
            
            answer.append(row)
            
            for i in row:
                nums.remove(i)
             
            row = list(set(nums))
  
        answer.append(row)

        return answer
                  
            
        
