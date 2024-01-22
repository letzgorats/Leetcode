class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums_set = list(set(nums))
        real = 0
        duplicated = 0
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
            if count[i] == 2:
                duplicated = i
                break

        for i in range(1,len(nums)+1):
            if i not in nums_set:
                real = i
                break
        
        return [duplicated,real]

# clever sol

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        a = sum(set(nums))
        b = sum(nums)
        s = n*(n+1) // 2
        
        return [b-a,s-a]


        
