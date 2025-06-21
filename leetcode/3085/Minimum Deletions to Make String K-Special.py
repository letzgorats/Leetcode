# solution 1 - (hash_table,counting,sort) - (63ms) - (2025.06.21)
from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:

        cnt_table = Counter(word)
        # print(cnt_table)

        res = len(word)

        for a in cnt_table.values():
            deleted = 0
            for b in cnt_table.values():
                if a > b:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a + k)
            res = min(res, deleted)

        return res