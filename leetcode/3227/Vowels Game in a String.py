from collections import Counter
# solution 1 - (math,counter) - (68ms) - (2025.09.12)
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        state = Counter(s)

        if any(v in state for v in vowels):
            return True
        return False
