class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        goal = [1,2,3,4,5,0]
        '''
        0 1 2
        3 4 5 --> 0 can go to {1, 3}

        1 0 2
        3 4 5 --> 0 can go to index of {0,2,4}

        1 2 0
        3 4 5 --> 0 can go to {1, 5}

        1 2 3
        0 4 5 --> 0 can go to {0,4}

        1 2 3
        4 0 5 --> 0 can go to {1, 3, 5}

        1 2 3
        4 5 0 --> 0 can go to {2, 4}
        '''
        swaps = {
            0 : [1,3],
            1 : [0,2,4],
            2 : [1,5],
            3 : [0,4],
            4 : [1,3,5],
            5 : [2,4]
        }
        board = board[0] + board[1]
        # print(board)
        empty_idx = board.index(0)
        q = deque([(board, 0 , empty_idx)])
        # Lists are unhashable types, so we need to convert a list to a tuple, which is immutable.
        visited = set([tuple(board)])

        while q :

            board, moves, empty_idx = q.popleft()
            if board == goal:
                return moves
            for j in swaps[empty_idx]:
                nxt = board[:]
                # 이동
                nxt[empty_idx] , nxt[j] = nxt[j], nxt[empty_idx]
                # 새로운 배열형태라면
                if tuple(nxt) not in visited:
                    visited.add(tuple(nxt))
                    q.append((nxt,moves+1,j))

        return -1