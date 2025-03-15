# solution 1 - binary search - (363ms) - (2025.03.15)
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def is_valid(threshold):

            cnt, i = 0, 0
            while i < len(nums):
                if nums[i] <= threshold:
                    cnt += 1
                    i += 1  # 다음 원소를 반드시 건너뛰어야 함.
                i += 1  # index 증가

            if cnt >= k:
                return True
            return False

        left, right = min(nums), max(nums)
        answer = 0
        while left <= right:

            mid = (left + right) // 2
            # 최댓값이 될 수 있는 원소의 최소값을 mid로 하는
            # 비연속적인 k 개의 원소를 선택할 수 있다면
            if is_valid(mid):
                answer = mid
                right = mid - 1
            else:  # 너무 작은 값을 찾는 것이므로 left 이동
                left = mid + 1

        return answer

'''
min,max 는 거의 binary search 로 풀 수 있을 것 같다.
'''