# solution 1 - vertical
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        answer = ""
        strs.sort(key=len)

        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return answer
            else:
                answer += strs[j][i]

        return answer
        # print(answer)
        # # ["flow","flight","flower"]

# solution 2 - horizontal
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        word1 = strs[0]
        end = 0

        for idx in range(len(word1)):
            for word in strs[1:]:
                if idx == len(word) or word1[idx] != word[idx]:
                    return word1[:end]
            end += 1

        return word1
