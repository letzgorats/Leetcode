# solution 1
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        N = len(nums)

        lis = [1] * N
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], 1 + lis[j])

        lds = [1] * N
        for i in reversed(range(N)):
            for j in range(i + 1, N):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], 1 + lds[j])

        res = N
        for i in range(1, N - 1):
            if lis[i] > 1 and lds[i] > 1:
                res = min(res, N - lis[i] - lds[i] + 1)

        return res

# solution 2
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        n = len(nums)
        if n < 3:  # 리스트의 길이가 3 미만인 경우, mountain array를 만들 수 X
            return 0

        # LIS (longest increasing subsequence) 의 길이를 저장할 dp 배열
        # (왼쪽 -> 오른쪽)
        lis = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        # LDS (longest decreasing subsequence) 의 길이를 저장할 dp 배열
        # (오른쪽 -> 왼쪽)
        lds = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)

        max_mountain_len = 0
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:
                max_mountain_len = max(max_mountain_len, lis[i] + lds[i] - 1)

        return n - max_mountain_len
