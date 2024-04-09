# solution - simulation - 시간복잡도 : O(n*max(tickets))

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
      
        n = len(tickets)
        seconds = 0
        while tickets[k] != 0:

            for i in range(len(tickets)):
                if tickets[i] != 0:
                    tickets[i] -= 1
                    seconds += 1      
                    if tickets[k] == 0:
                        break

        return seconds  


# solution - math - 시간복잡도 : O(n) - more effective
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):

        total = 0
        target = tickets[k]

        for i in range(len(tickets)):
            t = tickets[i]
            if i <= k:
                total += min(t,target)
            else:
                total += min(t,target-1)

        return total

'''
24 + 24 + 5 + 24 = 77
                        [84,49,5,24,70,77,87,8]
23 + 23 + 23 + 8 = 77
'''        
