# bubble sort - (sort) - (8ms) - (2025.05.17)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # bubble sort
        for _ in range(1, len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            # print(nums)

# selection sort - (sort) - (0ms) - (2025.05.17)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # selection sort
        for i in range(len(nums) - 1):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]

# merge sort - (sort) - (0ms) - (2025.05.17)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # merge sort
        def merge_sort(arr):
            if len(arr) < 2:
                return arr

            mid = len(arr) // 2
            left_arr = arr[:mid]
            right_arr = arr[mid:]

            # recursion
            merge_sort(left_arr)
            merge_sort(right_arr)

            # merge
            i, j = 0, 0  # left_arr idx, right_arr idx
            k = 0  # merged_index
            # merge
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1

        merge_sort(nums)

# quick sort(in-place) - (sort) - (0ms) - (2025.05.17)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # quick sort
        def quick_sort(arr, left, right):
            if left < right:
                pivot_index = partition(arr, left, right)

                quick_sort(arr, left, pivot_index - 1)
                quick_sort(arr, pivot_index + 1, right)

        def partition(arr, left, right):
            # pivot selection - (we use the last element here for simplicity)
            i = left  # index of smaller element
            j = right - 1
            pivot = arr[right]

            while i < j:
                while i < right and arr[i] < pivot:
                    i += 1
                while j > left and arr[j] >= pivot:
                    j -= 1

                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]

            if arr[i] > pivot:
                arr[i], arr[right] = arr[right], arr[i]

            return i

        quick_sort(nums, 0, len(nums) - 1)


# solution 1 - (sort) - (11ms) - (2024.06.12)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i, left = 0,0
        right = len(nums) -1

        while i <= right :
            
            
            if nums[i] == 0:
                
                nums[i] , nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            
            elif nums[i] == 2:
                nums[i] , nums[right] = nums[right], nums[i]
                right -= 1
            
            elif nums[i] == 1:
                i += 1
            

          
        