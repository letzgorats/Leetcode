import copy

class Solution(object):

    

    def floodFill(self,image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        def search(image,r,c,value):
            
            paint[r][c] = True
            answer[r][c] = color

            for d in range(4):
                nr = r + dr[d] 
                nc = c + dc[d]
                if 0 <= nr < m and 0 <= nc < n:
                    if image[nr][nc] == value and paint[nr][nc] == False:
                        search(image,nr,nc,value)
                        
        answer = copy.deepcopy(image)

        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        m = len(image)
        n = len(image[0])

        paint = [[False] * n  for _ in range(m)]
        value = image[sr][sc]
        search(image,sr,sc,value)
        
     
