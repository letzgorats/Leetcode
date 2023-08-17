class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        State = {}
        def turn(left,right,player):

            if (left,right,player) in State : return State[(left,right,player)]
            if left > right :
                return 0

            if player:
                State[(left,right,player)] = max(nums[left] + turn(left+1,right,not player), nums[right] + turn(left,right-1,not player))
            else:
                State[(left,right,player)] = min(-nums[left] + turn(left+1,right,not player), -nums[right] + turn(left,right-1,not player))
            
            return State[(left,right,player)]
            
        return turn(0,len(nums)-1,True) >= 0 
