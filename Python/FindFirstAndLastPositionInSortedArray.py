from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]
    if nums[0] == target and nums[-1] == target:
        return [0, len(nums) - 1]

    def findStart():
        i = 0
        j = len(nums) - 1
        idx = -1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] >= target:
                j = mid - 1
            else:
                i = mid + 1
            if nums[mid] == target:
                idx = mid
        return idx

    def findEnd():
        i = 0
        j = len(nums) - 1
        idx = -1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] <= target:
                i = mid + 1
            else:
                j = mid - 1

            if nums[mid] == target:
                idx = mid
        return idx

    start = findStart()
    end = findEnd()
    return [start, end]


print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 5))
print(searchRange([5,7,7,8,8,10], 9))
print(searchRange([], 3))
