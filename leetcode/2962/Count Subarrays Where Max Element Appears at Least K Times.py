class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        max_num = max(nums)

        cnt = Counter(nums)
        if cnt[max_num] < 2:
            return 0

        index = defaultdict(list)
        count = defaultdict(int)

        s_index = 0
        e_index = 0



        while s_index < len(nums):

            count[nums[e_index]] += 1

            while e_index < len(nums) and count[max_num] >= k:

                e_index += 1
                count[nums[e_index]] += 1
            
            e_index += 1
