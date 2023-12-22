# first 
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        def make_answer(first,last):
            if first != last:
                answer.append(""+str(first)+"->"+str(last))
            else:
                answer.append(""+str(first))

        answer = []
        if nums == []:
            return []
        first = nums[0]
        last = nums[0]
        tmp = [first, last]

        for i in range(len(nums[:-1])):

            if nums[i] + 1 == nums[i+1]:
                tmp[1] = nums[i+1]
            else:
                make_answer(tmp[0],tmp[1])
                tmp[0] = nums[i+1]
                tmp[1] = nums[i+1]
            
        make_answer(tmp[0],tmp[1])

        return answer



        
# second

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:


        output = []
        
        for n in nums:
            
            if output and output[-1][1] == n-1:
                output[-1][1] = n
            else:
                output.append([n,n])
            
        return [f'{x}->{y}' if x!=y else f'{x}' for x,y in output]
