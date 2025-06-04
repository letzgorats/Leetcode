# solution 1 - (greedy,math) - (11ms) - (2025.06.04)
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:

        if numFriends == 1:
            return word

        res = ""
        length = len(word) - numFriends + 1
        for i in range(len(word)):
            temp = word[i:i + length]
            if temp > res:
                res = temp

        return res


'''
combinations(range(1, 50), 20)이 너무 많음
이 예시에도 우리가 자를 수 있는 위치는 1부터 49까지 총 49개고, 그 중 20개를 뽑는 경우의 수는:

C(49, 20) ≈ 4.7 × 10^12 로 이건 완전탐색으로 절대 못 구한다.
메모리 초과(MLE)도 아니고 사실상 시간초과(TLE)가 먼저 나야 정상이다.

해결전략?
-> 그리디 최적화

아이디어
-> numFriends개의 non-empty 조각을 만들면,
-> 그 중 어떤 조각도 최소 1자 이상, 따라서 가장 긴 조각의 길이는 len(word) - numFriends + 1 이하임.
-> 즉, 어떤 조각도 길이 len(word) - numFriends + 1보다 길 수 없음.
-> 그리고 박스에는 모든 split에서 나온 조각들이 다 들어가므로, 
-> 이 최대 길이를 갖는 모든 substring 중 가장 큰 것만 보면 된다.


-> "가장 긴 조각 길이" 를 정확히 제한할 수 있었기 떄문에, 완전 탐색 대신 슬라이딩 윈도우 방식으로 풀면 됐다.
-> 핵심은 "모든 split을 다 보지 않아도 된다. 어차피 가장 긴 조각 길이는 고정되어 있으니까!"
'''

