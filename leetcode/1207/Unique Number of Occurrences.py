class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = {}
        for i in arr:
            counts[i] = counts.get(i,0) + 1

        return len(set(arr)) == len(set(counts.values()))
      # return len(counts) == len(set(counts.values()))
