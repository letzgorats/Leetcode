# solution 1 - (greddy,min,math,max) - (131ms) -(2025.11.03)
from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        ans = 0
        i = 1
        last = [colors[0], 0]
        while i < len(colors):
            if last[0] == colors[i]:
                ans += min(neededTime[i], neededTime[last[1]])  # 삭제한 풍선
                if neededTime[i] >= neededTime[last[1]]:
                    # 남은 풍선
                    last[1] = i
            else:
                last = [colors[i], i]
            i += 1
            # print(i,last)
        return ans


# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/solutions/4463574/98-20-beats-intuitive-approach-easy-to-understand-python/
from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        if len(neededTime) <= 1:
            return 0

        cost = 0
        i,j = 0,1
        n = len(colors)

        while i < n and j < n:

            if colors[i] != colors[j]:

                if j- i >= 2:
                    i = j       # change standard
                    j += 1
                else: 
                    i += 1
                    j += 1
            
            else:
                if neededTime[i] <= neededTime[j] :

                    cost += neededTime[i]

                    if j- i >= 2:
                        i = j       # change standard
                        j += 1
                    else: 
                        i += 1
                        j += 1

                else:
                    cost += neededTime[j]
                    j += 1

        return cost


            
        # a b a a a [1,2,1,4,2]

        #       i j   
        # 1 + 1

        # a b a a b [1,2,4,1,2]

        #       i    j
        # 1 + 
        # a a b a a [1,2,3,4,1]
        #   i   j 
        # 1 + 2 + 

        # a a a b b b a b b b b [3,5,10,7,5,3,5,5,4,8,1]
        #             i j 
        # 3 + 5 + 5 + 3 +  

        # a a a a a a a a a a a a a a [1,3,6,5,4,5,4,4,2,8,3,10,6,6]
        #     i             j
        # 1 + 3 + 5 + 4 + 5 + 4 + 4 + 2 + 6 + 

# solution using function
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        if len(neededTime) <= 1:
            return 0

        def change_index(i,j):

            if j - i >= 2:
                i = j       # change standard
                j += 1

            else: 
                i += 1
                j += 1

            return i,j


        cost = 0
        i,j = 0,1
        n = len(colors)

        while i < n and j < n:

            if colors[i] != colors[j]:

                i,j = change_index(i,j)
            
            else:
                if neededTime[i] <= neededTime[j] :

                    cost += neededTime[i]
                    i,j = change_index(i,j)

                else:
                    
                    cost += neededTime[j]
                    # 어차피 현재 max neededTime 값은 i 위치에 있다.
                    # neededTime[i] 가 max time 이므로
                    # j만 단순히 증가 시켜도 비교하는데 문제 없다.
                    # 지금 현재 i 위치의 값보다 큰 값이 나오면, 
                    # 그 때 가서 i 값을 갱신하면 된다.
                    j += 1  

        return cost


# refactoring code
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) <= 1:
            return 0

        total_cost = 0
        max_cost = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                total_cost += min(neededTime[i], max_cost)
                max_cost = max(max_cost, neededTime[i])
            else:
                max_cost = neededTime[i]

        return total_cost
