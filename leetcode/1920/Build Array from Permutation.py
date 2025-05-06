# solution 1 - (array) - (3ms) - (2025.05.06)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans

# solution2 - (1-code) - (0ms) - (2025.05.06)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[x] for x in nums]

# solution3 - follow up, extra space : O(1) - (0ms) - (2025.05.06)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        for i in range(n):
            nums[i] += 1000 * (nums[nums[i]] % 1000)
            # print(nums)

        for i in range(n):
            nums[i] //= 1000

        # print(nums)

        return nums