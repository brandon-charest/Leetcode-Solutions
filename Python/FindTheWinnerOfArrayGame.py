from typing import List


# def getWinner(arr: List[int], k: int) -> int:
#     if k > len(arr):
#         return max(arr)
#
#     count = 0
#     while count != k:
#         if arr[0] > arr[1]:
#             count += 1
#             arr.append(arr.pop(1))
#         else:
#             count = 1
#             arr.append(arr.pop(0))
#     return arr[0]

# time O(n)
# space: O(1)

# single pass
def getWinner(arr: List[int], k: int) -> int:
    if k > len(arr):
        return max(arr)

    count = 0
    curr = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > curr:
            curr = arr[i]
            count = 0
        count += 1
        if count == k:
            break
    return curr
