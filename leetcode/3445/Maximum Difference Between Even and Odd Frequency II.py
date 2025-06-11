# solution 1 - (prefix sum,frequency) - (3022ms) - (2025.06.11)
# 이해 필요!! 이해 아직 못함
from collections import defaultdict
from math import inf

class Solution:
    def maxDifference(self, s: str, k: int) -> int:

        max_diff = -inf
        for odd_char in "01234":               # 홀수번 등장해야 할 문자
            for even_char in "01234":          # 짝수번 등장해야 할 문자
                if odd_char == even_char:
                    continue

                # 홀/짝 등장 횟수 조합별 최소 (a_count - b_count) 저장
                min_diff_by_parity = defaultdict(lambda: inf)
                # 누적 등장 횟수 리스트
                odd_prefix_count = [0]   # odd_char가 앞에서부터 몇 번 나왔는지 누적
                even_prefix_count = [0]  # even_char 누적

                left = 0  # 윈도우의 왼쪽 끝 포인터

                for right, char in enumerate(s):
                    # 오른쪽으로 한 글자씩 늘려가며 누적값 업데이트
                    odd_prefix_count.append(odd_prefix_count[-1])
                    even_prefix_count.append(even_prefix_count[-1])
                    if char == odd_char:
                        odd_prefix_count[-1] += 1
                    elif char == even_char:
                        even_prefix_count[-1] += 1

                    # 왼쪽 포인터를 가능한 한 밀어보자
                    while left <= right - k + 1 and \
                          odd_prefix_count[left] < odd_prefix_count[-1] and \
                          even_prefix_count[left] < even_prefix_count[-1]:

                        # 현재 왼쪽 지점의 (홀/짝) 여부
                        parity_key = (odd_prefix_count[left] % 2, even_prefix_count[left] % 2)
                        # 이 위치에서의 (odd - even) 값
                        current_diff = odd_prefix_count[left] - even_prefix_count[left]
                        # 최소값만 저장
                        min_diff_by_parity[parity_key] = min(min_diff_by_parity[parity_key], current_diff)

                        left += 1

                    # 지금 위치 (right)에서 반대 parity를 가진 left 지점을 찾음
                    current_key = (1 - odd_prefix_count[-1] % 2, even_prefix_count[-1] % 2)
                    current_diff = odd_prefix_count[-1] - even_prefix_count[-1]

                    if current_key in min_diff_by_parity:
                        max_diff = max(max_diff, current_diff - min_diff_by_parity[current_key])

        return max_diff