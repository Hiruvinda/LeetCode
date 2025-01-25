# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Determine the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Compute the effective rotations needed
        k %= length
        if k == 0:
            return head

        # Step 3: Find the new head after the rotation
        # The new head is at position (length - k)
        steps_to_new_head = length - k
        prev = None
        current = head
        for _ in range(steps_to_new_head):
            prev = current
            current = current.next

        # Step 4: Update the links to perform the rotation
        prev.next = None  # Break the list
        tail.next = head  # Connect the end of the list to the old head

        return current
