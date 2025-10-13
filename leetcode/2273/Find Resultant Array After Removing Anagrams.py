# solution 1 - (Coutner,delete) - (35ms) - (2025.10.13)
from typing import List
from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        for i in range(len(words) - 1, 0, -1):

            state1 = Counter(words[i])
            state2 = Counter(words[i - 1])
            # print(state1,state2)
            if state1 == state2:
                del words[i]

        return words

# solution 2 - (sort) - (7ms) - (2025.10.13)
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        ans = [words[0]]
        for i in range(1, len(words)):

            current = sorted(words[i])
            prev = sorted(words[i - 1])
            # print(state1,state2)
            if current != prev:
                ans.append(words[i])

        return ans