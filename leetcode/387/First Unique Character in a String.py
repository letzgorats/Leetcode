from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = defaultdict(int)

        for a in s:
            count[a]+= 1
    
        for idx,a in enumerate(s):
            if count[a] == 1:
                return idx

        return -1
        
