# solution 1 - (array,string) - (0ms) - (2025.05.24)
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        answer = []
        for idx, w in enumerate(words):
            if x in w:
                answer.append(idx)

        return answer
