class Solution:
    
    def isHappy(self, n: int) -> bool:

        now = n
        pre = [n]

        def change(number):
            
            new = 0 
            for n in number:

                new += pow(int(n),2)
            
            return new
        
        while True:

            now = change(str(now))
            if now == 1:
                return True
            else:
                if now in pre:
                    return False
                pre.append(now)
