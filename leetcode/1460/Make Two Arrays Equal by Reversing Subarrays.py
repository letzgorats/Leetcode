# solution 1
from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        if set(target) != set(arr):
            return False

        t = Counter(target)
        a = Counter(arr)

        if t != a:
            return False

        return True

# solution 2 - simple code(one-line code)
from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(arr) == Counter(target)