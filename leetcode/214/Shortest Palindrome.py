# TLE - brute force, two pointers
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        def is_pali(s, l, r):

            while l <= r:

                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1

            return True

        for r in reversed(range(len(s))):

            if is_pali(s, 0, r):
                suffix = s[r + 1:]
                return suffix[::-1] + s

        return

# solution - Robin Karp solution
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        prefix = 0
        suffix = 0
        base = 29
        last_index = 0 # -1
        power = 1
        mod = 10**9 + 7

        for i,c in enumerate(s):
            char = (ord(c)-ord('a') + 1)

            prefix = (prefix * base) % mod
            prefix = (prefix + char) % mod
            suffix = (suffix + char * power) % mod
            power = (power * base) % mod

            if prefix == suffix:
                last_index = i

        suffix = s[last_index+1:]

        return suffix[::-1] + s

# solution 2 - recursion solution
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        if not s or len(s) == 1:
            return s

        n = len(s)
        i = 0
        for j in range(n):
            if s[i] == s[n - j - 1]:
                i += 1

            if i == n:
                return s

        p = s[i:n][::-1]

        return p + self.shortestPalindrome(s[:i]) + s[i:]
