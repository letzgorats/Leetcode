class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = defaultdict(int)

        for n in nums:
            cnt[n] += 1

        value_list = sorted(cnt.values(),reverse=True)
        tmp = value_list[0]
        answer = tmp
        for v in value_list[1:]:

            if v == tmp:
                answer += v
            else:
                break

        return answer
