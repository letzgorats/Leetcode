class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        ph = sorted(zip(positions, range(len(positions)), healths, directions))
        stack = []
        result = [0] * len(positions)

        for p, idx, h, d in ph:

            if d == "R":
                stack.append([idx, h])

            else:
                while stack and h > 0:

                    if stack[-1][1] < h:
                        stack.pop()
                        h -= 1
                    elif stack[-1][1] == h:
                        stack.pop()
                        h = 0
                    else:
                        stack[-1][1] -= 1
                        h = 0

                if h > 0:
                    result[idx] = h

        for idx, h in stack:
            result[idx] = h

        return [h for h in result if h > 0]
