class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        tests = minutesToTest // minutesToDie + 1
        pig = 0
        current_tests = 1  # 0번째 테스트 (아무 것도 안 함)을 고려

        while current_tests < buckets:
            pig += 1
            current_tests = tests ** pig

        return pig


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        tests = minutesToTest // minutesToDie + 1
        pig = 0
        
        while tests ** pig < buckets:
            pig += 1
         
        return pig
        
