# solution 1 - (greedy) - (0ms) - (2025.08.29)
class Solution:
    def flowerGame(self, n: int, m: int) -> int:

        # to be odd, even+odd OR odd odd+even
        odd1, even1 = 0, 0
        odd2, even2 = 0, 0

        if n % 2 != 0:
            odd1 = n // 2 + 1
            even1 = n // 2
        elif n % 2 == 0:
            odd1 = n // 2
            even1 = n // 2

        if m % 2 != 0:
            odd2 = m // 2 + 1
            even2 = m // 2
        elif m % 2 == 0:
            odd2 = m // 2
            even2 = m // 2

        return (odd1 * even2) + (even1 * odd2)


# solution 2 - (math) - (0ms) - (2025.08.29)
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # to be odd, even+odd OR odd odd+even
        # total pairs -> n * m
        # (even+odd), (even+even), (odd+odd), (odd+even)
        # we can select (even+odd), (odd+even) -> 2 parities

        return n * m // 2

'''
결론부터 말하자면, (홀,짝) + (짝,홀) 의 개수와 (홀,홀) + (짝,짝) 의 개수가 항상 같지는 않다.
두 수가 '모두 홀수' 일 때는 같지 않고 1개 차이가 난다. 다만, "홀수 합" 쌍의 개수는 언제나 [n*m // 2] 이다.

정확한 개수 식
    -> odd(n) = (n+1)//2
    -> even(n) = n//2
    -> "합이 홀수"쌍 = (홀,짝) + (짝,홀)
        = odd(n) * even(m) + even(n) * odd(m)
        -> 이를 전개하면 언제나 [n*m // 2]
    -> "합이 짝수"쌍 = (홀,홀) + (짝,짝)
        = odd(n) * odd(m) + even(n) * even(m)
        -> 이는 [n*m // 2]

'''