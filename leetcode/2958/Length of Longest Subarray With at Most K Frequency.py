from collections import deque
class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        cnt = defaultdict(int)
        index = defaultdict(deque)
        answer = 0
        tmp = 0
        least = 0

        for i,num in enumerate(nums):

            index[num].append(i)
            cnt[num] += 1

            while cnt[num] > k :

                old_index = index[num].popleft()
                cnt[num] -= 1
                least = max(least,old_index + 1)  # 서브배열의 시작 지점을 갱신
            
            answer = max(answer, i - least + 1)

        return answer


        # [1,2,2,1,3]
        # 1

                
            
