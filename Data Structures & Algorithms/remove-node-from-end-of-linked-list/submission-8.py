# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy_node = ListNode(0,head)
        curr = head 
        delayed_node = dummy_node# node that is spaced n from curr 
        
        count = 0
        while curr:
            if n <= 0: 
                delayed_node = delayed_node.next #increment
            
            # print("curr: ", curr.val if curr else None, " delayed_node: ", delayed_node.val if delayed_node else None, "count: ", count)
            n -= 1
            curr = curr.next
    
        delayed_node.next = delayed_node.next.next
        return dummy_node.next

        
