class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        one_cnt = bin(num2).count('1')

        answer = 0
        for i in range(31, -1, -1):  # 32bit 정수 기준
            if (num1 & (1 << i)) > 0:  # num1의 i번째 비트가 1인 경우
                if one_cnt > 0:
                    answer |= (1 << i)  # answer의 i번째 비트를 1로 설정
                    one_cnt -= 1

        # 아직 배치하지 못한 비트 1이 남아있다면, 낮은 자릿수부터 채운다.
        for i in range(32):
            # answer 의 i번째 비트가 0인 경우
            if one_cnt > 0 and (answer & (1 << i)) == 0:
                answer |= (1 << i)
                one_cnt -= 1

        return answer
