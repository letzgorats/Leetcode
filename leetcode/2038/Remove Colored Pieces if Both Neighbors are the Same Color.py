class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
    
        alice_win = 0
        bob_win = 0

        # AAABAABAAAABBBB

        for i in range(1,len(colors)-1):
            
            if colors[i-1] == 'A' and colors[i] == 'A' and colors[i+1] == 'A':
                alice_win += 1
            elif colors[i-1] == 'B' and colors[i] == 'B' and colors[i+1] == 'B':
                bob_win += 1
        
        return alice_win > bob_win 
