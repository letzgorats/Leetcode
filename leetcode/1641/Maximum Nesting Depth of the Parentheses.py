class Solution(object):
    def maxDepth(self, s):
      
        max_count = 0 
        cnt = 0
        stack = []

        for st in s:
            
            if stack and st == ")" and stack[-1] == "(":
                stack.pop()
                max_count = max(max_count, cnt)
                cnt -= 1
                
            elif st == "(":
                cnt += 1
                stack.append(st)
        
        max_count = max(max_count, cnt)

        return max_count
