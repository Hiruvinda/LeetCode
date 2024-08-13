# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

    # Iterate through both lists until the end of both
        while l1 is not None or l2 is not None:
        # Get the current values, if the node is present
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

        # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10  # Carry for the next digit
            total = total % 10   # The digit to store in the current node

        # Create a new node with the total and move the current pointer
            current.next = ListNode(total)
            current = current.next

        # Move to the next nodes in the list if available
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

    # If there's a carry left, add it as a new node
        if carry > 0:
            current.next = ListNode(carry)

    # The result list is the next node of the dummy node
        return dummy.next

# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst
