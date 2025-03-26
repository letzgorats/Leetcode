# solution 1 - math, median, mod, grid - (187ms) - (2025.03.26)

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        elements = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                elements.append(grid[i][j])

        elements.sort()

        # step 1 - uni-valid grid
        # 모든 원소들의 차이가 x 로 나누어 떨어져야 한다.
        # for i in range(len(elements)-1):
        #     for j in range(1,len(elements)):
        #         if abs(elements[j]-elements[i]) % x !=0 :
        #             return -1
        base = elements[0]
        for num in elements:
            if abs(num - base) % x != 0:
                return -1
        '''
        왜 모든 쌍을 비교하지 않고, 첫 번째 값과의 차이만 보면 충분할까?
        - 모든 값들이 x만큼 더하거나 빼서 같은 값이 될 수 있어야 한다.
        - 즉, 모든 값들 간의 차이가 x로 나누어 떨어져야 한다.
        -> abs(a-b) % x == 0

        그런데, 굳이 모든 쌍을 비교할 필요 없이 하나의 기준 값(ex.첫 번째 값)과만
        비교해도 충분한 이유는?
        - 수학적으로 a ≡ b (mod x), a ≡ c (mod x) 이면,
        -> b ≡ c (mod x) 도 자동으로 성립한다.
        ('≡' 은 '동승값'으로 다시 말해 'a ≡ b' 라면 'a 와 b를 x 로 나눈 나머지가 같다'는 말이다.)

        떄문에 불필요하게 O(n^2) 비교를 할 필요없이 O(n) 으로 시간복잡도를 줄일 수 있다.
        '''

        # step 2 - 목표값은 중앙값(median)으로 수렴되어야 최소연산
        median = elements[len(elements) // 2]
        # print(median)

        answer = 0
        for i in range(len(elements)):
            answer += abs(elements[i] - median) // x

        return answer


