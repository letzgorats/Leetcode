# solution 1
class Solution(object):
    def relativeSortArray(self, arr1, arr2):

        answer1, answer2 = [], []
        leftover = sorted(list(set(arr1)-set(arr2)))

        for a in arr1:
            if a in leftover:
                answer2.append(a)

        answer2 = sorted(answer2)

        for a2 in arr2:
            for a1 in arr1:
                if a2 == a1 :
                    answer1.append(a1)


        return answer1 + answer2


# solution 2

from collections import Counter

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        index_table = {v:i for i,v in enumerate(arr2)}

        sorted_arr1 = sorted(arr1,key=lambda x:(0,index_table[x]) if x in index_table else (1,x))

        return sorted_arr1
