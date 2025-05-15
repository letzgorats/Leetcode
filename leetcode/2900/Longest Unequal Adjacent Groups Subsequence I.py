# solution 1 - (greedy,array) - (0ms) - (2025.05.15)
from typing import List
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        answer = [words[0]]
        g = groups[0]
        for i in range(1, len(words)):
            if groups[i] != g:
                answer.append(words[i])
                g = groups[i]

        return answer