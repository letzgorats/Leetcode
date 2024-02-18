import heapq
class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """

        # sort meetings based on start times
        meetings = sorted(meetings,key=lambda x:x[0])

        rooms_usage = [0] * n
        queue = []
        available_rooms = [i for i in range(n)]
        heapq.heapify(available_rooms)

    
        for s, e in meetings:
            
            # 현재 회의 시작 시간 전에 끝나는 모든 회의를 처리
            while queue and queue[0][0] <= s:
                t,r = heapq.heappop(queue)
                heapq.heappush(available_rooms,r)
                
            if available_rooms:
                # 사용 가능한 회의실이 있다면, 가장 번호가 낮은 회의실 할당
                r = heapq.heappop(available_rooms)
                heapq.heappush(queue,[e,r])

            else:
                # 사용 가능한 회의실이 없다면, 가장 먼저 끝나는 회의실 재할당
                t, r = heapq.heappop(queue)
                heapq.heappush(queue,[t + e-s,r])
            
            # 회의실 사용 횟수 증가 및 진행 중인 회의에 추가
            rooms_usage[r] += 1


        # 가장 많이 예약된 회의실 번호 반환
        return rooms_usage.index(max(rooms_usage))

            



