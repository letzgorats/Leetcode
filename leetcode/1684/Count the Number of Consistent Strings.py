# solution 3 - &
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        allowed = set(allowed)
        res = 0
        for w in words:
            if set(w) & allowed == set(w):
                res += 1

        return res

# solution 2 - intersection
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        allowed = set(allowed)
        res = 0
        for w in words:
            if set(w).intersection(allowed) == set(w):
                res += 1

        return res

# solution 3 - issubset
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        res = 0
        for w in words:
            if set(w).issubset(set(allowed)):
                res += 1

        return res