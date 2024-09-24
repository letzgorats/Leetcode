# TLE
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        answer = 0
        arr1Set = set(arr1)
        arr2Set = set(arr2)

        for num1 in arr1Set:
            for num2 in arr2Set:
                tmp = 0
                if len(str(num1)) >= len(str(num2)):
                    a = str(num1)
                    b = str(num2)
                else:
                    a = str(num2)
                    b = str(num1)
                for i in range(len(b)):
                    if a[i] == b[i]:
                        tmp += 1
                answer = max(answer, tmp)

        return answer


