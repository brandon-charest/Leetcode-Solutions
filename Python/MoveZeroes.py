from typing import List

# time: O(n)
# space: O(1)

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 0

    while i < len(nums) and j < len(nums):
        if nums[i] != 0:
            i += 1
            j = i
        elif nums[j] == 0:
            j += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1


arr = [0, 1, 0, 2, 3]
moveZeroes(arr)
assert arr == [1, 2, 3, 0, 0]

arr = [0]
moveZeroes(arr)
assert arr == [0]

arr = [12]
moveZeroes(arr)
assert arr == [12]

arr = [1, 2, 3]
moveZeroes(arr)
assert arr == [1, 2, 3]

arr = [0, 0, 0, 1]
moveZeroes(arr)
assert arr == [1, 0, 0, 0]
