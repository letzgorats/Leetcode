# solution 1 - (backtracking,xpr) - (35ms) - (2024.05.20)
from itertools import combinations
class Solution(object):
    def subsetXORSum(self, nums):
      
        def backtracking(index,cur_xor):

            if index == len(nums):
                return cur_xor
            
            # 현재 요소를 포함
            include = backtracking(index+1,cur_xor ^ nums[index])
            
            # 현재 요소를 포함 x
            exclude = backtracking(index+1,cur_xor)

            return include + exclude

        return backtracking(0,0)
        
# solution 2 - (backtracking) - (47ms) - (2025.04.05)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def backtracking(cur, idx):
            nonlocal n

            candi.append(cur)
            if idx == n:
                return

            for i in range(idx, n):
                nxt = cur[:] + [nums[i]]
                backtracking(nxt, i + 1)

        candi = list()
        n = len(nums)
        backtracking([], 0)

        answer = 0
        for lst in candi:
            xor_val = 0
            for j in lst:
                xor_val ^= j
            answer += xor_val

        return answer


# solution 3 - (backtracking,accumulative) - (15ms) - (2025.04.05)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtracking(cur, idx):
            if idx == len(nums):
                return cur

            include = backtracking(cur ^ nums[idx], idx + 1)
            exclude = backtracking(cur, idx + 1)

            return include + exclude

        return backtracking(0, 0)

# solution 4 - (bitmask,accumulative) - (15ms) - (2025.04.05)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        n = len(nums)
        answer = 0

        for mask in range(1 << n):  # 0 번 부터 2^n-1 까지
            xor_val = 0
            for i in range(n):
                if mask & (1 << i):  # i 번째 현재 부분집합에 포함되는지 확인
                    xor_val ^= nums[i]
            answer += xor_val

        return answer


'''
mask 의 의미는 이진수로 표현한 부분집합의 포함 여부를 나타낸다.
(ex) nums = [1,100] 이라고 하면, len(nums) == 2 이므로, range(1<<n) 은 4가 된다.
--> for mask in range(4): 이므로, Mask s는 0,1,2,3 순서로 값을 가지게 된다.


    mask(10진수)         mask(2진수)        포함된 원소(nums 기준)
        0                   00                  [] 공집합
        1                   01                  [1]   0번째 인덱스에 있는 1
        2                   10                  [100] 1번째 인덱스에 있는 100
        3                   11                  [1,100] 0번째 인덱스와 1번째 인덱스에 있는 [1,100]

즉, (mask). & (1<<i) 는 i 번째 비트가 1인지 확인(=i번째 원소가 nums에 포함됐는지 확인하는 작업이다.)
nums 의 실제값이 어떤지는 상관없이, 우리는 각 인덱스를 포함할지 말지를 비트로 표현하고 있을 뿐이다.
'''