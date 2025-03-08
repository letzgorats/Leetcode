# solution 1 - sliding window,count,greedy - (0ms) - (2025.03.08)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        window = blocks[:k]
        min_recolor = len(blocks)

        for i in range(len(blocks) - k + 1):
            window = blocks[i:i + k]
            recolor = window.count('W')
            if recolor == 0:
                return 0
            min_recolor = min(min_recolor, recolor)

        return min_recolor

# solution 2 - sliding window - (0ms) - (2025.03.08)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        recolor = blocks[:k].count('W')
        min_recolor = recolor

        # 슬라이딩 윈도우 적용
        for i in range(k, len(blocks)):
            # 이전 블록이 'W' 면 감소
            if blocks[i - k] == 'W':
                recolor -= 1
            # 새로운 블록이 'W'면 증가
            if blocks[i] == 'W':
                recolor += 1

            min_recolor = min(min_recolor, recolor)
            if min_recolor == 0:
                return 0

        return min_recolor