from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    return mergeSort(lists, 0, len(lists) - 1)


def mergeSort(lists, start, end):
    if start == end:
        return lists[start]

    mid = start + (end - start) // 2
    left = mergeSort(lists, start, mid)
    right = mergeSort(lists, mid + 1, end)
    return merge(left, right)


def merge(l1, l2):
    merged = ListNode(-1)
    dummy = merged

    while l1 and l2:
        if l1.val <= l2.val:
            dummy.next = ListNode(l1.val)
            l1 = l1.next
        else:
            dummy.next = ListNode(l2.val)
            l2 = l2.next
        dummy = dummy.next

    while l1:
        dummy.next = ListNode(l1.val)
        dummy = dummy.next
        l1 = l1.next

    while l2:
        dummy.next = ListNode(l2.val)
        dummy = dummy.next
        l2 = l2.next

    return merged.next


k1 = ListNode(1)
k1.next = ListNode(2)
k1.next.next = ListNode(5)

k2 = ListNode(1)
k2.next = ListNode(3)
k2.next.next = ListNode(4)

k3 = ListNode(2)
k3.next = ListNode(6)

result = mergeKLists([k1, k2, k3])

while result:
    print(result.val)
    result = result.next
