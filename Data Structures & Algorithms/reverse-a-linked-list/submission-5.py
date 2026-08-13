# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We are creating 2 pointers, prev and curr 

        prev = None
        curr = head 
        while curr: 
            next_node = curr.next # temp
            curr.next = prev # attaches previous to the end
            prev = curr #replaces prev with curr addr
            curr = next_node


        return prev
        