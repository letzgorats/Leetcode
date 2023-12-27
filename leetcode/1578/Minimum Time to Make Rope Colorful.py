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
