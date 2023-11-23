class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """

        # 0 - 2 -> 4 6 5 -> 4 5 6

        # 0 - 3 -> 4 6 5 9 -> (x)

        # 2 - 5 -> 5 9 3 7 -> 3 5 7 9

        answer = []

        for idx in range(len(l)):
            
            temp = sorted(nums[l[idx]:r[idx]+1])
            check = True
            # print(temp)
            diff = temp[1] - temp[0]
            for j in range(1,len(temp)):
                # print(temp[j] - temp[j-1])
                if diff != (temp[j] - temp[j-1]):
                    check = False
                    break


            if check:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer
