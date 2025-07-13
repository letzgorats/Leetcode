# solution 1 - (two pointers,sorting) - (72ms) - (2025.07.13)
from typing import List
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        n = len(players)
        m = len(trainers)

        players.sort()
        trainers.sort()
        cnt = 0

        i = j = 0
        while i < n and j < m:

            if players[i] <= trainers[j]:
                cnt += 1
                i += 1
                j += 1
            else:
                j += 1

        return cnt

