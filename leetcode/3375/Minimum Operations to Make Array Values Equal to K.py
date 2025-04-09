# solution 1 - set,hash table - (75ms) - (2025.04.09)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        if k > min(nums):
            return -1

        unique_elements = set(nums)
        unique_count = len(unique_elements)

        # Step 3: If 'k' is already in the list,
        # return the number of unique elements minus 1.
        # No operation is needed to reach 'k',
        # so we subtract 1 from the unique count.
        if k in unique_elements:
            return unique_count - 1

        # Step 4: If 'k' is not in the list,
        # return the number of unique elements.
        # In this case, we must perform at least one operation
        # for each unique element in the list.
        else:
            return unique_count
