# TLE
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        # forward : 1, backward : 0
        s = list(s)
        for start, ends, d in shifts:

            tmp = list(s[start:ends + 1])

            if d == 1:  # forward
                for idx, letter in enumerate(tmp):
                    tmp[idx] = chr(97 + (ord(letter) - 97 + 1) % 26)

            else:  # backward
                for idx, letter in enumerate(tmp):
                    tmp[idx] = chr(97 + (ord(letter) - 97 - 1) % 26)
            s[start:ends + 1] = tmp

        return "".join(s)

# solution 1 - prefix sum
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        # 변화량을 저장할 배열 생성
        n = len(s)
        shift_arr = [0] * (n + 1)

        # 누적 변화량 계산
        for start, end, direction in shifts:
            if direction == 1:  # forward
                shift_arr[start] += 1
                shift_arr[end + 1] -= 1
            else:  # backward
                shift_arr[start] -= 1
                shift_arr[end + 1] += 1

        # 누적합을 통해 각 문자에 적용할 총 변화량 계산
        for i in range(1, n):
            shift_arr[i] += shift_arr[i - 1]

        answer = []
        for idx, letter in enumerate(s):
            shift = shift_arr[idx] % 26
            new_char = chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
            answer.append(new_char)

        return "".join(answer)