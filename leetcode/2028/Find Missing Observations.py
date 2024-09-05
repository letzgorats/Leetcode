class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

        m = len(rolls)
        total = m + n

        m_val = sum(rolls)
        n_val = (mean * total) - m_val

        answer = []
        if n <= n_val <= 6 * n:
            avg = n_val // n
            mod = n_val % n

            answer = [avg] * n

            for i in range(mod):
                answer[i] += 1

            return answer

        else:
            return []




