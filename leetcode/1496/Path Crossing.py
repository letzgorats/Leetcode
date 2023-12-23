class Solution:
    def isPathCrossing(self, path: str) -> bool:
        

        visited = [(0,0)]

        d = {'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}

        x,y = visited[-1]
        for p in path:    
            x += d[p][0]
            y += d[p][1]
            if (x,y) in visited:
                return True
            visited.append((x,y))

        return False


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        

        visited = [(0,0)]

        d = {'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}

        for p in path:
            x,y = visited[-1]
            visited.append((x + d[p][0] , y + d[p][1]))
        
        visited.sort()
        for i in range(len(visited)-1):

            if visited[i] == visited[i+1]:
                return True
                
        return False
        


            
