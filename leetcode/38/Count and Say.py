# solution 1- recursive - (7ms) - (2025.04.18)
class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        count = 1
        result = ""

        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result += str(count) + prev[i - 1]
                count = 1

        result += str(count) + prev[-1]

        return result


# solution 2 - iterative - (7ms) - (2025.04.18)
class Solution:
    def countAndSay(self, n: int) -> str:

        result = "1"  # 시작문자열

        for _ in range(n - 1):
            tmp = ""
            count = 1
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    tmp += str(count) + result[i - 1]
                    count = 1

            tmp += str(count) + result[-1]  # 마지막 그룹 처리
            result = tmp

        return result
