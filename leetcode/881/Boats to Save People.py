class Solution(object):
    def numRescueBoats(self, people, limit):
        
        answer = 0
        people = sorted(people,reverse=True)

        left = 0
        right = len(people)-1

        while left != right and left < right :
            
            if people[left] == limit:
                left += 1
                
            elif people[left] < limit:
                if people[left] + people[right] <= limit:
                    right -= 1
                    left += 1
                else:
                    left += 1
            answer += 1

        return answer+1 if left == right else answer
