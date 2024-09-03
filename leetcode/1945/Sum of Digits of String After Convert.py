class Solution:
    def getLucky(self, s: str, k: int) -> int:

        convert = ""
        for alpha in s:
            convert += str(ord(alpha) - 96)

        for _ in range(k):
            transform = 0
            for c in convert:
                transform += int(c)

            convert = str(transform)

        return transform
