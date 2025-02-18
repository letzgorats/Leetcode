# solution 1 - backtracking (346ms)
class Solution:
    def smallestNumber(self, pattern: str) -> str:

        answer = ""
        inc = 1
        visited = [0] * 10  # 1~9 숫자 사용여부

        def backtrack(idx, cur):

            nonlocal answer

            if idx == len(pattern) + 1:
                if answer == "" or "".join(cur) < answer:
                    answer = "".join(cur)
                return

            for num in range(1, 10):  # 1 부터 9까지 숫자 선택 가능
                if visited[num]:  # 이미 사용한 숫자는 패스
                    continue

                # 첫 숫자이거나, 패턴을 만족하는 경우만 선택
                if idx == 0 or (pattern[idx - 1] == "I" and cur[-1] < str(num)) or (
                        pattern[idx - 1] == "D" and cur[-1] > str(num)):
                    cur.append(str(num))
                    visited[num] = 1
                    backtrack(idx + 1, cur)
                    cur.pop()
                    visited[num] = 0

        backtrack(0, [])

        return answer

# solution 2 - stack,greedy(0ms)
class Solution:
    def smallestNumber(self, pattern: str) -> str:

        stack = []
        answer = ""
        for idx, ch in enumerate(pattern + "I", start=1):

            stack.append(idx)
            if ch == "I":
                while stack:
                    answer += str(stack.pop())

        return answer