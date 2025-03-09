# TLE - greedy - (TLE) - (2025.03.09)
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        colors += colors
        # print(colors)
        n = len(colors)
        # [0,1,0,0,1,0,1] + [0,1,0,0,1,0,1]
        ans = 0
        for i in range(n // 2):
            prev = colors[i]
            diff = False
            for num in colors[i + 1:i + k]:
                if prev != num:
                    diff = True
                    prev = num
                else:
                    diff = False
                    break
            if diff:
                ans += 1

        return ans

# solution 1 - sliding window - (739ms) - (2025.03.09)
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        n = len(colors)
        ans = 0

        alternating_count = 1  # 연속된 교차 개수

        for i in range(1, n + k - 1):  # 순환을 고려하여 k-1 길이까지 확인
            if colors[i % n] != colors[(i - 1) % n]:  # 이전 값과 다르면 증가
                alternating_count += 1
            else:
                alternating_count = 1  # 연속이 끊기면 다시 1부터

            if alternating_count >= k:  # k 개 이상 연속되면 카운트 증가
                ans += 1

        return ans
