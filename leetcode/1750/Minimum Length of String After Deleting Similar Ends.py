class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = len(s)-1
        while left < right and s[left] == s[right]:
            current_char = s[left]

            while left <= right and s[left] == current_char:
                left += 1

            while left <= right and s[right] == current_char:
                right -= 1

        return max(0, right - left + 1)
