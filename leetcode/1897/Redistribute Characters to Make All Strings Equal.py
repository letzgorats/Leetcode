class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if len(words)==1:
            return True

        count = defaultdict(int)

        for word in words:
            for c in word:
                count[c] += 1

        for k,v in count.items():
            if v == 1:
                return False
            else:
                if v % len(words) != 0:
                    return False
        
        return True


class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """

        n = len(words)

        ans = ''.join(words)
        res = set(ans)

        for i in res:
            if ans.count(i) % n != 0:
                return False
        return True
