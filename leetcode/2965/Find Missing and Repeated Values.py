# solution 1 - array, hash table - (7ms,O(n^2)) - (2025.03.06)
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        numbers = set(i for i in range(1, n * n + 1))

        answer = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] not in numbers:
                    # element which appears twice is 'a'
                    answer.append(grid[i][j])
                else:
                    numbers.remove(grid[i][j])

        # left element in numbers is 'b'
        # [a,b]

        return answer + list(numbers)

# solution 2 - math - (7ms,O(n)) - (2025.03.06)
'''
1. n^2 값을 계산하여 총 개수를 저장한다.
2. `sum` 과 `sqrSum` 변수를 초기화하여 실제 그리드에서 숫자들의 합과 제곱합을 구한다.
3. 이론적으로 완벽한 합과 제곱 합을 구한다.
4. 두 값의 차이를 활용하여 `sumDiff` 와 `sqrDiff` 를 계산한다.
5. 방정식을 활용하여 x(중복된 값)와 y(누락된 값)를 구한다.
'''
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # 1. n^2 값을 계산하여 총 개수를 저장
        n = len(grid)
        total = n * n

        # 2. sum과 sqrSum 초기화 후 실제 그리드 값 계산
        sum_val = sum(num for row in grid for num in row)
        sqr_sum = sum(num * num for row in grid for num in row)

        # 3. 완벽한 합(perfectSum)과 제곱 합 계산
        perfectSum = total * (total + 1) // 2  # 1부터 n^2까지의 합
        # 1 부터 n^2까지의 제곱 합
        # 시그마 1~n k^2 합 공식 -> n(n+1)(2n+1) // 6
        # n^2 = (1부터 n) 까지의 합 + (1부터 n-1) 까지의 합
        perfectSqrSum = total * (total + 1) * (2 * total + 1) // 6

        # 4. 차이 계산
        sumDiff = sum_val - perfectSum  # x-y
        sqrDiff = sqr_sum - perfectSqrSum  # x^2-y^2

        # 5. 방정식을 활용하여 x(중복된 값), y(누락된 값) 구하기
        sumXY = sqrDiff // sumDiff  # (x+y)

        x = (sumXY + sumDiff) // 2  # x (중복된 값)
        y = (sumXY - sumDiff) // 2  # y (누락된 값)

        return [x, y]

