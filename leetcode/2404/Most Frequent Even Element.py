class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = defaultdict(int)

        for n in nums:

            if n % 2 == 0:
                count[n] += 1
        
        if not count:
            return -1
        
        count = sorted(count.items(), key = lambda x:(-x[1],x[0]))

        return count[0][0]
