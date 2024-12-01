# solution 1 - hash_table - 19ms
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        hash_table = dict()

        for i in range(len(arr)):

            if arr[i] * 2 in hash_table or arr[i] / 2 in hash_table:
                return True
            else:
                hash_table[arr[i]] = hash_table.get(arr[i], 0) + 1

        return False

# solution 2 - greedy - 0ms
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        arr.sort()
        print(arr)

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] < 0:
                    if arr[i] / 2 == arr[j]:
                        return True
                elif arr[i] >= 0:
                    if arr[i] * 2 == arr[j]:
                        return True

        return False