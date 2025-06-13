# solution - (binary search, greedy) - (408ms) - (2025l.06.13)
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        nums.sort()

        # 1 1 2 3 7 10

        def is_valid(guess):

            count = 0
            i = 0
            '''
            모든 인덱스를 훑어가며 그리디하게 쌍을 만든다.
                - 차이가 guess 이하이면 짝을 만들고 i+= 2
                - 아니면 i += 1
            (배열이 오름찬순 정렬되어 있으니까, 인접한 두 수의 차이가 바로 가장 작은 차이이다.)
            '''
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= guess:  # 어차피 nums 는 오름차순 배열
                    count += 1
                    i += 2  # 이 둘은 쌍이 됐으므로 건너뜀
                else:
                    i += 1  # 짝이 안됐으므로 다음으로 진행

            if count >= p:  # p 쌍 이상 만들 수 있으면
                return True

            return False

            # difference

        left = 0
        right = (nums[-1] - nums[0])
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):  # p쌍 이상 만들 수 있으면 mid 를 더 줄여보며 탐색
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

