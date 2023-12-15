class Solution(object):
    def destCity(self, paths):
        city = dict()
        for a,b in paths:
            city[a] = b
        
        answer = ""
        for c in city:
 
            if city[c] not in city:
                answer = city[c]
                break

        return answer
