from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
   
        if len(hand) % groupSize != 0:
            return False
        
        cnt = Counter(hand)
        count = sorted(cnt)
        print(cnt)

        for k in count:

            while cnt[k] > 0 :

                for i in range(groupSize):
                    if cnt[k+i] <= 0:
                        return False
                    cnt[k+i] -= 1

        return True

        # for k in count:

        #     if cnt[k] > 0 :

        #         start = k
        #         for i in range(groupSize):
        #             if cnt[start+i] < cnt[k]:
        #                 return False
        #             cnt[start+i] -= cnt[k]
        
        # return True
