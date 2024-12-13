class Solution:
    def findScore(self, nums: List[int]) -> int:

        score = 0
        q = []
        for idx, num in enumerate(nums):
            q.append((num, idx))

        q = sorted(q)
        marked = set()
        for num, idx in q:

            if idx not in marked:
                score += num
                pre, nxt = idx - 1, idx + 1
                if 0 <= pre:
                    marked.add(pre)
                if nxt < len(nums):
                    marked.add(nxt)

        return score