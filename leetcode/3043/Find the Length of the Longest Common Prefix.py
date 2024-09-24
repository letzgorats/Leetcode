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
                    else:
                        break
                answer = max(answer, tmp)


        return answer

# solution
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        store = set()
        arr1Set = set(arr1)
        arr2Set = set(arr2)

        for val in arr2Set:
            cur = ""
            for ch in str(val):
                cur += ch
                if int(cur) not in store:
                    store.add(int(cur))

        answer = 0
        for val in arr1Set:
            cur = ""
            for ch in str(val):
                cur += ch
                if int(cur) in store:
                    answer = max(answer, int(len(cur)))

        return answer

