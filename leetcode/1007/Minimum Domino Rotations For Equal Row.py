# solution 1 - (greedy,top,bottom) - (23ms) - (2025.05.03)
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        if tops == bottoms:
            return 0

        n = len(tops)
        answer = n
        flag = False

        for i in range(1, 7):

            rotate_for_top = 0
            rotate_for_bottom = 0
            # tops 기준으로 바꿔보기
            for j in range(n):
                if tops[j] != i:
                    if bottoms[j] == i:
                        rotate_for_top += 1
                    else:
                        rotate_for_top = 0
                        break

                # bottoms 기준으로 바꿔보기
                if bottoms[j] != i:
                    if tops[j] == i:
                        rotate_for_bottom += 1
                    else:
                        rotate_for_bottom = 0
                        break

            if rotate_for_top != 0 and rotate_for_bottom != 0:
                answer = min(rotate_for_top, rotate_for_bottom)
                flag = True

        return answer if flag else -1


# solution 2 - (zip,len-max) - (19ms) - (2025.05.03)

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        for x in [tops[0], bottoms[0]]:

            if all(x in d for d in zip(tops, bottoms)):
                return len(tops) - max(tops.count(x), bottoms.count(x))

        return -1

'''
min 을 구할 때, 값이 변경될 때만 min 값 갱신을 비교하려고 하는 문제라면,
len-max 도 고려할 수 있다.
'''