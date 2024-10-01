from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        modular_counts = defaultdict(int)
        for n in arr:
            modular_counts[n % k] += 1

        if modular_counts[0] % 2 == 1:
            return False

        for i in range(1, k):
            if modular_counts[i] != modular_counts[k - i]:
                return False

        return True
