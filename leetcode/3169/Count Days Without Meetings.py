# solution 1 - sort, greedy - (185ms) - (2025.03.24)
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings = sorted(meetings, key=lambda x: (x[0], x[1]))

        # print(meetings)
        cnt = 0
        current_availableDay = 1

        for start, finish in meetings:

            if start >= current_availableDay:
                cnt += (start - current_availableDay)
            # else:   # start < current_availableDay => overlapping
            if finish >= current_availableDay:
                current_availableDay = finish + 1

            # print(current_availableDay)
            # print("cnt",cnt)

        # 남은 여유 날짜 추가
        if current_availableDay <= days:
            cnt += days - current_availableDay + 1

        return cnt