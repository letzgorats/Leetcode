# solutino 1 - (dfs,memoization) - (4090ms) - (2025.05.16)
from functools import lru_cache
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        def hamming_distance(a, b):
            return sum(c1 != c2 for c1, c2 in zip(a, b))

        n = len(words)

        @lru_cache(None)
        def dfs(i, last_group, last_word):
            if i == n:
                return []
            take = []
            if len(words[i]) == len(last_word) and hamming_distance(words[i], last_word) == 1:
                if groups[i] != last_group:
                    take = [words[i]] + dfs(i + 1, groups[i], words[i])
            skip = dfs(i + 1, last_group, last_word)
            return max(len(take),len(skip))

        res = []
        for i in range(n):
            curr = [words[i]] + dfs(i + 1, groups[i], words[i])
            if len(curr) > len(res):
                res = curr

        return res


# solution 2 - (topological sort) - (2025.05.16)


# wrong answer - 최적의 답 보장 못함(그리디)
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        def hamming_distance(a, b):
            return sum(c1 != c2 for c1, c2 in zip(a, b))

        answer = []
        segment = []

        for i in range(len(words)):

            if answer and len(words[i]) == len(answer[-1]):
                if hamming_distance(words[i], answer[-1]) == 1:
                    if groups[i] != segment[-1]:
                        segment.append(groups[i])
                        answer.append(words[i])
            elif len(answer) == 0:
                answer.append(words[i])
                segment.append(groups[i])

        return answer