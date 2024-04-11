# 5.19 % 
class Solution(object):
    def removeKdigits(self, num, k):
      
        if k == 1 and len(num) == 1:
            return "0"

        answer = ""
        stack = []
        for idx in range(len(num)):
        
            while stack and int(stack[-1]) > int(num[idx]) and k!=0:
                stack.pop()
                k -= 1
            if k == 0:
                stack.extend(num[idx:])
                break
            stack.append(num[idx])

        answer = str(int(''.join(stack)))
    
        if k != 0:
            answer = answer[:-k]
        if answer == "":
            return "0"
            
        return answer

# same solution
class Solution(object):
    def removeKdigits(self, num, k):
        
        answer = ""
        stack = []
        for n in num:
        
            while stack and int(stack[-1]) > int(n) and k:
                stack.pop()
                k -= 1
            stack.append(str(n))

        while k:
            stack.pop()
            k -= 1
    
        if not stack:
            return "0"
        
        return str(int(''.join(stack)))
     

        
        
