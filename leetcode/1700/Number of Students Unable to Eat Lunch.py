from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):

        queue = deque(students)
        cnt = 0
        while queue and cnt <= len(queue):

            pre = queue.popleft()
            if sandwiches[0] == pre:
                sandwiches.pop(0)
                cnt = 0
            else:
                queue.append(pre)
                cnt += 1

        if queue:
            return len(queue)

        return 0
