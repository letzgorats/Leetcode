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


# solution 2 - trie - 2980ms

class PrefixNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, w):

        cur = self.root
        for c in w:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = PrefixNode()
            cur = cur.children[i]
            cur.count += 1

    def get_score(self, w):
        cur = self.root
        score = 0
        for c in w:
            i = ord(c) - ord('a')
            cur = cur.children[i]
            score += cur.count
        return score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        res = []
        prefix_tree = PrefixTree()

        for w in words:
            prefix_tree.insert(w)

        for w in words:
            res.append(prefix_tree.get_score(w))

        return res