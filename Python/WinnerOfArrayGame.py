from typing import List


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

print(getWinner([2,1,3,5,4,6,7], 2))