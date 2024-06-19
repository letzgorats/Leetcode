# solution - Binary Search (O(Nlog(Max(Bloomday))))
class Solution(object):
    def minDays(self, bloomDay, m, k):


        if m * k > len(bloomDay):
            return -1

        def canMakeBouquets(days):

            bouquets, flowers = 0, 0
            for bloom in bloomDay:

                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0

                else:
                    flowers = 0

                if bouquets == m:
                    return True

            return False

        left, right = min(bloomDay), max(bloomDay)

        while left <= right:

            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left



# TLE solution - brute force
class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """

        if m * k > len(bloomDay):
            return -1

        dayCandi = sorted(list(set(bloomDay)))
        n = len(bloomDay)

        for d in dayCandi:

            bouquets = 0
            flowers = 0

            for i in range(n):

                if bloomDay[i] <= d:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            if bouquets >= m:
                return d

        return -1
