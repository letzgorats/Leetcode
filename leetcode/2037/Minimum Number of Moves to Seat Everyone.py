class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        
        students = sorted(students)
        seats = sorted(seats)
        answer = 0

        for i in range(len(students)):

            answer += abs(students[i]-seats[i]) 

        return answer
