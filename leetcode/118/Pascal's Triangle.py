'''
The secrets of Pascal's' triangle(TED) -> https://www.youtube.com/watch?v=XMriWTvPXHI
'''

# Wrong answer - (math) - (2025.08.01)
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []

        for i in range(1, numRows + 1):
            number = pow(11, (i - 1))
            answer.append(list(map(int, str(number))))

        return answer
'''
row가 m번째 줄일 때
11^(n-1) 이 값을 이루는데, 이는 n<=5 까지만 유효하다.
6번째 줄 이후부터는 각 자리수가 더 이상 이항계수와 일치하지 않게 되기 때문인데, 
자리수의 덧셈으로 올림(carry)가 발생하면서 파스칼 삼각형의 성질과 달라져버리게 된다. 
'''


# solution 1 - (dp, math) - (0ms) - (2025.08.01)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        answer = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = answer[i - 1][j - 1] + answer[i - 1][j]
            answer.append(row)

        return answer

'''
nCk = n-1Ck-1 + n-1Ck
'''

# solution 2 - (combinations) - (0ms) - (2025.08.01)
import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        answer = []

        for n in range(numRows):
            row = []
            for k in range(n + 1):
                row.append(math.comb(n, k))  # C(n,k)
            answer.append(row)

        return answer

'''
            0C0
          1C0 1C1
        2C0 2C1 2C2
     3C0 3C1 3C2 3C3
   4C0 4C1 4C2 4C3 4C4
 5C0 5C1 5C2 5C3 5C4 5C5
6C0 6C1 6C2 6C3 6C4 6C5 6C6
            ...
            ...
'''


