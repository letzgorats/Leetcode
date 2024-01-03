class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        cur, pre = 0, 0
        answer = 0
        for i in bank:

            cur = i.count('1')
            if cur :
                answer += (pre * cur)
                pre = cur

        return answer


class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """

        board = []
        for row in bank:
            if '1' in row:  
                board.append(list(map(int,row)))

        n = len(board)

        answer = 0
        for i in range(n-1):
            a = board[i].count(1)
            b = board[i+1].count(1)
            answer += (a*b)

        return answer
        
