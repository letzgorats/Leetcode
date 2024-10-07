class Solution:
    def minSwaps(self, s: str) -> int:

        '''
        1. open bracket 개수 == close bracket 개수
        2. if close bracket appears first, it would be unbalanced.
        3. What we have to do is to find out this unbalanced case
            and swap the brackets with minimum frequency.

        '''
        close, max_close = 0, 0

        for c in s:

            if c == "[":
                close -= 1
            else:
                close += 1
            # 불균형의 최대치 추적
            # (이 최댓값을 통해 최대 몇 번의 swap이 필요한지 계산 할 수 있음)
            max_close = max(close, max_close)

        # 최대 불균형의 절반만큼 swap을 하면 문제가 해결 된다.
        # (왜냐하면 한번의 swap으로 2개의 불균형을 해결할 수 있기 떄문)
        return (max_close + 1) // 2