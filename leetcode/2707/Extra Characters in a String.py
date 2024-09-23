# solution 1 - memoization
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        wordSet = set(dictionary)
        dp = {len(s): 0}

        def dfs(i):

            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)  # skip curr char

            for j in range(i, len(s)):
                if s[i:j + 1] in wordSet:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res

        return dfs(0)

# solution - prefix tree, trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        dp = {len(s): 0}
        trie = Trie(dictionary).root

        def dfs(i):

            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)  # skip curr char
            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.word:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res

        return dfs(0)

# solution 3 - dp
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        wordSet = set(dictionary)
        dp = [0] * (len(s) + 1)

        for i in range(len(s) - 1, -1, -1):
            dp[i] = dp[i + 1] + 1

            for length in range(1, len(s) - i + 1):
                if s[i:i + length] in wordSet:
                    dp[i] = min(dp[i], dp[i + length])

        return dp[0]