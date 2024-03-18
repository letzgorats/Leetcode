class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        # 1. 풍선 배열을 xend의 값에 따라 오름차순으로 정렬합니다. 
        # 이렇게 하면 가장 먼저 끝나는 풍선부터 처리할 수 있고, 화살이 다른 풍선에도 영향을 미칠 수 있는지 쉽게 판단할 수 있습니다.
   
        # 2. 배열을 순회하면서, 다음 풍선의 시작점이 현재 화살의 최대 도달 지점보다 큰 경우, 새로운 화살이 필요함을 의미하므로 화살의 수를 증가시키고, 
        #    현재 화살의 최대 도달 지점을 현재 풍선의 끝점으로 업데이트합니다.
      
        # 3. 모든 풍선을 처리할 때까지 이 과정을 반복합니다.

        points = sorted(points,key = lambda x:x[1])
        arrow = 1
        possible = points[0][1]

        for i in range(1,len(points)):

            if possible < points[i][0]:
                arrow += 1
                possible = points[i][1]
        

        return arrow
