# solution 1 - (dfs,backtracking,cache) - (511ms) - (2025.10.19)
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        n = len(s)
        incremented = {str(n): str((n + a) % 10) for n in range(10)}

        def addOps(s):
            res = ""
            for i in range(n):
                res += s[i] if i % 2 == 0 else incremented[s[i]]
            # print(s)
            return res

        def rotateOps(s):
            return s[n - b:] + s[:n - b]

        seen = set()

        def dfs(s):
            if s in seen:
                return

            seen.add(s)
            dfs(addOps(s))
            dfs(rotateOps(s))

        dfs(s)

        return min(seen)