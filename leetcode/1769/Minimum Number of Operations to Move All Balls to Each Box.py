# solution 1 - O(n^2)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        ball_exist = set()
        for i, box in enumerate(boxes):
            if box == '1':
                ball_exist.add(i)

        answer = [0] * len(boxes)
        for i in range(len(boxes)):

            for j in ball_exist:
                if i == j:
                    continue
                else:
                    answer[i] += abs(i - j)

        return answer

# solution 2 - prefix sum
class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        n = len(boxes)
        answer = [0] * n

        # 왼쪽에서 오른쪽으로 이동
        moves = 0
        balls = 0
        for i in range(n):
            answer[i] += moves
            balls += int(boxes[i])
            moves += balls

        # 오른쪽에서 왼쪽으로 이동
        moves = 0
        balls = 0
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            balls += int(boxes[i])
            moves += balls

        return answer