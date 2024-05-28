# sliding window 1
class Solution(object):
    def equalSubstring(self, s, t, maxCost):

        tmp = []
        cnt = 0
        max_len = 0
        for i in range(len(s)):

            diff = abs(ord(t[i])-ord(s[i]))
            cnt += diff
            tmp.append(diff)
            while tmp and cnt > maxCost:
                cnt -= tmp.pop(0)
            max_len = max(len(tmp),max_len)   
        
        return max_len
      
# slidiing window 2, not using list

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
 
        l = 0
        cnt = 0
        max_len = 0
        for r in range(len(s)):

            cnt += abs(ord(t[r])-ord(s[r]))
            while cnt > maxCost:
                cnt -= abs(ord(t[l])-ord(s[l]))
                l += 1

            max_len = max(max_len,r-l+1) 
        
        return max_len
