from heapq import heappush, heappushpop
from typing import List


# time: O(nlogk)
# space: O(k)
def findKthLargest(nums: List[int], k: int) -> int:
    heap = []

    for num in nums:
        if len(heap) < k:
            heappush(heap, num)
        else:
            heappushpop(heap, num)
    return heap[0]
