# binary search solution

class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """

        position = sorted(position)

        min_dis = 1
        max_dis = position[-1] - position[0]
        result = 0

        def check(position, m, mid):

            current_pos = position[0]
            count = 1  # 첫 번째 볼은 이미 선택한 상태

            for i in range(1, len(position)):

                # 현재 위치에서 mid 이상의 거리에 다음 볼을 배치할 수 있는지 확인
                if position[i] - current_pos >= mid:
                    count += 1  # 볼을 배치
                    current_pos = position[i]

                    if count == m:
                        return True

            return False

        while min_dis <= max_dis:

            mid = (min_dis + max_dis) // 2
            if check(position, m, mid):
                result = mid
                min_dis = mid + 1
            else:
                max_dis = mid - 1

        return result

