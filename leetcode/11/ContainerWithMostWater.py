# solutino 2 - - (two pointers) - (63ms) - (2025.10.05)
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        current = 0
        while left < right:
            if height[left] < height[right]:  # 왼쪽 막대 높이가 더 낮다면, 높은쪽을 찾기 위한 진행
                current = max(current, (right - left) * height[left])
                left += 1  # 왼쪽 + 1
            else:  # 오른쪽 막대 높이가 더 낮다면, 높은쪽을 찾기 위한 진행
                current = max(current, (right - left) * height[right])
                right -= 1  # 오른쪽 -1

        return current

'''
우리는 i = 0, j = height.size() - 1 에서 시작한다고 하자. 즉, i는 첫 번째 막대를, j는 마지막 막대를 가리킨다.
이제 일반성을 잃지 않고 h(i) > h(j)라고 가정하자.
이때 두 막대가 만들 수 있는 물의 용량(capacity)은 h(j) * (j - i)로 계산된다.

이제 생각해보자. j를 마지막 위치에 고정시킨 채 i를 오른쪽으로 옮겨본다면, 더 큰 물의 용량을 얻을 수 있을까?
용량은 "두 막대의 높이 중 더 작은 값 × 두 막대 사이의 거리"로 계산된다.
즉, 이 값은 두 요인에 의해 결정된다: 높이와 너비(거리).

먼저 너비를 보자. i를 오른쪽으로 옮기면 항상 거리 (j - i)가 줄어든다. → 즉, 너비는 작아진다.
다음으로 높이를 보자. 용량을 계산할 때는 min(h(i), h(j))를 사용한다. 그런데 h(i)를 오른쪽으로 옮긴다고 해도, h(i)는 여전히 h(j)보다 작거나 같을 것이다. → 즉, 높이 또한 커질 수 없다.

따라서 두 요인(높이, 너비) 모두 감소하거나 유지될 뿐, 동시에 커질 수 없으므로 용량이 커질 가능성은 없다.
이 말은 곧 "i를 옮겨봤자 의미가 없고, j를 왼쪽으로 한 칸 이동하는 것이 합리적"이라는 뜻이다.

이 논리를 반복하면, 결국 투 포인터를 양쪽 끝에서 좁혀오면서 효율적으로 최댓값을 구할 수 있다는 것이 증명의 핵심이다.

요약하자면 👉

"작은 쪽 막대를 안쪽으로 옮겨야 한다. 큰 쪽을 고정하고 작은 쪽을 옮기는 것은 최댓값을 잃지 않기 때문이다."


문제 이해 아직도 안 간다면?
-> 이 문제는 정말 간단히 말하면 "막대들 중에서 두 개를 골라서, 그 두 막대가 만들 수 있는 물의 면적 중 최대값을 구하는 문제"이다.
-> 즉, 여러 막대 중에서 딱 두 개만 선택해서 계산하는 거고, 그 두 개 사이에 다른 막대가 몇 개 있든 상관없다.

-> 넓이 = min(두 막대의 높이) × (두 막대 사이의 거리)

-> 그리고 모든 가능한 (i, j) 쌍에 대해 이 넓이를 계산했을 때, 가장 큰 값을 찾는 것이다. 간단한 문제이다.
근데, for문으로 O(n^2)로 풀면 비효율코드라 시간초과가 당연히 걸리고, 왼쪽, 오른쪽을 좁혀가면서 찾는 문제이다.
-> 즉, 더 낮은 쪽을 버리고, 더 높은 벽을 찾으러 이동하는 과정

-> 물론 위 코드가 가장 최적화한 코드인데, 의미없는 높이를 스킵하는 코드를 넣어도 되는데, 사실 큰 성능차이가 없기에, 위 코드가 가장 최적임.

'''
# 위 코드 중복되는 코드를 일부 통일 - (103ms)
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        current = 0
        while left < right:
            h = min(height[left], height[right])
            current = max(current, h * (right - left))
            if height[left] < height[right]:  # 왼쪽 막대 높이가 더 낮다면, 높은쪽을 찾기 위한 진행
                left += 1  # 왼쪽 + 1
            else:  # 오른쪽 막대 높이가 더 낮다면, 높은쪽을 찾기 위한 진행
                right -= 1  # 오른쪽 -1

        return current

        # solution 1 - (two pointers) - (566ms,63ms) - (2023.04.20)
class Solution(object):
    def maxArea(self, height):

        left = 0
        right = len(height)-1
        max_amount = 0  # tentative answer

        # decide the standard height
        while(left < right):
            change_left, change_right = False, False

            if height[left] < height[right]:
                standard = height[left]
                change_left = True
            else:
                standard = height[right]
                change_right = True

            amount = (right-left) * standard
            max_amount = max(max_amount,amount) # renew the max_amount compared to original_max_amount

            if change_left :
                left += 1   # let's change the start point
            elif change_right:
                right -= 1  # let's change the end point

            # print(max_amount)
    
        return max_amount
        
        """
        :type height: List[int]
        :rtype: int
        """
