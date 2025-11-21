# solution 4 - (find,rfind) - (99ms) - (2025.11.21)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        substring = defaultdict(list)
        ans = 0
        uniq_s = set(s)
        for ch in uniq_s:
            st = s.find(ch)
            ed = s.rfind(ch)
            ans += len(set(s[st + 1:ed]))

        return ans

# solution 3 - (defaultdict,substring) - (139ms) - (2025.11.21)
from collections import defaultdict
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        substring = defaultdict(list)

        for i, ch in enumerate(s):
            substring[ch].append(i)

        ans = 0
        for ch in substring:

            if len(substring[ch]) < 2:
                continue

            st = substring[ch][0]
            ed = substring[ch][-1]

            ans += len(set(s[st + 1:ed]))

        return ans


# solution 2 - (defaultdict,substring) - (170ms) - (2025.01.04)
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


# solution 1 - (count,find) - (228ms) - (2023.11.14)
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
