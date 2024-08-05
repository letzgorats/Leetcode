from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        counts = Counter(arr)
        print(counts)
        for alpha, v in counts.items():
            if v == 1:
                k -= 1
                if k == 0:
                    return alpha

        return ""