# solution 1
import re
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        # expression = re.split('[-|+|*]',expression)

        if expression.isdigit():
            return [int(expression)]

        res = []
        for i, char in enumerate(expression):
            if char in "+-*":
                # 왼쪽과 오른쪽 부분을 재귀적으로 계산
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i + 1:])

                # 왼쪽과 오른쪽 결과를 연산
                for left in left_results:
                    for right in right_results:
                        if char == "+":
                            res.append(left + right)
                        elif char == "-":
                            res.append(left - right)
                        elif char == "*":
                            res.append(left * right)

        return res


# solution 2
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }

        def backtrack(left, right):

            res = []

            for i in range(left, right + 1):
                op = expression[i]
                if op in operations:
                    nums1 = backtrack(left, i - 1)
                    nums2 = backtrack(i + 1, right)

                    for n1 in nums1:
                        for n2 in nums2:
                            res.append(operations[op](n1, n2))

            if res == []:
                res.append(int(expression[left:right + 1]))

            return res

        return backtrack(0, len(expression) - 1)

# solution 3
class Solution:
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }

    def diffWaysToCompute(self, expression: str) -> List[int]:

        res = []

        for i in range(len(expression)):
            op = expression[i]
            if op in self.operations:
                nums1 = self.diffWaysToCompute(expression[:i])
                nums2 = self.diffWaysToCompute(expression[i + 1:])

                for n1 in nums1:
                    for n2 in nums2:
                        res.append(self.operations[op](n1, n2))

        if res == []:
            res.append(int(expression))

        return res







