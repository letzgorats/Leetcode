# solution - count array : O(n^2)

class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0] * 1000000
        answer = 0
        nums = sorted(nums)
        # print(nums)

        for num in nums:

            if count[num] == 0 :
                count[num] += 1
            else:
                answer += abs(count.index(0,num) - num)
                count[count.index(0,num)] += 1
            # print(count,answer)
                
        return answer


# solution - O(nlogn)
class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        prev = nums[0]
        moves = 0

        for i in range(1,len(nums)):

            if nums[i] <= prev:

                prev += 1
                moves += prev-nums[i]

            else:
                prev = nums[i] 

        return moves
        
        
