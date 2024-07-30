# solution 1 - 241ms
class Solution:
    def minimumDeletions(self, s: str) -> int:

        b_count = 0
        res = 0

        for alpha in s:
            if alpha == 'a':
                res = min(res + 1, b_count)
            else:
                b_count += 1

        return res

# <--- a ---- middle(기준) ----- b ----->
# solution 2 - 660ms
class Solution:
    def minimumDeletions(self, s: str) -> int:

        a_count_right = [0] * len(s)

        for i in range(len(s) - 2, -1, -1):

            a_count_right[i] = a_count_right[i + 1]
            if s[i + 1] == 'a':
                a_count_right[i] += 1

        b_count_left = 0
        res = len(s)

        for i, c in enumerate(s):
            res = min(res, b_count_left + a_count_right[i])
            if c == 'b':
                b_count_left += 1

        return res

# solution 2 - 408ms
class Solution:
    def minimumDeletions(self, s: str) -> int:

        a_count_right = s.count('a')

        b_count_left =0
        res = len(s)

        for i,c in enumerate(s):

            if c == 'a':
                a_count_right -= 1
            res = min(res,b_count_left + a_count_right)
            if c == 'b':
                b_count_left += 1

        return res