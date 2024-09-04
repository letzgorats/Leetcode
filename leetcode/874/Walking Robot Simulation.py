class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        max_distance = 0
        curx, cury = 0, 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 상 우 하 좌
        cur_dir = 0

        obstacles = set(map(tuple, obstacles))

        for cmd in commands:

            if cmd == -2:  # turn left

                cur_dir = (cur_dir - 1) % 4

            elif cmd == -1:  # turn right

                cur_dir = (cur_dir + 1) % 4

            else:  # move on

                for _ in range(cmd):
                    nx = curx + dirs[cur_dir][0]
                    ny = cury + dirs[cur_dir][1]
                    if (nx, ny) in obstacles:
                        break
                    else:
                        curx, cury = nx, ny

                max_distance = max(max_distance, curx ** 2 + cury ** 2)

        return max_distance % (2 ** 31)
