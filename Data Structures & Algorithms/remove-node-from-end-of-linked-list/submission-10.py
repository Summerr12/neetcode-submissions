# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        We start with 3 nodes, 1 node behind the head (dummy node) to counter smaller lists
        1 left node starting at the dummy node and 1 right node to track till the end of the list
        then we increment the right node until n<=0, then increment both left and right till the end of list
        once we finish the while loop, the left node should be at the node before the one we need to remove, so we remove it and return "head"
        '''
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

        
