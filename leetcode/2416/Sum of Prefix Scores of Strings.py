# solution 1 - my solution -4685ms
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        # a : 2
        # ab : 2
        # abc : 1

        # b : 2
        # bc : 1

        scores = defaultdict(int)

        for w1 in words:
            cur = ""
            for ch in w1:
                cur += ch
                # print(cur)
                if cur in scores:
                    scores[cur] += 1
                else:
                    scores[cur] = 1
                # scores[cur] = scores.get(scores[cur],0) + 1

        # print(scores)
        answer = [0] * len(words)
        for idx, w2 in enumerate(words):
            # tmp = 0
            for i in range(len(w2)):

                if w2[:i + 1] in scores:
                    answer[idx] += scores[w2[:i + 1]]

        return answer
