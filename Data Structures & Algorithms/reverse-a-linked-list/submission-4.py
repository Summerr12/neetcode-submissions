# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We are creating 2 pointers, prev and curr 
        # curr will be reversed where curr points to 0 -> None
        # so prev should be 1 afterwards
        # curr -> 0, prev -> None
        # curr -> 0 > None
        prev = None
        curr = head 
        while curr: #while pointer still pointing at values
            next_node = curr.next # temp
            curr.next = prev # attaches previous to the end
            prev = curr #replaces prev with curr addr
            curr = next_node


        return prev
        