# solution 1 - (math,diff,max,min,difference,0,1) - (0ms) - (2025.06.15)
class Solution:
    def maxDiff(self, num: int) -> int:

        s = str(num)

        # max_num: replace first non-9 digit with 9
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = num  # all digits are 9

        # min_num: first digit should not be 0, so replace first non-1 digit
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for ch in s[1:]:
                if ch not in ('0', s[0]):
                    min_num = int(s.replace(ch, '0'))
                    break
            else:
                min_num = num

        return max_num - min_num


'''

앞자리가 이미 '1'이면, 그 숫자는 더 작게 만들 수 없어.

그래서 그 다음 자리들 중에서, 0이나 1이 아닌 숫자가 있으면 그걸 0으로 바꿔서 작게 만든다.


s = '1019'
s[0] = '1' → 건너뜀

s[1:] = '019'

→ ch = '0' → 건너뜀
→ ch = '1' → 건너뜀
→ ch = '9' → 바꾼다!

s.replace('9', '0') → '1010'
min_num = 1010

'''

