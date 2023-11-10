from collections import defaultdict
class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        
        nums = defaultdict(set)

        # 1 -> 2
        # 2 -> 1, 3
        # 3 -> 2, 4
        # 4 -> 3

        for i,j in adjacentPairs:
            nums[i].add(j)
            nums[j].add(i)

        for node, adj in nums.items():
            if len(adj) == 1:
                break
        
        answer = [node]
        while nums[node]:

            cur = nums[node].pop()
            answer.append(cur)
            nums[cur].remove(node)
            node = cur

        return answer
