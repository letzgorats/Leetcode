# solution 1
from collections import defaultdict
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True

        a = defaultdict(list)
        b = defaultdict(list)
        for i in range(len(s1)):
            a[s1[i]].append(i)
            b[s2[i]].append(i)

        if a.keys() != b.keys():
            return False

        should_a = []
        should_b = []
        cnt = 0

        for i in range(26): # a~z 까지 체크

            # 각 알파벳에 해당하는 인덱스 개수가 다르면, False
            if len(a[chr(97 + i)]) != len(b[chr(97 + i)]):
                return False
            # 각 알파벳에 해당하는 인덱스 모음이 다르면, 체크 필요
            if a[chr(97 + i)] != b[chr(97 + i)]:

                # 다른 부분의 길이만큼 cnt 증가(최대 2번까지 허용-1번만 swqp 해야 하므로, 총 알파벳 2개)
                cnt += len(list(set(b[chr(97 + i)]) - set(a[chr(97 + i)])))
                if cnt > 2:  # 최대 한번만 스왑 가능(2번 초과면 False)
                    return False

                # should_a 와 should_b 가 비어 있으면
                if not should_a and not should_b:
                    # b 여야만 하는 should_b 와 a 여야만 하는 should_a 를 정해준다.
                    should_b = list(set(a[chr(97 + i)]) - set(b[chr(97 + i)]))
                    should_a = list(set(b[chr(97 + i)]) - set(a[chr(97 + i)]))

                # 이미 should_a 와 should_b 가 정해져 있다면, 해당 인덱스가 맞는지 검사
                else:
                    # 다르면, False 반환
                    if should_b == list(set(b[chr(97 + i)]) - set(a[chr(97 + i)])) and should_a != list(
                            set(a[chr(97 + i)]) - set(b[chr(97 + i)])):
                        return False

        # 그 외 모든 경우 True
        return True


# solution 2
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True

        # 다른 위치 저장
        diff = [(i, s1[i], s2[i]) for i in range(len(s1)) if s1[i] != s2[i]]

        # 다른 자리가 2개여야만 한다. 그 외는 False
        if len(diff) == 2:
            return False

        # 스왑이 가능한지 체크
        return diff[0][1] == diff[1][2] and diff[0][2] == diff[1][1]

