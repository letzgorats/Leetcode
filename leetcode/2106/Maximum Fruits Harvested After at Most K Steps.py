# solution 1 - (sliding window,two pointers) - (130ms) - (2025.08.03)
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:

        def steps_required(left, right, start):
            return min(
                abs(start - left) + (right - left),
                abs(start - right) + (right - left)
            )

        n = len(fruits)
        left = 0
        total = 0
        max_fruits = 0

        for right in range(n):
            total += fruits[right][1]

            while left <= right and steps_required(fruits[left][0], fruits[right][0], startPos) > k:
                total -= fruits[left][1]
                left += 1

            max_fruits = max(max_fruits, total)

        return max_fruits


'''
두 가지 경로를 비교

1. start -> left -> right : abs(start-left) + (right-left)
2. start -> right -> left : abs(start-right) + (right-left)

즉, start 에서 가장 먼 끝까지 돌아가는 최소 거리를 반환하는 함수

while 문 
-> 현재 [left,right] 범위가 startPos 에서 왕복 가능한 거리 k 를 초과하면
    - 윈도우 왼쪽을 줄이면서 total 도 같이 줄임
    - 즉, 슬라이딩 윈도우 유지

max
-> 현재 유효한 윈도우 내 과일 합이 max_fruits 보다 크면 갱신


즉,
statPos 를 기준으로 왼쪽과 오른쪽 구간을 유지하면서, 거리 조건을 만족하는 범위 안에서 
슬라이딩 윈도우로 과일 수의 최대 합을 구하는 투포인터 알고리즘 이다.
'''

