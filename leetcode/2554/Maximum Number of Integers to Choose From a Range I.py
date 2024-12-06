# solution 1 - 9897ms
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        cnt = 0
        for i in range(1, n + 1):

            if i not in banned:
                maxSum -= i
                cnt += 1
            if maxSum < 0:
                return cnt - 1

        return cnt

# solution 2 - 35ms
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        cnt = 0
        banned = set(banned)
        for i in range(1, n + 1):

            if i not in banned:
                maxSum -= i
                cnt += 1
            if maxSum < 0:
                return cnt - 1

        return cnt
