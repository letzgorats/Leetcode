# solution 1 - O(n^2)
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        if k == 0:
            return [0] * len(code)

        answer = [0] * len(code)
        if k > 0:
            for i in range(len(code)):
                tmp = 0
                for j in range(1, k + 1):
                    if (i + j) >= len(code):
                        tmp += code[(i + j) % len(code)]
                    else:
                        tmp += code[i + j]

                answer[i] = tmp

            # print(answer)

        else:
            for i in range(len(code)):
                tmp = 0
                for j in range(1, -k + 1):
                    if (i - j) < 0:
                        tmp += code[i - j]
                    else:
                        tmp += code[i - j]

                answer[i] = tmp

            # print(answer)

        return answer

# solution 2 - O(n)
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        if k == 0:
            return [0] * len(code)

        n = len(code)
        extended = code + code
        answer = [0] * n
        # [5,7,1,4,5,7,1,4]
        if k > 0:
            window_sum = sum(extended[1:k + 1])
            for i in range(n):
                answer[i] = window_sum

                window_sum += extended[i + k + 1] - extended[i + 1]

        else:
            k = -k
            window_sum = sum(extended[n - k:n])
            for i in range(n):
                answer[i] = window_sum

                window_sum += extended[i] - extended[i + n - k]

        return answer