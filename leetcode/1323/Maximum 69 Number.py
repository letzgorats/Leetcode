# solution 1 - (greedy) - (0ms) - (2025.08.16)
class Solution:
    def maximum69Number(self, num: int) -> int:

        num = list(str(num))
        for i in range(len(num)):

            if num[i] == '9':
                continue
            else:
                num[i] = '9'
                break

        return int(''.join(num))