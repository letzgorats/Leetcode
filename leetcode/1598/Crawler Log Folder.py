class Solution:
    def minOperations(self, logs: List[str]) -> int:

        now = 0

        for cmd in logs:

            if cmd[:-1] == '..':
                if now == 0:
                    now = 0
                else:
                    now -= 1
            elif cmd[:-1] == '.':
                continue
            else:
                now += 1

        return now