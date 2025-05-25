# solution 1 - (palindrome,hash table) - (203ms) -(2025.05.25)
from collections import defaultdict
from typing import List
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        hash_table = defaultdict(int)
        cnt = 0
        for w in words:
            if w[::-1] in hash_table:
                cnt += len(w) * 2
                hash_table[w[::-1]] -= 1
                if hash_table[w[::-1]] == 0:
                    del hash_table[w[::-1]]
            else:
                hash_table[w] += 1

            # print(hash_table,cnt)

        def is_pelindrome(a):

            l, r = 0, len(a) - 1
            while l < r:
                if a[l] == a[r]:
                    l += 1
                    r -= 1
                else:
                    return False

            return True

        for k, v in hash_table.items():
            if v == 1 and is_pelindrome(k):
                cnt += len(k)
                break
        return cnt