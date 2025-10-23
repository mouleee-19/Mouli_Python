# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        # Helper function to check if there are at least k nodes remaining
        def hasKNodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k

        # Helper function to reverse k nodes and return new head and tail
        def reverseKNodes(head, k):
            prev = None
            curr = head
            while k > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k -= 1
            # prev becomes new head of this group, head becomes tail
            return prev, head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        # Keep processing in groups of k
        while hasKNodes(group_prev.next, k):
            start = group_prev.next
            end = start
            # Move end pointer to the kth node
            for _ in range(k - 1):
                end = end.next
            next_group = end.next  # Save next group's start
            end.next = None        # Temporarily break the link

            # Reverse current k group
            new_head, new_tail = reverseKNodes(start, k)

            # Connect reversed group to the rest
            group_prev.next = new_head
            new_tail.next = next_group

            # Move to the next group
            group_prev = new_tail

        return dummy.next
