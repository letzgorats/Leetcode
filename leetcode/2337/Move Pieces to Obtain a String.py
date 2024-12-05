class Solution:
    def canChange(self, start: str, target: str) -> bool:

        startChar = start.replace("_", "")
        targetChar = target.replace("_", "")

        if startChar != targetChar:
            return False

        Lstart = [i for i in range(len(start)) if start[i] == 'L']
        Lend = [i for i in range(len(start)) if target[i] == 'L']
        Rstart = [i for i in range(len(start)) if start[i] == 'R']
        Rend = [i for i in range(len(start)) if target[i] == 'R']

        for i, j in zip(Lstart, Lend):
            if i < j:
                return False

        for i, j in zip(Rstart, Rend):
            if i > j:
                return False

        return True