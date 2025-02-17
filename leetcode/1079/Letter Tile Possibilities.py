# solution 1 - Counter, backtracking
from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def backtrack():

            answer = 0
            for c in counts:
                if counts[c] > 0:
                    counts[c] -= 1
                    answer += 1
                    answer += backtrack()
                    counts[c] += 1

            return answer

        counts = Counter(tiles)
        # print(counts)
        return backtrack()

# solution 2 - permutations
import itertools
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        set_t = set()
        for i in range(1, len(tiles) + 1):
            for j in list(itertools.permutations(tiles, i)):
                if j not in set_t:
                    set_t.add(j)
                    # print(set_t)
        return len(set_t)