# solution 1 - (modular,math) - (5ms) - (2025.11.25)
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0

        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            # print(length,remainder)
            if remainder == 0:
                return length

        return -1

'''
1) 111..11 (n개) 를 직접 만들지 않고, remainder만 mod k 범위에서 유지한다.
2) 가능한 나머지는 k개뿐 -> 최대 k 번만 돌면 반드시 사이클이 돌아온다.
3) remainder가 0 이 나오면 "111...1(n개)"가 k로 나누어 떨어진다.
'''