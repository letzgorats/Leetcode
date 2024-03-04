class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        
        score = 0 
        tokens = sorted(tokens)
        if not tokens or tokens[0] > power:
            return 0 

        left = 0
        right = len(tokens)-1

        while left < right:

            if score > 0 and power < tokens[left]:
                score -= 1
                power += tokens[right]
                right -= 1
            elif score > 0 and power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
            elif score <= 0 :
                if power >= tokens[left] :
                    score += 1
                    power -= tokens[left]
                    left += 1
            # print(score,power)
            # print(left,right)
        
        if power >= tokens[right]:
            return score + 1
        else:
            return score



# final code
class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        
        score = 0 
        tokens = sorted(tokens)
        if not tokens or tokens[0] > power:
            return 0 

        left = 0
        right = len(tokens)-1

        while left < right:

            if score > 0 and power < tokens[left]:
                score -= 1
                power += tokens[right]
                right -= 1
            elif power >= tokens[left] :
                    score += 1
                    power -= tokens[left]
                    left += 1
            # print(score,power)
            # print(left,right)
        
        if power >= tokens[right]:
            return score + 1
        else:
            return score
