# solution 1
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        res = bin(start ^ goal)
        cnt = 0
        for i in res[2:]:
            if i == '1':
                cnt += 1

        return cnt

# solution 2
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        res = bin(start ^ goal)

        return res.count('1')