# solution1 - (iterative,counter) -(7ms) - (2025.08.10)
from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        numbers = sorted(str(n))
        cnt = Counter(numbers)

        for i in range(32):
            if cnt == Counter(str(2 ** i)):
                return True

        return False


# solution 2 - (space optimization,precomputing,same logic,signature) - (0ms) - (2025.08.10)
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        def get_sign(num):
            sign = 1
            while num > 0:
                sign *= prime[num % 10]
                num //= 10
            return sign

        target_sign = get_sign(n)
        print(target_sign)

        for i in range(31):
            if get_sign(1 << i) == target_sign:
                return True

        return False


