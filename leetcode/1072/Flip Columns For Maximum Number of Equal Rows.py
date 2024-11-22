from collections import defaultdict
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        pattern_count = defaultdict(int)

        for row in matrix:

            original = tuple(row)

            flipped = tuple(1-x for x in row)

            # 둘 중 하나를 패턴으로 선택
            pattern_count[original] += 1
            pattern_count[flipped] += 1
        # 가장 많은 패턴의 빈도를 반환
        return max(pattern_count.values())