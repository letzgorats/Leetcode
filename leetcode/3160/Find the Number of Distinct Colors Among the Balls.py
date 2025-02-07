from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        current = dict()
        color_cnt = defaultdict(int)
        answer = []
        distinct_colors = 0

        for ball, color in queries:

            if ball in current:
                prev_color = current[ball]
                color_cnt[prev_color] -= 1  # 기존색 제거
                if color_cnt[prev_color] == 0:
                    distinct_colors -= 1

            # 새로운 색 적용
            current[ball] = color
            if color_cnt[color] == 0:
                distinct_colors += 1
            color_cnt[color] += 1

            answer.append(distinct_colors)

        return answer