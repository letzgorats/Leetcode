class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(dist)
        time = []

        for i in range(n):
        
            time.append(float(dist[i])/float(speed[i]))
        
        time.sort()
        
        for j in range(n):
            if j >= time[j]:
                j-=1
                break

        return j + 1


# Find the arrival times (remember to round them up correctly!).
# Sort.
# Find the number of times[i] >= i.
