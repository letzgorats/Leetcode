from collections import deque
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        
        res = 0

        jmin = jmax = jbad = -1

        for idx, num in enumerate(nums):
            if not minK <= num <= maxK:
                jbad = idx
            
            if num == minK :
                jmin = idx
            if num == maxK :
                jmax = idx
            
            res += max(0, min(jmin,jmax)-jbad)
            # print("jmin=",jmin)
            # print("jmax=",jmax)
            # print("jbad=",jbad)
            # print(res)
        
        return res

 
            



        

 
            



        
