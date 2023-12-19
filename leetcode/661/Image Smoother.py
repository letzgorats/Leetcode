class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        
        n = len(img)
        m = len(img[0])
        answer = [[0]*m for _ in range(n)]

        # top-left, top, top-right, right, 
        # bottom-right, bottom, bottom-left, left
        dr = [-1,-1,-1,0,1,1,1,0]
        dc = [-1,0,1,1,1,0,-1,-1]

        for r in range(n):
            for c in range(m):
                val = img[r][c]
                cnt = 1
                for d in range(8):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr <  n and 0 <= nc < m :
                        cnt += 1 
                        val += img[nr][nc]
                answer[r][c] = (val / cnt)
        
        return answer
                
    
