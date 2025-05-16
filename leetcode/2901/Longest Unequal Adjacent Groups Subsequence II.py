# solutino 1 - (dfs) - (2025.05.16)



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