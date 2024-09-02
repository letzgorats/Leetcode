class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        leftover = k % sum(chalk)
        answer = 0

        for i in range(len(chalk)):

            leftover -= chalk[i]
            if leftover < 0:
                answer = i
                break

        return answer