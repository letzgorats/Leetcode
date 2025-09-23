# solution 1 - (map,split,string) - (16ms, 0ms) - (2024.03.23), (2025.09.23)
class Solution(object):
    def compareVersion(self, version1, version2):

        v1 = list(map(int,version1.split('.')))
        v2 = list(map(int,version2.split('.')))

        if len(v1) != len(v2):

            if len(v1) < len(v2):
                v1.extend([0] * (len(v2)-len(v1)))
            elif len(v1) > len(v2):
                v2.extend([0] * (len(v1)-len(v2)))

        for i in range(len(v1)):

            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1

        return 0
