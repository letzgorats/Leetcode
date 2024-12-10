from collections import Counter
# solution 1 - TLE
class Solution:
    def maximumLength(self, s: str) -> int:

        cnt = Counter(s)
        # print(cnt)
        if all(v == 1 for v in cnt.values()):
            return -1
        candi = set()

        def backtracking(cur, idx):

            if cur != []:
                candi.add("".join(cur[:]))

            for i in range(idx, len(s)):
                cur.append(s[i])
                backtracking(cur, i + 1)
                cur.pop()

        backtracking([], 0)

        # print(candi)
        answer = 0
        for letter in candi:
            x = len(letter)
            cnt = 0
            for i in range(len(s)):
                if s[i:i + x] == letter:
                    cnt += 1
                if cnt >= 3:
                    answer = max(answer, len(letter))
                    break

        return answer

# solution 2 - sliding window(168ms)
class Solution:
    def maximumLength(self, s: str) -> int:

        # 카운트 확인: 모든 문자가 3번 미만이면 -1 반환
        cnt = Counter(s)
        if all(v < 3 for v in cnt.values()):
            return -1

        n = len(s)

        # 긴 길이부터 탐색 - (바로 length 리턴하도록)
        for length in range(n, 0, -1):  # 길이 n부터 1까지 감소
            substr_cnt = Counter(s[i:i + length] for i in range(n - length + 1))
            # print(substr_cnt)
            # 조건을 만족하는 가장 긴 문자열 확인
            for sub, count in substr_cnt.items():
                # special substring(단일 문자로만 이루어진 경우)만 체크 and 3번 이상인지 체크
                if len(set(sub)) == 1 and count >= 3:
                    return length

        return -1


# solution 3 - sliding window(31ms)
from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:

        n = len(s)
        max_len = -1

        # 동일한 문자로 이루어진 substring의 길이를 저장하는 딕셔너리
        substr_freq = defaultdict(int)

        # 슬라이딩 윈도우 탐색
        for start in range(n):
            char = s[start]
            length = 0
            for end in range(start, n):

                if s[end] == char:
                    length += 1
                    substr_freq[(char, length)] += 1
                else:
                    break
                # 조건을 만족하는 가장 긴 길이 갱신
                if substr_freq[(char, length)] >= 3:
                    max_len = max(max_len, length)

        return max_len