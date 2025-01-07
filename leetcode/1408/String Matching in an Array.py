# solution 1
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        answer = set()
        for w1 in words:
            for w2 in words:
                if w1 in answer or w2 in answer:
                    continue
                else:
                    if w1 != w2:
                        if w1 in w2:
                            answer.add(w1)
                        elif w2 in w1:
                            answer.add(w2)

        return list(answer)

# solution 2
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        words.sort(key=len, reverse=True)

        answer = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j] in words[i]:
                    answer.append(words[j])

        return list(set(answer))