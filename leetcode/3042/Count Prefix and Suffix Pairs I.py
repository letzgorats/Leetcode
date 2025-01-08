class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(str1, str2):
            # endswith is also possible to use
            if str2.startswith(str1) and str2[len(str2) - len(str1):] == str1:
                return True

            return False

        answer = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):

                if isPrefixAndSuffix(words[i], words[j]):
                    answer += 1

        return answer