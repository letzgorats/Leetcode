class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        original = [0] * len(derived)

        for idx in range(len(derived) - 1):

            if derived[idx] == 0:
                original[idx + 1] = original[idx]
            if derived[idx] == 1:
                if original[idx] == 1:
                    original[idx + 1] = 0
                elif original[idx] == 0:
                    original[idx + 1] = 1

        if derived[-1] == 0:
            if original[-1] == original[0]:
                return True
            else:
                return False

        elif derived[-1] == 1:
            if original[-1] != original[0]:
                return True
            else:
                return False

        return True

        # * 찾은 규칙 *
        # original = [a,b,c]
        # 라고 하면,
        # a ^ b == 1
        # -> 만약 a의 이진수의 일의자리가 0이라면 b는 a+1
        # -> 만약 a의 이진수의 일의자리가 1이라면 b는 a-1
        # -> ...
        # a ^ b == 0
        # -> a==b

# solution 2 - revised version
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original = [0] * len(derived)

        # `original` 배열을 유추
        for i in range(len(derived) - 1):
            original[i + 1] = original[i] ^ derived[i]  # XOR 성질로 계산

        # 원형 조건 검증
        return (original[-1] ^ original[0]) == derived[-1]
