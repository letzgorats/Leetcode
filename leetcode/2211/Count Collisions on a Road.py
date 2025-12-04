# solution 1 - (strip,string,math) - (3ms) - (2025.12.04)
class Solution:
    def countCollisions(self, directions: str) -> int:
        dirs = directions.lstrip("L").rstrip("R")
        # print(dirs)

        return len(dirs) - dirs.count('S')

# solution 2 - (simulation) - (94ms) - (2025.12.05)
class Solution:
    def countCollisions(self, directions: str) -> int:

        i, j = 0, len(directions) - 1
        while i < len(directions) and directions[i] == 'L':
            i += 1
        while j >= 0 and directions[j] == 'R':
            j -= 1

        return sum(directions[k] != 'S' for k in range(i, j + 1))

