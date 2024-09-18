# solution
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(str,nums))
        # nums.sort(reverse=True)
        # n = max(map(len,nums))

        nums = sorted(nums,key=lambda x : x*10,reverse=True)

        if int(''.join(nums)) == 0:
            return "0"

        return "".join(nums)


# wrong solution
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(str,nums))
        n = max(map(len,nums))

        nums = sorted(nums,key=lambda x :(x.ljust(n,x[-1])),reverse=True)

        if int(''.join(nums)) == 0:
            return "0"
        return "".join(nums)


