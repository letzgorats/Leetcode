# TLE1 - (copy,backtracking,dfs) - (TLE) - (2025.06.27)
from collections import defaultdict
import copy
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:

        ans = ""

        total_idx = defaultdict(list)
        for idx, ch in enumerate(s):
            total_idx[ch].append(idx)

        candi = set()

        def counting_alphabet(curr):

            trial = k
            total_tmp = copy.deepcopy(total_idx)
            curr_tmp = Counter(curr)

            for i, ch in enumerate(curr):
                if len(total_tmp[ch]) < k * curr_tmp[ch]:
                    return False

            tmp = []
            while trial > 0:
                for idx, ch in enumerate(curr):
                    if len(total_tmp[ch]) == 0:
                        return False
                    else:
                        tmp.append(total_tmp[ch].pop(0))
                # print(curr,tmp)
                if sorted(tmp) != tmp:
                    return False
                trial -= 1

            return True

            # l : 0,4 e : 1,5,6,11 t : 2,7

        def backtracking(idx, cur):
            nonlocal candi

            if len(s) - len(cur) * k >= 0 and counting_alphabet(cur):
                candi.add(cur)

            for i in range(idx, len(s)):
                backtracking(i + 1, cur + s[i])
                backtracking(i + 1, cur)

        backtracking(0, "")
        candi = sorted(candi, key=lambda x: (len(x), x))
        # print(candi)
        return candi[-1]

# solution 1 - (bfs) - (1979ms) - (2025.06.27)
from collections import Counter, deque
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:

        counts = Counter(s)
        valid_chars = [ch for ch in counts if counts[ch] >= k]

        if not valid_chars:
            return ""

        max_length = len(s) // k
        queue = deque([""])
        answer = ""

        candidates = sorted(valid_chars, reverse=True)

        def is_k_subsequence(t):

            # t*k 가 s 의 subsequence 인지 검사
            target = t * k
            i = 0
            for ch in s:
                if i < len(target) and ch == target[i]:
                    i += 1

            return i == len(target)

        while queue:

            cur = queue.popleft()
            for ch in candidates:
                nxt = cur + ch
                if is_k_subsequence(nxt):
                    if len(nxt) > len(answer) or (len(nxt) == len(answer) and nxt > answer):
                        answer = nxt
                    if len(nxt) < max_length:
                        queue.append(nxt)

        return answer


# TLE 2 - (dfs,backtracking) - (TLE) - (2025.06.27)
from collections import Counter
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        count = Counter(s)
        valid_chars = [ch for ch in count if count[ch] >= k]
        if not valid_chars:
            return ""

        valid_chars.sort(reverse=True)  # 사전순 큰 것 먼저 탐색
        max_len = len(s) // k
        ans = ""

        def is_k_subsequence(pattern):
            target = pattern * k
            i = 0
            for ch in s:
                if i < len(target) and ch == target[i]:
                    i += 1
            return i == len(target)

        def dfs(cur):
            nonlocal ans
            if len(cur) > max_len:
                return

            if is_k_subsequence(cur):
                if len(cur) > len(ans) or (len(cur) == len(ans) and cur > ans):
                    ans = cur

            for ch in valid_chars:
                dfs(cur + ch)

        dfs("")
        return ans
