# solution 1 - (heapq) - (1184ms) - (2024.02.18)
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

            

# solution 2 - (heapq) - (235ms) - (2025.07.11)
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        print(meetings)

        # q1 : 방 번호 minHeap
        q1 = [i for i in range(n)]

        # q2 : 방 번호와 끝나는 시간 체킹 minHeap
        q2 = []
        meeting_count = [0] * n

        for idx, (start, ends) in enumerate(meetings):

            while q2 and q2[0][0] <= start:
                _, room_number = heapq.heappop(q2)
                heapq.heappush(q1, room_number)

            if q1:
                room_number = heapq.heappop(q1)
                heapq.heappush(q2, [ends, room_number])
            else:
                room_available_time, room_number = heapq.heappop(q2)
                heapq.heappush(q2, [room_available_time + ends - start, room_number])

            meeting_count[room_number] += 1

        return meeting_count.index(max(meeting_count))



