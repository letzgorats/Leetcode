class Solution:
    def nearestPalindromic(self, n: str) -> str:

        if 1 <= int(n) <= 10:
            return str(int(n) - 1)

        string_len = len(n)
        # if int(n) % (10 ** (string_len-1)) == 0:
        #     return str(int(n)-1)

        # generating potential closet palindromes
        candidates = set()

        prefix = n[:(string_len + 1) // 2]
        for diff in [-1, 0, 1]:
            new_prefix = str(int(prefix) + diff)
            if string_len % 2 == 0:
                palindrome = new_prefix + new_prefix[::-1]
            else:
                palindrome = new_prefix + new_prefix[:-1][::-1]

            candidates.add(int(palindrome))

        candidates.add(10 ** (string_len - 1) - 1) # (ex) 99 for n = 100
        candidates.add(10 ** string_len + 1) # (ex) 1001 for n = 999

        # remove the original one
        candidates.discard(int(n))
        # print(candidates)
        # ca = sorted(candidates, key=lambda x: (abs(x - int(n)), x))
        # print(ca)
        # closest = ca[0]
        closest = min(candidates, key=lambda x: (abs(x - int(n)), x))

        return str(closest)
