# recent solution
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        c_nums = Counter(nums)
        maxV ,res = 0, 0

        for k,v in c_nums.items():

            if max(maxV,v) == v:
                res = k
                maxV = v

        return res


# previous solution 
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dicts = defaultdict(int)

        for n in nums:
            dicts[n] += 1

        dicts = sorted(dicts.items(), key = lambda x : x[1],reverse = True)

        return dicts[0][0]
