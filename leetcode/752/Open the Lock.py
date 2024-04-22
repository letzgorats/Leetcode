from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)  # Convert to set for O(1) lookups
        queue = deque([('0000',0)])  # (current lock position, number of turns)
        visited = set('0000')   # Visited positions

        if '0000' in deadends:
            return -1
        
        while queue:

            position, turns = queue.popleft()

            if position == target:
                return turns
            
            for i in range(4):
                num = int(position[i])
                for move in (-1,1):
                    new_num = (num+move) % 10
                    new_position = position[:i] + str(new_num) + position[i+1:]
                    if new_position not in visited and new_position not in deadends:
                        visited.add(new_position)
                        queue.append((new_position, turns+1))
        
        return -1  # If no solution is found
