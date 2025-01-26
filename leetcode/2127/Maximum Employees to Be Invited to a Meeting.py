from collections import deque


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:

        n = len(favorite)
        indegree = [0] * n

        for person in range(n):
            indegree[favorite[person]] += 1

        # topological sorting to remove non-cycle nodes
        q = deque()
        for person in range(n):
            if indegree[person] == 0:
                q.append(person)

        depth = [1] * n  # depth of each node

        while q:
            current_node = q.popleft()
            next_node = favorite[current_node]
            depth[next_node] = max(depth[next_node], depth[current_node] + 1)
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)

        longest_cycle = 0
        two_cycle_invitations = 0

        # detect cycles
        for person in range(n):
            if indegree[person] == 0:
                continue

            cycle_length = 0
            current = person
            while indegree[current] != 0:
                indegree[current] = 0  # mark as visited
                cycle_length += 1
                current = favorite[current]

            if cycle_length == 2:
                # for 2-cycles, add the depth of both nodes
                two_cycle_invitations += depth[person] + depth[favorite[person]]
            else:
                longest_cycle = max(longest_cycle, cycle_length)

        return max(longest_cycle, two_cycle_invitations)