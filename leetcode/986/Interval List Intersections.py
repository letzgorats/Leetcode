# solution 1 - min,max,interval,two pointers - (5ms) - (2025.03.30)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        entire_list = sorted(firstList + secondList, key=lambda x: x[0])
        answer = []
        pres, pref = entire_list[0][0], entire_list[0][1]

        # print(entire_list)
        for start, finish in entire_list[1:]:

            if start <= pref:
                answer.append([max(pres, start), min(pref, finish)])
            pres, pref = min(start, pref), max(finish, pref)

        # print(answer)

        return answer

# solution 2 - two pointers - (7ms)  - (2025.03.30)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        i, j = 0, 0
        answer = []

        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            # 교집합 시작과 끝 계산
            start = max(a_start, b_start)
            end = min(a_end, b_end)

            # 실제 겹치는 구간이 있을 때만 추가
            if start <= end:
                answer.append([start, end])

            # 더 빨리 끝나는 구간을 다음으로
            if a_end < b_end:
                i += 1
            else:
                j += 1

        return answer