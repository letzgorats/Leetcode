class Solution(object):
    def sumSubarrayMins(self, arr):
      
        mod= 10 ** 9 + 7
        stack = []
        n = len(arr)

        # PLE :  각 요소에 대해 이전에 나오는 작은 요소의 인덱스를 저장
        ple = [0] * n
        # [0,0,0,0]

        # NLE :  각 요소에 대해 이후에 나오는 작은 요소의 인덱스를 저장
        nle = [0] * n
        # [0,0,0,0]


        # PLE 찾기
        for i in range(n):

            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            ple[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # print(ple)
        # ple = [-1,-1,1,2]
        # stack = [1,2,4]

        stack = []

        # NLE 찾기
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)

        # stack = []
        # print(nle)
            

        # 부분 배열의 최소값 합계 계산
        result = 0
        for i in range(n):
            result += arr[i] * (i - ple[i]) * (nle[i] - i)
        return result % mod

   
