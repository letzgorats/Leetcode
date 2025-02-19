# solution 1 - backtracking, greedy (1091ms)
class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        happy_string = []

        def backtracking(cur, idx):

            if len(cur) == n:
                happy_string.append(cur)
                return
            if idx == n:
                return

            for j in range(idx + 1, n + 1):
                if cur == "":
                    backtracking(cur + "a", j)
                    backtracking(cur + "b", j)
                    backtracking(cur + "c", j)
                elif cur[-1] == "a":
                    backtracking(cur + "b", j)
                    backtracking(cur + "c", j)
                elif cur[-1] == "b":
                    backtracking(cur + "a", j)
                    backtracking(cur + "c", j)
                elif cur[-1] == "c":
                    backtracking(cur + "a", j)
                    backtracking(cur + "b", j)

        backtracking("", 0)
        if k > len(happy_string):
            return ""
        # print(happy_string)
        return happy_string[k - 1]



# solution 2 - backtracking, optimal code (3ms)
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0

        def backtracking(cur):
            nonlocal count

            if len(cur) == n:
                count += 1
                if count == k:
                    return cur  # k번째 happy_string 을 찾으면 즉시 반환
                return  # 아니면 계속 탐색

            for ch in "abc":
                if not cur or cur[-1] != ch:
                    res = backtracking(cur + ch)
                    if res:  # k번째 문자열을 찾았다면 즉시 리턴
                        return res

            return None  # k 번째 happy_string 을 찾지 못한 경우

        answer = backtracking("")

        return answer if answer else ""
