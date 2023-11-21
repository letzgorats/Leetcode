class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        rev_nums = []

        for n in nums:

            rev_nums.append(int(str(n)[::-1]))
        
        # print(rev_nums)
        diff = []

        for i in range(len(nums)):
            a = nums[i] - rev_nums[i]
            diff.append(a)
        
        # print(diff)
        
        frq_count = Counter(diff)
        # print(frq_count)
        count = list(frq_count.values())
        total = 0

        for c in count:
            # Number of cases where two different elements are selected
            total += (c*(c-1)) //2
        
        return total % mod
  
