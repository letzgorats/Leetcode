import heapq

class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.seats = [i for i in range(1,n+1)]
        heapq.heapify(self.seats)    

    def reserve(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.seats)

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.seats,seatNumber)
