# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if len(head) == 0: return []
        curr = head
        rev_l = []

        while curr:
            rev_l.append(curr.val)
            curr = curr.next

        rev_l = rev_l[::-1]
        if len(rev_l) == 0: return None
        rev_head = ListNode(rev_l[0])
        x = rev_head
        for i in rev_l[1:]:
            x.next = ListNode(i)
            x = x.next
            
        return rev_head
