class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """

        MOD = 10 ** 9 + 7
        cur_pos = [1] * 10


        # move = {1:[6,8],2:[7,9],3:[4,8],4:[3,9,0],5:[],6:[1,7,0],7:[2,6],8:[1,3],9:[2,4],0:[4,6]}

        for jump in range(2,n+1):

            new_pos = [0] * 10


            new_pos[0] = (cur_pos[6] + cur_pos[4]) % MOD
            new_pos[1] = (cur_pos[6] + cur_pos[8]) % MOD
            new_pos[2] = (cur_pos[7] + cur_pos[9]) % MOD
            new_pos[3] = (cur_pos[4] + cur_pos[8]) % MOD
            new_pos[4] = (cur_pos[0] + cur_pos[3] + cur_pos[9]) % MOD
            new_pos[5] = 0  # Knight cannot move to position 5
            new_pos[6] = (cur_pos[0] + cur_pos[1] + cur_pos[7]) % MOD
            new_pos[7] = (cur_pos[2] + cur_pos[6]) % MOD
            new_pos[8] = (cur_pos[1] + cur_pos[3]) % MOD
            new_pos[9] = (cur_pos[2] + cur_pos[4]) % MOD

            cur_pos = new_pos
        
        total = sum(cur_pos) % MOD

        return total

        




        
