# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Helper function to reverse a portion of the list
        def reverseLinkedList(head: ListNode, k: int) -> ListNode:
            prev, curr = None, head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev

        # Count the number of nodes in the list
        count = 0
        ptr = head
        while ptr:
            count += 1
            ptr = ptr.next

        # Dummy node to simplify head manipulations
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while count >= k:
            # Reverse k nodes
            group_start = prev_group_end.next
            group_end = group_start

            # Move group_end k-1 times to reach the end of the group
            for _ in range(k - 1):
                group_end = group_end.next

            next_group_start = group_end.next

            # Reverse the current group of k nodes
            reversed_group = reverseLinkedList(group_start, k)

            # Connect the previous part with the reversed group
            prev_group_end.next = reversed_group
            group_start.next = next_group_start

            # Move prev_group_end to the end of the reversed group
            prev_group_end = group_start

            # Reduce the count by k since we've reversed k nodes
            count -= k

        return dummy.next
