# solution 1
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        tuples = []
        for idx, n in enumerate(nums):
            tmp = ""
            for i in str(n):
                tmp += str(mapping[int(i)])
            tuples.append((int(tmp), n, idx))

        answer = sorted(tuples, key=lambda x: (x[0], x[2]))
        # print(answer)

        return [x[1] for x in answer]


# solution 2
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def convert(num):
            res = 0
            m = 1
            if num == 0:
                return mapping[num]
            while num:
                res += mapping[num%10] * m
                num //= 10
                m *= 10
            return res

        nums.sort(key=lambda x : convert(x))
        return nums
