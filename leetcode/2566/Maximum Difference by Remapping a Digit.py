class Solution:
    def minMaxDifference(self, num: int) -> int:

        existing = set(list(map(int, str(num))))

        max_num, min_num = num, num
        for i in existing:
            for j in range(0, 10):  # 0~9
                if i != j:
                    x = int(str(num).replace(str(i), str(j)))
                    max_num = max(max_num, x)
                    min_num = min(min_num, x)

        return max_num - min_num