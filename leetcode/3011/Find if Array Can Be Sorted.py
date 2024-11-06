# solution 1- O(n)
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        def count_set_bits(a):
            return bin(a).count('1')

        # (이전 최댓값), (현재 구간의 최소값,최댓값)
        prevMax, currMin, currMax = float('-inf'), 0, 0  # 이전 구간의 최대값 초기화
        prevBit = -1  # 이전 비트 개수를 -1로 초기화

        for num in nums:
            bits = count_set_bits(num)
            if prevBit != bits:  # 비트개수가 다르면 새 그룹 시작
                # 현재 그룹의 최소값이 이전 그룹의 최대값보다 작으면 False
                if currMin < prevMax:
                    return False
                prevMax = currMax  # 이전 그룹의 최대값을 현재 그룹의 최대값으로 갱신
                currMin, currMax = num, num  # 새 그룹의 최소, 최대값을 현재 숫자로 초기화
                prevBit = bits  # 이전 비트 개수를 현재 비트 개수로 갱신
            else:
                currMin = min(currMin, num)  # 동일 비트 개수 구간에서 최소값 갱신
                currMax = max(currMax, num)  # 동일 비트 개수 구간에서 최대값 갱신

            # print(prevMax,"prevMax")
            # print(currMax,"currMax")
            # print(currMin,"currMin")

            print()
        return currMin >= prevMax  # 마지막 구간의 최소값이 이전 구간의 최대값 이상인지 확인


# solution 2 - O(n^2)
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        N = len(nums)

        def have_same_bits(a, b):
            return bin(a).count('1') == bin(b).count('1')

        for i in range(N - 1, 0, -1):
            for j in range(i):

                if have_same_bits(nums[j], nums[j + 1]) and nums[j + 1] < nums[j]:
                    # swap
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

            print(nums)

        return nums == sorted(nums)