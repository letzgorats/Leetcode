class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        
        if len(word1) != len(word2):
            return False
        
        if set(word1) != set(word2):
            return False

        word1_cnt = [0] * 26
        word2_cnt = [0] * 26

        for w in word1:
            word1_cnt[ord(w)-ord('a')] += 1
        for w in word2:
            word2_cnt[ord(w)-ord('a')] += 1

        word1_cnt.sort()
        word2_cnt.sort()

        return word1_cnt == word2_cnt
