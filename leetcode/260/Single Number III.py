# hash solution
class Solution(object):
    def singleNumber(self, nums):
        
        nums_set = dict()

        for n in nums:

            nums_set[n] = nums_set.get(n,0) + 1

        answer = []
        for k,v in nums_set.items():

            if v == 1:
                answer.append(k)

        return answer




# bit manipulation solution
class Solution(object):
    def singleNumber(self, nums):

        xors = 0

        for num in nums:

            xors = xors ^ num

        lowbit = xors & -xors

        first, second = 0,0
        for num in nums:
            if num & lowbit:
                first ^= num
            else:
                second ^= num
        
        return [first,second]
