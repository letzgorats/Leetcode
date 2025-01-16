# solution 1 - math
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        m = len(nums2)
        ans = 0

        # num2 길이가 짝수,  nums1 길이가 짝수
        if m % 2 == 0 and n % 2 == 0:
            return ans
        # nums2 길이가 짝수, nums1 길이가 홀수
        elif m % 2 == 0 and n % 2 == 1:
            for num in nums2:
                ans ^= num
        # nums2 길이가 홀수, nums1 길이가 짝수
        elif m % 2 == 1 and n % 2 == 0:
            for num in nums1:
                ans ^= num
        # nums2 길이가 홀수, nums1 길이가 홀수
        elif m % 2 == 1 and n % 2 == 1:
            for num in nums1:
                ans ^= num
            for num in nums2:
                ans ^= num

        return ans

# TLE - greedy
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        nums3 = []
        for num1 in nums1:
            for num2 in nums2:
                nums3.append(num1 ^ num2)

        answer = 0
        for n in nums3:
            answer ^= n

        return answer
