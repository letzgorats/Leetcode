# Counter solution
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cnt = Counter(nums)         
        # print(cnt)

        answer = 0 
        for k,v in cnt.items():

            if v >= 2:
                return k


