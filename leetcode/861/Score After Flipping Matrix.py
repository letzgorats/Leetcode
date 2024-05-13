class Solution(object):
    def matrixScore(self, grid):

        n = len(grid)
        m = len(grid[0])

        # flipping row
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] = (grid[i][j] ^ 1)

        # flipping col
        for j in range(m):
            tmp = 0
            for i in range(n):
                tmp += grid[i][j]
            if tmp <= n//2:
                for i in range(n):
                    grid[i][j] ^= 1

        answer = 0
        for i in range(n):
            tmp = 0
            number = 0
            for x in grid[i][::-1]:
                number += x * (2 ** tmp)
                tmp += 1
            answer += number

        return answer

# There are only two rules that you need to know in this problem. 
# 1. If the first number in the row is 0, flip the row. 
# 2. If the count of 0 in the col is greater than the count of 1


'''
"
1. If the first number in the row is 0, flip the row." (행의 첫 번째 숫자가 0이면 행을 뒤집습니다.)

이진수에서 가장 왼쪽 비트(가장 상위 비트)는 가장 큰 가중치를 갖습니다. 
예를 들어, 이진수 1000은 십진수로 8이며, 0111은 십진수로 7입니다. 따라서 각 행의 가장 왼쪽 비트가 1이 되도록 하는 것이 점수를 최대화하는 전략입니다.
행의 첫 번째 숫자가 0인 경우, 그 행을 뒤집으면 첫 번째 숫자가 1이 되므로 해당 행의 값이 최대한 크게 됩니다.
같은 원리로 최상위비트가 1이면 뒤집지 않습니다.

2. If the count of 0 in the column is greater than the count of 1, flip the column." (열에서 0의 개수가 1의 개수보다 많으면 열을 뒤집습니다.)

이 규칙은 각 열의 값을 최대화하기 위한 것입니다. 이진수의 각 비트 위치는 고정된 가중치를 가지므로, 각 열에서 1의 개수를 최대화하면 전체 행렬의 값이 증가합니다.
예를 들어, 어떤 열이 0, 0, 0, 1로 구성되어 있고, 이 열을 뒤집으면 1, 1, 1, 0이 되어 1의 개수가 더 많아집니다. 
이는 그 열에 해당하는 이진수 가중치의 합을 증가시키며, 결과적으로 전체 행렬의 점수도 증가합니다.

'''
# calculating -> int(str_, 2) : 숫자로 된 해당 이진수 str_을 십진수로 바꾸는 방법 
class Solution(object):
    def matrixScore(self, grid):
        
        n = len(grid)
        m = len(grid[0])

        # flipping row
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] = (grid[i][j] ^ 1)
                  
        # flipping col
        for j in range(m):
            tmp = 0
            for i in range(n):
                tmp += grid[i][j]
            if tmp <= n//2:
                for i in range(n):
                    grid[i][j] ^= 1

        answer = 0
        for i in range(n):
            answer += int("".join([str(i) for i in grid[i]]),2)

        return answer
