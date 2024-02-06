class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        count = defaultdict(list)

        for word in strs:
            s = "".join(sorted(word))

            count[s].append(word)
            
        # print(count)

        return count.values()
