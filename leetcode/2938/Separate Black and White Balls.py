class Solution:
    def minimumSteps(self, s: str) -> int:

        one_count = 0
        answer = 0

        for i in s:

            if i == '1':
                one_count += 1
            else:
                answer += one_count

        return answer