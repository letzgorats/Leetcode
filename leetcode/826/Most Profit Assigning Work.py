import heapq

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        q = []

        for diff, pro in zip(difficulty, profit):
            q.append((diff, pro))

        q = sorted(q, key=lambda x: x[0])
        worker = sorted(worker)
        # print(q)
        # print(worker)
        answer = 0
        i = 0
        max_pro = 0

        for w in worker:
            while i < len(difficulty) and q[i][0] <= w:
                max_pro = max(max_pro, q[i][1])
                i += 1

            # if i != 0:
            #     i -= 1
            answer += max_pro

        return answer

# TLE solution
import heapq


class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        q = []

        for diff, pro in zip(difficulty, profit):
            q.append((diff, pro))

        q = sorted(q, key=lambda x: x[0])
        # print(q)

        answer = 0
        for w in worker:
            max_p = 0
            for d, p in q:
                if w >= d:
                    max_p = max(max_p, p)
                else:
                    break
            answer += max_p

        return answer