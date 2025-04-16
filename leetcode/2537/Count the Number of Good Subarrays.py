# TLE - brute force - (2025.04.16)
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        cnt = 0
        for i in range(len(nums) - 1):
            mpp = {}
            pairs = 0
            for j in range(i, len(nums)):
                pairs += mpp.get(nums[j], 0)
                mpp[nums[j]] = mpp.get(nums[j], 0) + 1
                if pairs >= k:
                    cnt += 1

        return cnt

# solution 1 - sliding window - 121ms - (2025.04.16)
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        mpp = defaultdict(int)
        cnt = left = 0

        for i in range(len(nums)):
            k -= mpp[nums[i]]
            mpp[nums[i]] += 1
            while k <= 0:
                mpp[nums[left]] -= 1
                k += mpp[nums[left]]
                left += 1
            cnt += left

        return cnt