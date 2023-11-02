from typing import List

# time: O(n)
# space: O(n)
def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i, num in enumerate(nums):
        val = target - num
        if val in d:
            return [d[val], i]
        d[num] = i


res = twoSum([2, 7, 11, 15], 9)
assert res == [1, 0] or res == [0, 1]

res = twoSum([3, 3], 6)
assert res == [1, 0] or res == [0, 1]
