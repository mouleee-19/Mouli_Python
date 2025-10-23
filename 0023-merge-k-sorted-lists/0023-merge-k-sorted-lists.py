# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # Create a min-heap
        heap = []

        # Initialize the heap with the head of each linked list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))  # (value, index, node)

        dummy = ListNode(0)
        current = dummy

        # Extract the smallest element and add the next node from that list
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
