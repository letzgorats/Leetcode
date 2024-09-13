# TLE soultion
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        answer = []
        for a, b in queries:

            tmp = 0
            for i in range(a, b + 1):
                tmp ^= arr[i]

            answer.append(tmp)

        return answer

# solution - XOR ( a ^ a = 0)
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        prefix_xor = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        answer = []
        for a, b in queries:
            answer.append(prefix_xor[a] ^ prefix_xor[b + 1])

        return answer

        # prefix_xor[b+1] => arr[0]부터 arr[b]까지의 xor 값
        # prefix_xor[a] => arr[0]부터 arr[a-1]까지의 xor 값
        # prefix_xor[b+1] ^ prefix_xor[a] 를 하면, arr[a]부터 arr[b]까지의 XOR 값 (같은 값끼리는 xor 연산에서 0 이 되기 때문에)

        # (Ex) prefix_xor[4] = 1 ^ 3 ^ 4 ^ 8 = 14
        # (Ex) prefix_xor[1] = 1
        # prefix_xor[4] ^ prefix[1] = (1 ^ 3 ^ 4 ^ 8) ^ (1) = 3 ^ 4 ^ 8 ( 1^1 상쇄)
