# solution 1 - (enumeration,greedy,optimization) - (219ms) - (2025.07.10)
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)
        canMove = [False] * n  # i번째 회의를 자유롭게 다른 gap으로 옮길 수 있는지 여부

        # 앞으로 가면서 왼쪽 gap(t1)을 확인
        maxLeftGap = 0
        for i in range(n):
            duration = endTime[i] - startTime[i]

            # 이 회의를 이전 gap으로 옮길 수 있으면 True
            if duration <= maxLeftGap:
                canMove[i] = True

            # 다음 회의와의 gap을 계산
            if i == 0:
                maxLeftGap = startTime[0]  # 처음 회의까지의 gap
            else:
                maxLeftGap = max(maxLeftGap, startTime[i] - endTime[i - 1])

        # 뒤에서부터 가면서 오른쪽 gap(t2)을 확인
        maxRightGap = 0
        for i in range(n - 1, -1, -1):
            duration = endTime[i] - startTime[i]

            # 이 회의를 다음 gap으로 옮길 수 있으면 True
            if duration <= maxRightGap:
                canMove[i] = True

            if i == n - 1:
                maxRightGap = eventTime - endTime[-1]  # 마지막 회의 이후 gap
            else:
                maxRightGap = max(maxRightGap, startTime[i + 1] - endTime[i])

        # 이제 각 회의를 "제거해도 되나" 여부(canMove[i])를 기준으로
        # 이 회의를 제거했을 때, 생길 수 있는 가장 큰 자유시간을 계산
        maxFree = 0
        for i in range(n):
            left = 0 if i == 0 else endTime[i - 1]
            right = eventTime if i == n - 1 else startTime[i + 1]
            duration = endTime[i] - startTime[i]

            if canMove[i]:
                # i번째 회의를 완전히 제거할 수 있으므로, 그 위치를 통째로 gap으로 씀
                maxFree = max(maxFree, right - left)
            else:
                # 이 회의를 제거하지 못하므로, 최소한 duration은 빠져야 함
                # (그 회의는 다른 곳으로 이동하더라도 어딘가에 차지하고 있어야 하니까)
                maxFree = max(maxFree, right - left - duration)

        return maxFree

'''
문제를 풀면서 간과했던 점

1. 단순 완전탐색(O(n^2))으로는 TLE 발생
- 회의를 "제거하고, gap 에 삽입하는 시뮬레이션" 방식은 규모가 큰 입력에서 시간초과가 발생했다.
2. 회의를 반드시 어딘가에 유지해야 한다는 점도 계산에서 놓치기 쉽다.
- 제거했다고 해서 공간 전체가 자유 시간이 되는 건 아님

전략

1. 회의 앞뒤 gap 만 O(n)으로 한 번씩 훑으면, "이 회의가 다른 곳으로 옮겨질 수 있는가?"를 빠르게 판단할 수 있다.

2. canMove[i] = True 면 이 회의를 제거해도 문제 없다.
- 해당 위치의 전체 공간을 자유시간으로 활용 가능(right-left)

3. canMove[i] = False 면 이 회의는 어딘가에 존재해야 하므로
- duration 만큼 줄어든 자유시간만 활용 가능 하다.(right-left-duration)


이 문제는 시뮬레이션에 기반한 조건 기반 논리로 푸는게 맞다.
left/right는 "자유공간"의 경계값이라는 점을 명확히 이해해야 했다.
단순 반복보다 앞/뒤에서 누적되는 gap 추적이 매우 강력한 최적화 수단이었다.


(ex)

0---1---2---3---4---5---6---7---8---9--10
        [2,3]   [4,5]   [6,7]

Case 1: i = 1 (회의 [4, 5]) 제거

🔍 Step 1. left와 right 계산 
left = endTime[0] = 3
→ 이전 회의가 끝난 시간

right = startTime[2] = 6
→ 다음 회의가 시작하는 시간

즉, 자유시간 범위: [3, 6]


🔍 Step 2. 회의 duration 계산
duration = endTime[1] - startTime[1] = 1

----------------------------------------------------------------------------
[두 가지 경우 비교]

✅1) canMove[1] == True (이 회의는 완전히 제거할 수 있음)
즉, 회의 [4,5]를 완전히 다른 곳으로 옮길 수 있음
그러면 [3,6] 이 구간 전체가 자유 시간

자유 시간 = right - left = 6 - 3 = 3

❌2) canMove[1] == False (이 회의는 제거할 수 없음)
이 회의는 "꼭 존재해야" 해서, 어딘가엔 들어가야 함
해당 시간 구간 내에서 duration만큼 줄어든 공간이 자유 시간

자유 시간 = right - left - duration = 6 - 3 - 1 = 2

다른 회ㅐ의들도 확인하면
| i | 회의     | left | right | duration | canMove | 자유 시간 (True) | 자유 시간 (False) |
| - | ------  | ---- | ----- | -------- | ------- | ------------ | ------------- |
| 0 | [2,3]   | 0    | 4     | 1        | ?       | 4            | 3             |
| 1 | [4,5]   | 3    | 6     | 1        | ?       | 3            | 2             |
| 2 | [6,7]   | 5    | 10    | 1        | ?       | 5            | 4             |


✅ canMove[i]란
-> "회의 i를 다른 위치로 옮길 수 있는가?"를 나타내는 Boolean 값
즉,
👉 i번째 회의의 duration이, 앞이나 뒤의 빈 공간(gap)보다 작거나 같다면 True
👉 그렇지 않다면 False


[핵심 조건]
if duration <= maxLeftGap or duration <= maxRightGap:
    canMove[i] = True

그럼, 여기서 maxLeftGap, maxRightGap 이 뭔데?

1. maxLeftGap (앞쪽 gap)
- 앞에서부터 진행하면서 현재까지의 최대 왼쪽 gap을 저장
- 즉, 회의 i가 제거되었을 때 그 앞의 빈 공간이 충분한가?

2. maxRightGap (뒤쪽 gap)
- 뒤에서부터 진행하면서 현재까지의 최대 오른쪽 gap을 저장
- 즉, 회의 i를 제거했을 때 그 뒤쪽 gap에 옮겨 넣을 수 있는가?

이걸 효율적으로 하기 위해 왼쪽/오른쪽을 각각 한번씩만 O(n)으로 훑는 방식을 쓰는 것이었다!

'''