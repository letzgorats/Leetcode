class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        n = len(dominoes)
        forces = [0] * n

        # 오른쪽으로 힘 전달
        force = 0
        for i in range(n):
            if dominoes[i] == "R":
                force = n
            elif dominoes[i] == "L":
                force = 0  # 오른쪽으로 미는 힘 즉시 차단
            else:
                force = max(force - 1, 0)
            forces[i] += force

        # print(forces)
        # 왼쪽으로 힘 전달(음수로 기록) -> 그래야 최종적으로 도미노 i 에 작용하는 힘이 forces[i] 에 저장되므로
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == "L":
                force = n
            elif dominoes[i] == "R":
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        # print(forces)

        result = []
        for f in forces:
            if f == 0:
                result.append('.')
            elif f > 0:
                result.append('R')
            else:
                result.append('L')

        return "".join(result)
