# TLE
class Solution:
    def minEnd(self, n: int, x: int) -> int:

        # nums의 모든 요소에 대해 AND 연산의 결과가 x 가 되어야 한다고
        # 했으니, 배열의 모든 수는 반드시 x 의 비트 패턴을 유지해야 함.
        # x 의 비트 패턴 유지 조건은, 배열의 각 요소는 x의 1로 설정된
        # 비트는 반드시 1을 유지해야 하고, 0 인 비트는 자유롭게 선택 가능
        # 그러므로, AND 연산을 통해 x 가 되려면 배열의 최소값은 무조건
        # x 이상이어야 한다. 만약 x 보다 작은 수가 포함되면, 비트 패턴이
        # 맞지 않아 AND 결과가 x 가 될 수 없다.

        nums = [x]

        for i in range(1, n):

            # nums 배열의 마지막 요소에서 1을 더하면서 새로운 요소 만듦
            next_num = nums[-1] + 1

            # AND 연산 결과가 x가 될 때 까지 next_num 증가
            while (next_num & x) != x:
                next_num += 1

            nums.append(next_num)

        return nums[-1]

# solution
class Solution:
    def minEnd(self, n: int, x: int) -> int:

        res = x
        i_x = 1
        i_n = 1  # for n-1

        while i_n <= n - 1:

            if i_x & x == 0:
                if i_n & (n - 1):
                    res = res | i_x
                i_n = (i_n << 1)

            i_x = (i_x << 1)

        return res
