class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        def calculatelen(cnt):

            if cnt == 0: return 0
            elif cnt == 1: return 1
            elif cnt < 10 : return 2
            elif cnt < 100 : return 3
            else: return 4
        
        n = len(s)
        # dp[i][j]
        # 문자열의 첫 i개 문자까지 고려했을 때,
        # 최대 j개의 문자를 삭제함으로써 얻을 수 있는 
        # 최소 압축 길이로 설정
        dp = [[99999] * (k+1) for _ in range(n+1)]
        
        # 모든 j에 대해 0으로 초기화합니다. 
        # 문자열이 없는 경우, 압축 길이는 0
        for j in range(k+1):
            dp[0][j] = 0

        # dp[i][0]
        # 초기 문자열의 압축 길이로 설정
        # 여기서는 아무 문자도 삭제하지 않는다.


        # 문자열의 각 위치에 대해 최적의 압축 길이를 계산
        for i in range(1,n+1):
            for j in range(k+1):

                # cnt는 현재 위치에서 연속된 동일 문자의 수
                # remove는 삭제한 문자의 수
                cnt, remove = 0,0

                # 현재 문자를 삭제하는 경우
                if j > 0 :
                    dp[i][j] = dp[i-1][j-1]
                
                # 현재 위치에서 이전 위치까지 되돌아가며 최적의 압축 길이를 계산
                for p in range(i,0,-1):

                    # 동일한 문자가 나타나면 cnt 증가
                    if(s[p-1] == s[i-1]):
                        cnt += 1
                    
                    # 다른 문자가 나타나면 제거 카운트 증가
                    else:
                        remove += 1

                        # 제거 가능한 문자 수를 초과한 경우 중단
                        if remove > j : break
                    # 최소 압축 길이 계산
                    dp[i][j] = min(dp[i][j],dp[p-1][j-remove] + calculatelen(cnt))
        # print(dp)

        # 전체 문자열에 대한 최소 압축 길이 반환
        return dp[n][k]
        
