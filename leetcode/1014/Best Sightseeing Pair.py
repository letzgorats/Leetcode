# solution 1 - sliding window, greedy, dp
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        max_score = 0
        max_i = values[0] # 초기값 values[i] + i (첫번째 원소로 설정)

        for j in range(1,len(values)):
            # 현재 j를 기준으로 최댓값 경신
            max_score = max(max_score,max_i+values[j]-j)

            # max_i를 갱신 (i가 증가함에 따라)
            max_i = max(max_i,values[j]+j)

        return max_score

# solution 2 - sliding window, greedy, dp
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        max_score = 0
        cur_max = values[0] -1 # 두 번째 원소와의 거리 1을 뺀 초기값 values[0]

        for i in range(1,len(values)):

            max_score = max(max_score, values[i] + cur_max)
            cur_max = max(cur_max-1,values[i]-1)

        return max_score

# TLE
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        a, b = [0] * len(values), [0] * len(values)
        for i, val in enumerate(values):
            a[i] = val + i
            b[i] = val - i

        total = 0
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                total = max(total, a[i] + b[j])

        return total