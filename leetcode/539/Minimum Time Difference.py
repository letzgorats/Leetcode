# solution 1(66ms)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        answer = 1440
        min_convert = []
        # HH:MM 을 모두 분으로 convert
        for tp in timePoints:
            tp = list(map(int, tp.split(':')))
            h, m = tp[0] * 60, tp[1]
            min_convert.append(h + m)

        min_convert.sort()
        for i in range(len(min_convert) - 1):
            # circular 특성을 생각한 두 가지 경우 모두 고려
            a, b = 24 * 60 + min_convert[i], min_convert[i]
            candi = min(abs(b - min_convert[i + 1]), abs(a - min_convert[i + 1]))
            answer = min(answer, candi)
            # answer이 0 이면 더 이상 고려할 필요도 없이 최소값은 0
            if answer == 0:
                return answer

        # 마지막 시각과 처음 시각도 비교(circular)
        answer = min(answer, abs(24 * 60 + min_convert[0] - min_convert[-1]))

        return answer

# solution 2(71ms)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        answer = 1440
        min_convert = []
        # HH:MM 을 모두 분으로 convert
        for tp in timePoints:
            tp = list(map(int, tp.split(':')))
            h, m = tp[0] * 60, tp[1]
            min_convert.append(h + m)

        min_convert.sort()
        for i in range(len(min_convert) - 1):
            # 그냥 이렇게 해도 된다. 어차피 정렬된 min_convert 리스트이기 때문
            answer = min(answer, min_convert[i + 1] - min_convert[i])
            # answer이 0 이면 더 이상 고려할 필요도 없이 최소값은 0
            if answer == 0:
                return answer

        # 마지막 시각과 처음 시각도 비교(circular)
        answer = min(answer, abs(24 * 60 + min_convert[0] - min_convert[-1]))

        return answer