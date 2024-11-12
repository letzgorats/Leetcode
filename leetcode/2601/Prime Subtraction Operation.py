import math
# solution 1 - O (n * m * sqrt(m))
class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:

        def is_prime(n):
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        primes = [0, 0]  # 1 : not prime - False, 2 : not prime - False
        for i in range(2, max(nums)):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(primes[i - 1])

        prev = 0
        # O (n * m * sqrt(m))
        for i, n in enumerate(nums):
            upper_bound = n - prev  # non inclusive

            largest_p = primes[upper_bound - 1]

            if n - largest_p <= prev:
                return False
            prev = n - largest_p

        return True

# solution 2 - O (n + m * sqrt(m))
class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:

        def is_prime(n):
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False

            return True

        prev = 0
        # O (n + m * sqrt(m))
        for i, n in enumerate(nums):
            upper_bound = n - prev  # non inclusive

            largest_p = 0
            for i in reversed(range(2, upper_bound)):
                if (is_prime(i)):
                    largest_p = i
                    break

            if n - largest_p <= prev:
                return False

            prev = n - largest_p

        return True
