# solution 1 - heapq, greedy
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        q = []

        # 힙에 (개수,문자) 형태로 저장, 최대 힙을 위해 - 개수 사용
        if a > 0: heapq.heappush(q, (-a, 'a'))
        if b > 0: heapq.heappush(q, (-b, 'b'))
        if c > 0: heapq.heappush(q, (-c, 'c'))

        answer = []

        while q:

            # 제일 많이 남은 문자를 먼저 꺼냄
            first_count, first_char = heapq.heappop(q)

            if len(answer) >= 2 and answer[-1] == answer[-2] == first_char:
                # 만약 첫번째 문자가 연속으로 나올 수 없으면 두 번째 문자를 꺼냄
                if not q:
                    break  # 더 이상 문자가 없으면 종료

                second_count, second_char = heapq.heappop(q)
                answer.append(second_char)
                # 두 번째 문자를 사용하고 남은 개수 다시 힙에 넣음
                if -second_count - 1 > 0:
                    heapq.heappush(q, (second_count + 1, second_char))

                # 첫 번째 문자는 다시 힙에 넣음
                heapq.heappush(q, (first_count, first_char))

            else:
                # 첫 번째 문자를 사용할 수 있으면 결과에 추가
                answer.append(first_char)
                # 첫 번째 문자를 사용하고 남은 개수를 다시 힙에 넣음
                if first_count + 1 < 0:
                    heapq.heappush(q, (first_count + 1, first_char))

        return "".join(answer)

# TLE
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        answer = []
        a, b, c = a, b, c

        def backtracking(cur):

            if len(cur) > a + b + c:
                return

            if cur.count('a') > a or cur.count('b') > b or cur.count('c') > c:
                return

            if 'aaa' in cur or 'bbb' in cur or 'ccc' in cur:
                return

            backtracking(cur + 'a')
            backtracking(cur + 'b')
            backtracking(cur + 'c')
            answer.append(cur)

        backtracking("")
        answer.sort(key=len, reverse=True)
        # print(answer[0])

        return answer[0]