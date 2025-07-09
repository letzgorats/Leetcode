# solution 1 - (array,sliding window) - (35ms) - (2025.07.09)
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

        gaps = []
        n = len(startTime)
        endtime = 0
        for i in range(n):
            gaps.append(startTime[i] - endtime)
            endtime = endTime[i]

        gaps.append(eventTime - endtime)
        # print(gaps)

        m = len(gaps)
        max_sum = curr_sum = sum(gaps[:k + 1])  # 첫 구간 초기화
        for i in range(k + 1, m):
            curr_sum = curr_sum - gaps[i - (k + 1)] + gaps[i]  # 왼쪽 하나 뺴고, 오른쪽 하나 추가
            max_sum = max(max_sum, curr_sum)

        # print(max_sum)

        return max_sum

    #     0    1       2      3        4       5
    #          |-------|
    #                         |-----------------|

    #       1             1                      0

    #     0    1       2      3        4       5 .... 9       10
    #     |----|
    #                  |---------------|              |---------|

    #       0       1                       5                   0

    #     0    1       2      3        4       5      6
    #     |----|       |-------|
    #                          |-------|       |-------|

    #    0          1          0           1             0
'''
문제 풀이 중 간과했던 점

1. 회의 순서 변경 불가 조건을 놓침
- 처음엔 "[7,10] 회의를 [18,21]로 옮기면 더 긴 휴식시간이 생긴다"고 판단
-> 하지만 문제 조건에 “회의의 상대 순서는 유지해야 함” 이 명시되어 있음
-> [7,10]을 맨 뒤로 옮기는 건 불가능

2. eventTime이 10^9이면 시간초과 걱정?
- 처음엔 eventTime이 너무 커서 TLE가 날까 걱정
-> 하지만 실제 연산은 startTime과 endTime의 길이 n(최대 10^5)에 대해만 수행됨
-> eventTime은 "범위"일 뿐, loop의 대상이 아니므로 TLE 발생 X

3. 슬라이딩 윈도우 방식의 이해
- gaps 리스트는  "회의 사이의 빈 시간" 을 나타내고
- 연속된 k+1개의 gap을 sliding window로 탐색
- 이 방식은 회의를 최대 k개까지 이동해 빈 구간 최대 병합이 가능하다는 점에서 유효

'''