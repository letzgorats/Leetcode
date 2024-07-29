# solution 1 - math, brute force, O(n^2) - 356ms
class Solution:
    def numTeams(self, rating: List[int]) -> int:

        res = 0

        # m -> middle point
        for m in range(1, len(rating) - 1):

            # asecending
            left_smaller = right_larger = 0

            for i in range(m):
                if rating[i] < rating[m]:
                    left_smaller += 1

            for i in range(m + 1, len(rating)):
                if rating[m] < rating[i]:
                    right_larger += 1

            res += (left_smaller * right_larger)

            # descending

            left_larger = m - left_smaller
            right_smaller = len(rating) - m - 1 - right_larger

            res += (left_larger * right_smaller)

        return res

# solution 2 - decision tree,backtracking,cache,memoization O(n^2) - 2110ms
class Solution:
    def numTeams(self, rating: List[int]) -> int:

        cache = {}

        def backtrack(i, ascend, count):

            if (i, ascend, count) in cache:
                return cache[(i, ascend, count)]
            if count == 3:
                return 1
            if i == len(rating):
                return 0

            res = 0
            for j in range(i + 1, len(rating)):
                if ascend and rating[i] < rating[j]:
                    res += backtrack(j, ascend, count + 1)
                if not ascend and rating[i] > rating[j]:
                    res += backtrack(j, ascend, count + 1)
            cache[(i, ascend, count)] = res
            return res

        res = 0
        for i in range(len(rating)):
            res += backtrack(i, True, 1)
            res += backtrack(i, False, 1)

        return res

# solution 3 - dp - 1016ms
class Solution:
    def numTeams(self, rating: List[int]) -> int:

        length = len(rating)
        ascend = [[0] * 4 for _ in range(length)]
        descend = [[0] * 4 for _ in range(length)]

        for i in range(length):
            ascend[i][1] = 1
            descend[i][1] = 1

        for count in range(2, 4):
            for i in range(length):
                for j in range(i + 1, length):
                    if rating[i] < rating[j]:
                        ascend[i][count] += ascend[j][count - 1]
                    if rating[i] > rating[j]:
                        descend[i][count] += descend[j][count - 1]
        res = 0
        for i in range(length):
            res += ascend[i][3] + descend[i][3]

        return res




