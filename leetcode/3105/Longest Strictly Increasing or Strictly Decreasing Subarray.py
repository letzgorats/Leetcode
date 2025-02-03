# solution 1
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        if nums[0] < nums[1]:
            flag = 'increasing'
            answer, length = 2, 2
        elif nums[0] > nums[1]:
            flag = 'decreasing'
            answer, length = 2, 2
        else:
            flag = 'both'
            answer, length = 1, 1

        for i in range(1, len(nums) - 1):

            if nums[i] < nums[i + 1]:
                if flag in ('decreasing' or 'both'):
                    length = 2
                else:
                    length += 1
                flag = 'increasing'
            elif nums[i] > nums[i + 1]:
                if flag in ('increasing' or 'both'):
                    length = 2
                else:
                    length += 1
                flag = 'decreasing'
            else:
                length = 1
                flag = 'both'

            answer = max(answer, length)

        return answer


# solution 2
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        inc, dec, answer = 1, 1, 1
        for i in range(1, len(nums)):

            if nums[i - 1] < nums[i]:
                inc += 1
                dec = 1
            elif nums[i - 1] > nums[i]:
                dec += 1
                inc = 1
            else:
                inc, dec = 1, 1

            answer = max(answer, inc, dec)

        return answer
