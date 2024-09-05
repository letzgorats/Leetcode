# wrong answer
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

            if mod:
                for _ in range(n - 1):
                    answer.append(avg)

                if mod >= 6:
                    i = mod // 6
                    j = mod % 6
                    for k in range(i):
                        answer[k] = 6
                    answer.append(j)
                else:
                    answer.append(avg + mod)
            else:
                for _ in range(n):
                    answer.append(avg)

            return answer
        else:
            return []



# solution
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




