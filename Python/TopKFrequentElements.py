from typing import List
from heapq import heappush, heappushpop
from collections import defaultdict


# Time: O(n logk)
# Space: (n)

def topKFrequent(nums: List[int], k: int) -> List[int]:
    d = defaultdict(int)
    heap = []
    for num in nums:
        d[num] += 1

    for num in d.keys():
        if len(heap) == k:
            heappushpop(heap, (d[num], num))
        else:
            heappush(heap, (d[num], num))
    return [x[1] for x in heap]


# Time: O(n)
# Space: O(n)
def topKFrequent_Bucket(nums: List[int], k: int) -> List[int]:
    bucket = [[] for _ in range(len(nums))]
    d = defaultdict(int)

    for num in nums:
        d[num] += 1

    for key in d.keys():
        freq = d[key]
        bucket[freq].append(key)

    res = []

    for i in range(len(nums) - 1, -1, -1):
        if len(res) == k:
            break
        if bucket[i]:
            res.append(bucket[i][0])
    return res


print(topKFrequent_Bucket([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1, 1, 1, 2, 2, 3], 3))
print(topKFrequent([1, 1, 1, 2, 2, 3], 1))
