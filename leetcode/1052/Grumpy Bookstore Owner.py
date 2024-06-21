# sliding window solution - O(n) complexity -197ms
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        base = 0

        for i in range(len(grumpy)):

            if grumpy[i] == 0:
                base += customers[i]

        # print(base)

        # 첫 윈도우 추가 만족도 계산
        current_adds = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                current_adds += customers[i]

        max_adds = current_adds

        for i in range(minutes, len(customers)):

            if grumpy[i] == 1:
                current_adds += customers[i]
            if grumpy[i - minutes] == 1:
                current_adds -= customers[i - minutes]

            max_adds = max(current_adds, max_adds)

        return base + max_adds

# sliding window solution - O(n*m) complexity - 7181 ms
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        base = 0

        for i in range(len(grumpy)):

            if grumpy[i] == 0:
                base += customers[i]

        # print(base)
        answer = 0
        for i in range(len(grumpy) - minutes + 1):
            adds = 0
            for j in range(i, i + minutes):

                if grumpy[j] == 1:
                    adds += customers[j]

            # print(base+adds)
            answer = max(answer, base + adds)

        return answer
