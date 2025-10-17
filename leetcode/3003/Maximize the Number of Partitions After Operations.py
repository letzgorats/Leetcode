# solution 1 - (string,dynaminc programming,bit manipulation,bitmask) - (39ms) - (2025.10.17)
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        # [num,mask,count]
        '''

        num : s[0:i] 구간 (즉, i 직전까지)은 그리디로 자를 때 완성된 파티션 개수
        mask : 현재 진행 중인(아직 확정 안 된) 마지막 파티션의 문자 집합(26비트 마스크)
        count : 그 집합의 서로 다른 문자 수 (mask.bit_count()와 같지만 저장해둠)

        '''
        left = [[0] * 3 for _ in range(n)]
        right = [[0] * 3 for _ in range(n)]

        # 1) 왼쪽에서 오른쪽으로: prefix 스캔

        num, mask, count = 0, 0, 0
        for i in range(n - 1):
            binary = 1 << (ord(s[i]) - ord("a"))
            if not (mask & binary):
                count += 1
                if count <= k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1
            left[i + 1][0] = num
            left[i + 1][1] = mask
            left[i + 1][2] = count

        # 2) 오른쪽에서 왼쪽으로: suffix 스캔
        num, mask, count = 0, 0, 0
        for i in range(n - 1, 0, -1):
            binary = 1 << (ord(s[i]) - ord("a"))
            if not (mask & binary):
                count += 1
                if count <= k:
                    mask |= binary
                else:
                    num += 1
                    mask = binary
                    count = 1
            right[i - 1][0] = num
            right[i - 1][1] = mask
            right[i - 1][2] = count

        max_val = 0
        for i in range(n):
            seg = left[i][0] + right[i][0] + 2
            tot_mask = left[i][1] | right[i][1]
            tot_count = bin(tot_mask).count("1")
            if left[i][2] == k and right[i][2] == k and tot_count < 26:
                seg += 1
            elif min(tot_count + 1, 26) <= k:
                seg -= 1
            max_val = max(max_val, seg)
        return max_val
'''
    - num, mask, count를 0으로 초기화.
    - for i in range(n - 1): **s[0..n-2]**까지 미리 계산해서 left[i+1]에 기록.
        - 이유: left[idx]는 “idx 직전까지 본 상태”를 담도록 하려는 패턴(즉, left[i]는 s[0:i-1]을 처리한 결과).

    - binary: 현재 문자 s[i]의 비트 (예: 'c'면 1<<2).

    - if not (mask & binary): 현재 진행 중 파티션에 처음 등장하는 문자라면

    -   count += 1: 구분자 수 증가

        - if count <= k: 아직 제한 이하면

            - mask |= binary: 집합에 추가하고 계속 같은 파티션 유지

        - else: 제한을 넘으면

            - num += 1: 직전에 파티션을 하나 확정하고

            - mask = binary; count = 1: 새 파티션을 현재 문자 하나로 시작

    - 마지막으로 left[i+1] = [num, mask, count] 저장
    → “i까지 처리했을 때, i+1 직전까지의 상태”가 채워짐
    (즉, left[pos]는 pos 왼쪽의 누적 상태라고 외워두면 편함)

    - 요약: left[i]는 **s[0..i-1]**을 그리디로 처리했을 때,

        - left[i][0]: 완성된 파티션 수

        - left[i][1]: 마지막 진행 중 파티션의 문자 집합 마스크

        - left[i][2]: 그 파티션의 distinct 수
    '''

'''
    - 이번엔 뒤에서 앞으로 스캔.

    - for i in range(n-1, 0, -1): s[n-1..1] 처리해서 right[i-1]에 기록.

        -  결과적으로 right[j]는 s[j+1..n-1](즉, j의 오른쪽 전부)을 그리디로 잘랐을 때 상태를 담음.

    - 로직은 위 prefix와 동일:

        - right[i-1][0]: 오른쪽에서 완성된 파티션 수

        - right[i-1][1]: 오른쪽 진행 중 파티션의 문자 집합 마스크

        - right[i-1][2]: 그 distinct 수

    - 요약: right[i]는 **s[i+1..n-1]**을 처리했을 때,

        - right[i][0]: 완성된 파티션 수

        - right[i][1]: 첫 진행 중 파티션(오른쪽 끝에서 보면 마지막)의 문자 집합

        - right[i][2]: 그 distinct 수
'''

'''
기본값 seg = left[i][0] + right[i][0] + 2

    - left[i][0]: i의 왼쪽을 이미 다 잘랐을 때 완성된 파티션 개수

    - right[i][0]: i의 오른쪽을 이미 다 잘랐을 때 완성된 파티션 개수

    - + 2: i를 기준으로 “왼쪽의 진행 중 파티션 1개” + “오른쪽의 진행 중 파티션 1개”를 기본적으로는 각각 하나의 파티션으로 본다는 뜻

        - 즉, ... [왼쪽-미완] | i(교체) | [오른쪽-미완] ...

        - 별다른 조건이 없으면, i를 중심으로 좌 1개, 우 1개가 생겨 총 +2가 더해짐

    - 이 +2는 “가장 보수적으로 잡은 기본 분할 수”라고 이해하면 돼요.
    - 이후 조건에 따라 더 쪼개져서 +1 될 수도 있고,
    - 반대로 두 미완 파트를 이어 붙여 -1 될 수도 있어요.
'''

'''
    - left[i][1]: 왼쪽 미완 파트의 문자 집합

    - right[i][1]: 오른쪽 미완 파트의 문자 집합

    - tot_mask: 두 집합 합집합

    - tot_count: 그 distinct 수
'''

'''(A) 좌/우가 각각 이미 k개로 꽉 찬 경우 + 합집합이 26 미만
   -  왼쪽 미완 파트의 distinct == k, 오른쪽도 == k → 양쪽 모두 더는 새 문자를 흡수 못함

    - 그런데 tot_count < 26이면, 양쪽 집합에 모두 없는 새 문자를 선택할 수 있음(26자 중 아직 안 쓴 게 있으니까)

    - 그 새 문자로 s[i]를 바꾸면:

        - 왼쪽은 이미 k라 i 직전에서 끊김

        - 오른쪽도 이미 k라 i에서 또 끊김

        - 그리고 i 한 글자 자체가 길이 1의 파티션으로 중간에 끼어듦

    - 즉, 기본 +2(좌1, 우1)에 중간 1개가 추가되어 seg += 1 → 총 +3이 됨
    - (그리디 규칙상, i가 좌/우 어느 쪽에도 흡수될 수 없으니 i 혼자 파티션으로 독립)

   (B) 좌/우를 아예 하나로 이어붙일 수 있는 경우 (합집합 + i가 k 이내)
    - tot_count는 좌/우 합집합 크기

    - +1은 i에 넣을 교체 문자 1개까지 고려한 distinct 수

    -  그 값이 k 이하면, 왼쪽 미완 + (바꾼 i) + 오른쪽 미완을 한 파티션으로 합칠 수 있음

    - 그러면 원래 기본값 +2(좌1, 우1)에서 둘을 합쳐 1개로 만들 수 있으니 -1

        - 결과적으로 i 주변은 +1만 추가되는 셈

    - 위 두 분기는 서로 배타적이에요.

        - (A)는 좌/우가 이미 꽉 차 있어서 i가 독립 1조각 더 만든다는 케이스

        - (B)는 반대로 i를 “접착제”로 써서 좌/우를 합쳐버리는 케이스
    
    - 모든 i(교체 위치 후보)에 대해 최대 파티션 수를 갱신하고, 최종 반환.
    

- left[i] = i 왼쪽까지의 결과, right[i] = i 오른쪽부터의 결과를 각 1패스로 미리 계산.

- i를 바꿀 때, i를 중심으로 생길 수 있는 기본 분할은 좌1 + 우1 = +2.

- 그런데

    - 좌/우가 이미 k개로 꽉 찼고 i를 새로운 문자로 바꿀 수 있으면, i 혼자 중간 파티션 1개 추가 → +3 (그래서 seg += 1)

    - 반대로, 좌/우 합집합에 i까지 넣어도 k 이내면 좌/우를 하나로 합침 → +1 (그래서 seg -= 1)

- 이 논리로 각 i를 평가해서 최댓값을 취함.

- 비트마스크를 쓰는 이유는 서로 다른 문자 집합을 O(1)로 합치고(OR),
- bit_count()로 크기를 O(1)에 구하려고예요.
- 덕분에 전체가 O(n) 으로 돌아갑니다.
'''