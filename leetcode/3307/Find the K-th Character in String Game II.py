# TLE - 정방향
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:

        word = 'a'
        for o in operations:

            if o == 0:  # append a copy of word to itself
                word += word
            else:  # generate new string
                tmp = ""
                for w in word:
                    tmp += chr((ord(w) - ord('a') + 1) % 97 + 97)
                # print(tmp)
                word += tmp

            if len(word) >= k:
                break
            # print(word)

        return word[k - 1]


# solution1 - (역방향,math,bit manipulation) - (0ms) - (2025.07.04)
from typing import List
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:

        # 즉, 맨 마지막 연산부터 거꾸로 보며, k가 어느 쪽에서 왔는지 추적하면 된다.
        cnt = 0  # 변환 횟수
        n = len(operations)
        length = pow(2, n - 1)

        for i in range(n - 1, -1, -1):
            if k > length:  # 오른쪽 파트에서 온 것
                k -= length  # 오른쪽 파트는 length 뒤에 위치하므로 보정
                if operations[i] == 1:  # 오른쪽에 붙은 것 알파벳이 1만큼 변한 것이므로
                    cnt += 1
                    # 매번 길이를 반씩 줄여가면서, 이전 연산 전의 길이로 돌아간다.
            length //= 2

        # 최종적으로 cnt 번 변형되었으므로, 'a'에서 cnt 만큼 이동한 문자가 결과이다.
        return chr(ord('a') + (cnt % 26))

    '''
    k = 10 
    operations = [0,1,0,1]

    연산 순서(정방향)
    1. "a" -> append same -> "aa"
    2. -> append next_char("bb") -> "aabb"
    3. -> append same -> "aabbaabb"
    4. -> append n ext_char("bbccbbcc") -> "aabbaabbbbccbbcc"

    최종 문자열 "aabbaabbbbccbbcc", 길이 : 16 -> k=10 의 문자 "b"

    역추적(역방향)
    1. n = 4 -> length : 2^3 = 8
    2. i=3, k=10 > 8 -> 오른쪽 -> k=2, cnt=1(operation == 1)
    3. i=2, k=2 <= 4 -> 왼쪽 -> 그대로
    3. i=1, k=2 > 2 -> 왼쪽 -> 그대로
    4. i=0, k=2 > 1 -> 오른쪽 -> k=1, cnt=0

    최종 cnt = 1 -> char(ord('a')+1)-> "b"
    '''
