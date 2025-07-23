# greedy solution - O(n^2) - (2024.07.12)
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        answer = 0
        if x >= y:

            while 'ab' in s:
                tmp = s.split('ab')
                answer += (len(tmp) - 1) * x
                s = "".join(tmp)

            while 'ba' in s:
                tmp = s.split('ba')
                answer += (len(tmp) - 1) * y
                s = "".join(tmp)

        else:

            while 'ba' in s:
                tmp = s.split('ba')
                answer += (len(tmp) - 1) * y
                s = "".join(tmp)

            while 'ab' in s:
                tmp = s.split('ab')
                answer += (len(tmp) - 1) * x
                s = "".join(tmp)

        return answer

# O(n) - stack solution - (2024.07.12)
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove_pairs(s, first, second, point):

            stack = []
            total_points = 0

            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    total_points += point

                else:
                    stack.append(char)

            return "".join(stack), total_points

        if x > y:
            first, second, high, low = 'a', 'b', x, y
        else:
            first, second, high, low = 'b', 'a', y, x

        s, point1 = remove_pairs(s, first, second, high)
        s, point2 = remove_pairs(s, second, first, low)

        return point1 + point2

# solution 2 - (greedy,stack) - (184ms) - (2025.07.23)
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove_patterns(s, a, b, point):

            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    score += point
                else:
                    stack.append(ch)

            return ''.join(stack), score

        if x > y:  # remove 'ab'

            remaining, sc1 = remove_patterns(s, 'a', 'b', x)
            _, sc2 = remove_patterns(remaining, 'b', 'a', y)

        else:  # remove 'ba'

            remaining, sc1 = remove_patterns(s, 'b', 'a', y)
            _, sc2 = remove_patterns(remaining, 'a', 'b', x)

        return sc1 + sc2