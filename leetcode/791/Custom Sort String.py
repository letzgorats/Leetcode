from collections import Counter

class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """

        cnt = Counter(s)
      
        answer = ""
        for c in order:

            if c in s:
                answer += (str(c) * cnt[c])
                del cnt[c]

        for c in cnt:
            answer += "".join(str(c) * cnt[c])

        return answer
        
