class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        seat_pos = []

        for idx,c in enumerate(corridor):

            if c == 'S':
                seat_pos.append(idx)
            
        if len(seat_pos)== 0 or len(seat_pos) % 2 != 0:
            return 0
        
        # print(seat_pos)
        answer = 1

        for i in range(1,len(seat_pos)-1,2):

            answer *= (seat_pos[i+1] - seat_pos[i])

        return answer % MOD


# another sol
class Solution:
    def numberOfWays(self, corridor):
        x = 1 # 0 seat
        y = 0 # 1 seat
        z = 0 # 2 seats
        for char in corridor:
            if char == 'S':
                x, y, z = 0, x + z, y
            else:
                x, y, z = x + z, y, z
        return z % (10**9+7) 
