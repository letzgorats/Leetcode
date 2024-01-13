class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in s:
            s_dict[i] = s_dict.get(i,0) + 1
        for j in t:
            t_dict[j] = t_dict.get(j,0) + 1
        
        cnt = 0
        for k,v in s_dict.items():
            if k in t_dict:
                if v == t_dict[k]:
                    cnt += v
                else:
                    cnt += min(v,t_dict[k])    
        
        return len(s)-cnt


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        sum = 0
        
        for n in count:
            if n > 0:
                sum += n

        return sum



