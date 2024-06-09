class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        
        mod_and_count = {0:1}
        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]
            mod = prefix % k
            if mod < 0 :  # 음수 나머지를 양수로 바꿈
                mod += k

            if mod not in mod_and_count :
                mod_and_count[mod] = 1
            else:
                count += mod_and_count[mod]
                mod_and_count[mod] += 1

        return count
