class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        # bitwise-xor

        answer = [pref[0]]

        for idx in range(1,len(pref)):

            x = pref[idx] ^ pref[idx-1]
            answer.append(x)
            # print(x)

        return answer
