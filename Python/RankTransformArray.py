from typing import List
from collections import defaultdict


# time: O(nlogn)
# space: O(n)

def arrayRankTransform(arr: List[int]) -> List[int]:
    d = defaultdict(int)
    temp = arr.copy()
    temp.sort()
    rank = 1
    for i, num in enumerate(temp):
        if i == 0:
            d[num] = rank
            continue
        if num != temp[i - 1]:
            rank += 1
        d[num] = rank

    res = []
    for num in arr:
        res.append(d[num])
    return res
