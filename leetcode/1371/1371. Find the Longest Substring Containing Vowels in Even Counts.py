# solution 1
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        mask_to_idx = {0: -1}
        n = 0
        answer = 0

        for idx, alpha in enumerate(s):

            if alpha in vowels:
                n ^= vowels[alpha]

            if n not in mask_to_idx:
                mask_to_idx[n] = idx

            else:
                answer = max(answer, idx - mask_to_idx[n])

        return answer

# solution 2
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        vowels = 'aeiou'

        res = 0
        mask = 0
        mask_to_idx = {0: -1}  # (ex) "xxxx" -> idx:3 3-(-1) = 4

        for i, c in enumerate(s):

            if c in vowels:
                mask = mask ^ (1 + ord(c) - ord('a'))

            if mask in mask_to_idx:
                length = i - mask_to_idx[mask]
                res = max(res, length)

            else:
                mask_to_idx[mask] = i

        return res

# solution 3
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        vowels = {
            "a": 1,
            "e": 2,
            "i": 4,
            "o": 8,
            "u": 16
        }

        res = 0
        mask = 0
        mask_to_idx = [-1] * 32

        for i, c in enumerate(s):

            mask = mask ^ vowels.get(c, 0)

            if mask_to_idx[mask] != -1 or mask == 0:
                length = i - mask_to_idx[mask]
                res = max(res, length)

            else:
                mask_to_idx[mask] = i

        return res
