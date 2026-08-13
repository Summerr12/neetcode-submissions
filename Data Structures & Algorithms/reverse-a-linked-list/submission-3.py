# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # so optional[] is a val or null but counts as a ListNode and wants to return as a listNode
        # 
        tail = head

        tempA = []
        rev = None
        while tail:
            tempA.insert(0,tail.val)
            tail = tail.next

        if len(tempA) == 0: return None

        r = ListNode(tempA[0])
        rev = r
        for i in tempA[1:]:
            rev.next = ListNode(i)
            rev = rev.next

        return r
        