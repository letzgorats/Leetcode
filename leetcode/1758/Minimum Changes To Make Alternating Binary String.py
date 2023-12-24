class Solution:
    def minOperations(self, s: str) -> int:
        
        def compare(case1,case2):

            cnt1, cnt2 = 0,0
            for i in range(n):
                if s[i] != case1[i]:
                    cnt1 += 1
            for i in range(n):
                if s[i] != case2[i]:
                    cnt2 += 1

            return min(cnt1,cnt2)

        n = len(s)
        if n == 1:
            return 0
        
        if n % 2 != 0:
    
            case1 = "01" * (n//2) + "0"
            case2 = "10" * (n//2) + "1"

            return compare(case1,case2)

        else:
            case1 = "01" * (n//2)
            case2 = "10" * (n//2)

            return compare(case1,case2)
