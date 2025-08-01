# solution 1 - (two pointers) - (930ms) - (2025.06.24)
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        ans = set()
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):
                if abs(i-j) <= k and nums[j] == key:
                   ans.add(i)

        return list(ans)

# solution 2 - (optimization,index) - (3ms) - (2025.06.24)
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        res = []
        r = 0
        n = len(nums)

        for j in range(n):
            if nums[j] == key:
                l = max(r, j - k)
                r = min(n - 1, j + k) + 1
                for i in range(l, r):
                    res.append(i)

        return res