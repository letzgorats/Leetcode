# dp solution
from collections import deque
class Solution(object):
    def findRotateSteps(self, ring, key):

        
        # the distance between two points (i, j) on the ring
        def dist(i, j):
            return min(abs(i - j), len(ring) - abs(i - j))

        # build the position list for each character in ring
        pos = {}
        for i, c in enumerate(ring):
            if c in pos: pos[c].append(i)
            else: pos[c] = [i]
        print(pos)
        
        # the current possible state: {position of the ring: the cost}
        state = {0: 0}
        for c in key:
            next_state = {}
            for j in pos[c]:  # every possible target position
                next_state[j] = float('inf')
                for i in state:  # every possible start position
                    next_state[j] = min(next_state[j], dist(i, j) + state[i])
            state = next_state
        return min(state.values()) + len(key)

# others solution
from collections import defaultdict

class Solution(object):
    def findRotateSteps(self, ring, key):

        memo = {}
        pos = defaultdict(list)
        
        for i,c in enumerate(ring):
            pos[c].append(i)
        
        def dp(index,ring_pos):
            # base_case : key의 모든 문자를 처리했을 때
            if index == len(key):
                return 0
            
            # memoziation check
            if (index,ring_pos) in memo:
                return memo[(index,ring_pos)]

            # 최소 단계 수 계산
            min_step = float('inf')
            target = key[index]
            for p in pos[target]:
                # 시계방향과 반시계방향 회전 계산
                clockwise = abs(p-ring_pos)
                anti_clockwise = len(ring) - clockwise
                rotate_step = min(clockwise, anti_clockwise)

                # 재귀적으로 다음 문자 처리
                step = rotate_step + 1 + dp(index+1, p)
                min_step = min(min_step,step)
            
            memo[(index,ring_pos)] = min_step
            return min_step

        return dp(0,0)


# wrong solution - not consider dp
from collections import deque
class Solution(object):
    def findRotateSteps(self, ring, key):

        
        clock = deque(list(ring))
        cnt = 0
        n = len(ring)

        for k in key:

            idx = list(clock).index(k)

            clockwise = idx
            anticlockwise = n - idx

            if clockwise <= anticlockwise:  # anti_clockwise
                cnt += clockwise # rotate
                clock.rotate(-clockwise)
            else:   # anti_clockwise
                cnt += anticlockwise # rotate
                clock.rotate(anticlockwise)
            cnt += 1 # press


        return cnt
