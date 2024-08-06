from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        counts = sorted(counts.items(), key=lambda x: -x[1])
        # print(counts)

        idx = 0
        answer = 0
        for alpha, times in counts:
            answer += times * (idx // 8 + 1)
            idx += 1

        return answer

