# wrong answer
from typing import List
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        # build the histogram
        n = len(mat)
        m = len(mat[0])

        def countRectangle(h, w):
            dp = [[0] * (w + 1) for _ in range(h + 1)]
            print(dp)
            tmp = 0
            for i in range(h):
                for j in range(w):
                    if mat[i][j] > 0:
                        dp[i + 1][j + 1] = 1 + min(
                            dp[i][j],
                            dp[i + 1][j],
                            dp[i][j + 1]
                        )
                        tmp += dp[i + 1][j + 1]

            # print(tmp)
            return tmp

        ans = 0
        height = 1
        while height <= n:
            ans += countRectangle(height, m)

            height += 1
            # print("ans", ans)
        return ans


# solution 1 - (O(n*m*m),greedy) - (333ms) - (2025.08.21)
from typing import List
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        n = len(mat)
        m = len(mat[0])
        heights = [0] * m
        ans = 0

        for i in range(n):
            # 히스토그램 갱신
            for j in range(m):
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0

            # 이 행(i)을 바닥으로 하는 직사각형 개수 합산
            #   j 를 오른쪽 끝으로 두고 왼쪽으로 확장하며, 최소 높이를 유지
            min_h = 0
            for j in range(m):
                if heights[j] == 0:
                    continue
                min_h = heights[j]
                # 왼쪽으로 확장
                k = j
                while k >= 0 and heights[k] > 0:
                    min_h = min(min_h, heights[k])
                    ans += min_h
                    k -= 1

        return ans


'''
(i,j) 를 오른쪽 아래 꼭짓점으로 하는 모든 직사각형의 높이는 "j...k 구간의 최소 높이" 이고,
그 개수만큼 더해주면 된다.
'''


# solution 2 - (O(n*m),monotonic stack) - (35ms) - (2025.08.21)
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        n = len(mat)
        m = len(mat[0])
        col_heights = [0] * m
        ans = 0

        for i in range(n):
            # 1) 현재 행을 바닥으로 히스토그램 갱신
            for j in range(m):
                col_heights[j] = col_heights[j] + 1 if mat[i][j] == 1 else 0

            # 1) 단조 증가 스택(monotonic stack) - (minHeight, span)
            # "이 행에서 끝나는"직사각형 수 합산
            stack = []
            row_sum = 0
            for j in range(m):
                # 현재 막대 높이
                curHeight = col_heights[j]
                cnt = 1

                # 현재 높이보다 크거나 같은 구간은
                # 이제 최소 높이가 curHeight로 떨어지므로 기여를 빼고 폭을 합친다.
                while stack and stack[-1][0] >= col_heights[j]:
                    h_prev, span_prev = stack.pop()
                    row_sum -= (h_prev * span_prev)
                    cnt += span_prev

                row_sum += col_heights[j] * cnt
                stack.append((col_heights[j], cnt))
                ans += row_sum

        return ans


'''
row_sum 은 "이 행을 바닥으로 하여 열 j 까지 고려했을 떄의 모든 직사각형 수" 이다.
스택에는 (막대높이, 그 높이가 유지되는 연속 구간의 폭 기여)를 저장한다. 
더 낮은 막대를 만나면, 더 높은 막대들의 기여를 빼고 병합한다.
'''


"""
(ex) 
1 0 1
1 1 1

Q) 왜 히스토그램으로 바꾸는가?
A) 직사각형을 세는 핵심 아이디어는 "각 행을 바닥으로 보고 세자" 이다.
    예를 들어 두 번째 행까지 본 상태라면, 각 열에 대해 “위로 연속된 1의 개수(=히스토그램 높이)”를 기록한다.
    행 0 기준 heights: [1, 0, 1]
    행 1 기준 heights: [2, 1, 2]
    즉, 행별로 "히스토그램 막대 그림"을 그려놓고, 그걸로 직사각형을 세는 것이다.
    
Q) 왜 스택/왼쪽확장을 쓰는가?
A) 히스토그램을 보면, "이 열을 오른쪽 끝으로 하는 직사각형 수"는 왼쪽으로 가면서 
   최소 높이가 얼마나 유지되는지에 따라 결정된다.
   
   열 j 를 끝으로 하는 직사각형의 조건을 살펴보자.
   열 j 에서 높이가 h 라면, 직사각형의 '세로 길이는 h 이하만 가능'하다.
   그런데, 가로로 확장해서 열 (j-1), (j-2), ... 를 포함하려면, 그 구간의 모든 열이 '높이>=h'이어야 직사각형이 유지된다.
   
   즉, 왼쪽으로 확장된 구간의 세로 길이 = min(해당 구간 높이들)
    
    예시 : heights = [2,1,2]
        -> j = 0 : 최소 높이 2 -> 직사각형 2개
            
        -> j = 1 : 왼쪽으로 확장 : [1] -> 높이 1 -> 1개 / [2,1] -> 최소 높이 -> 1개 =>  총 2개
            
        -> j = 2 : 왼쪽으로 확장 : [2] -> 2개 / [1,2] -> 최소=1 -> 1개 / [2,1,2] -> 최소=1 -> 1개 =>  총 4개
            (ex)
            -> 구간 [2] : min = 2 -> (가능한 직사각형 : 높이 2짜리 2개 - (2x1), (1x1) ) 
            -> 구간 [1,2] : min = 1 -> (가능한 직사각형 : 높이 1짜리 1개 - (2x1), (1x1) ) 
            -> 구간 [1,2,1] : min = 1 -> (가능한 직사각형 : 높이 1짜리 1개 - (1x3) )
            여기서 직사각형의 세로 길이가 그 구간의 최소 높이로 제한되기 때문에, 'min'이 핵심이다.
            
    그래서 이 행에서 끝나는 직사각형이 총 8개인 셈이다.
    스택을 쓰면 이 "왼쪽으로 확장하면서 최소 높이 찾기"를 빠르게 처리할 수 있는 장점이 있다.
    
    wrong answer 의 코드에서 
        -> dp[i+1][j+1] = 1 + min(dp[i][j], dp[i+1][j], dp[i][j+1]) 는 정사각형만 센다.
        -> 직사각형은 세로로 길쭉하게 늘어날 수도 있는데, 그걸 전혀 카운트하지 못한 셈이다.
        
"""