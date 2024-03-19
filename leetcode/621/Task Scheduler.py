class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        count = {}
        for t in tasks:
            count[t] = count.get(t,0) + 1

        max_cnt = max(count.values())
        count = list(count.values())
        max_count_ele_count = 0

        print(count)

        i = 0
        while i < len(count):
            if count[i] == max_cnt:
                max_count_ele_count += 1
            i += 1
        print(max_count_ele_count)

        ans = (max_cnt -1) * (n+1) + max_count_ele_count
        print(ans)
        
        return max(ans,len(tasks))
