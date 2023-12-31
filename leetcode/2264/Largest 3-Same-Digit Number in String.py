# solution 1 - 100%

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """

        case = [0,1,2,3,4,5,6,7,8,9]
        answer = -1
        for i in range(10):
            if str(case[i]) * 3 in num:
                answer = max(case[i],answer)
        
        if answer == -1:
            return ""
        else:
            return str(answer) * 3

# solution 2 - 76%

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """

        cnt = 0
        answer = -1
        for i in range(len(num)-1):
            
            if num[i] == num[i+1] :
          
                cnt += 1
                
            if cnt == 2:
        
                answer = max(int(num[i]),answer)
                cnt = 0

            elif num[i] != num[i+1]:
                cnt = 0 

            # print(cnt)

        if answer == -1 :
            return ""
        return str(answer) * 3
        
        
