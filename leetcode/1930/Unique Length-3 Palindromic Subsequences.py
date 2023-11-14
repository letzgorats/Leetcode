class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """


        sub = defaultdict(list)

        for i,c in enumerate(s):
            
            sub[c].append(i)
            
        cnt = 0

        for element in sub:
            if len(sub[element]) < 2:
                continue
            a = sub[element][0]
            b = sub[element][-1]
            # between count
            cnt += len(set(s[a+1:b]))
        
        return cnt


class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """

        cnt = 0
        unq_str = set(s)

        for ch in unq_str:
            st = s.find(ch)
            ed = s.rfind(ch)

            if st < ed:
                cnt += len(set(s[st+1:ed]))
            
        return cnt
