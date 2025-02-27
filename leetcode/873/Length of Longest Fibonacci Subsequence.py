# solution 1 - brute force, two pointers - (1750ms) - (2025.02.27)
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:

        arr_set = set(arr)
        res = 2

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2
                while nxt in arr_set:
                    length += 1
                    prev, cur = cur, nxt
                    nxt = prev + cur

                res = max(res, length)

        return 0 if res == 2 else res

# solution 2 - dp - (3251ms) - (2025.02.27)
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:

        # number -> index
        arr_map = {n: i for i, n in enumerate(arr)}
        res = 0
        dp = {}  # (i,j) -> length of longest subseq

        # 바텀업 패턴
        # -> i는 배열의 끝에서부터 한 칸 앞부터 시작
        # -> j는 항상 i보다 오른쪽에 있는 원소들을 탐색하는 구조이되, reversed()니까 끝에서부터 i 다음까지
        for i in reversed(range(len(arr) - 1)):
            for j in reversed(range(i + 1, len(arr))):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2
                if nxt in arr_map:
                    length = 1 + dp[(j, arr_map[nxt])]
                    res = max(res, length)

                dp[(i, j)] = length

        return res

# solution 3 - dp - (1139ms) - (2025.02.27)
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:

        # number -> index
        arr_map = {n: i for i, n in enumerate(arr)}
        res = 0
        # (i,j) -> length of longest subseq
        dp = [[0] * len(arr) for _ in range(len(arr))]

        # 바텀업 패턴
        # -> i는 배열의 끝에서부터 한 칸 앞부터 시작
        # -> j는 항상 i보다 오른쪽에 있는 원소들을 탐색하는 구조이되, reversed()니까 끝에서부터 i 다음까지
        for i in reversed(range(len(arr) - 1)):
            for j in reversed(range(i + 1, len(arr))):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2
                if nxt in arr_map:
                    length = 1 + dp[j][arr_map[nxt]]
                    res = max(res, length)

                dp[i][j] = length

        return res