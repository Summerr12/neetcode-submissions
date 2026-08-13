# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #track a pointer to be the nth 
        #so we start at head with count 0,our nth = 1st node, then increment count and nodes till count=n, then
        #then if there is a next node, we keep a distance of n+1 between curr and nth
        #12 n=2
        # curr=1 count=1 replace = 1
        # curr=2 count=2 replace = 1
        # if next is None, remove replace = 1: return replace.next
        # if next is none AND if count > n, increment replace
        # 



        #12345678 n=3
        #1 curr=1 count=1
        #2 curr=2 count=2
        #3 nth=3 curr=3 count= 0 Create the nth pointer
        #4 nth=3 curr=4 count= 1
        #5 nth=3 curr=5 count= 2 < n
        #6 nth=3 curr=6 count= 3 < n
        #7 nth=4 curr=7 count= 4 > n
        #8 nth=5 curr=8 count= 5 > n so we remove n index and attach curr.next = curr.next.next
        

        # 2 ptrs
        #If we have a ptr that is delayed till n+1 (number before the one we want to removie)
        # we start at count 1 for the first value
        # We need a dummy index 0 node

        if not head.next: #if there is just one value 
            if n != 1: 
                return head
            else:
                return None

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
        
        #when looop ends, we expect to be at the end of the list and have a ptr at the node that needss to be removed

        delayed_node.next = delayed_node.next.next
        return dummy_node.next
        #if count>=n, we know we have found the node to remove
        #if count < n, then that means the list is too small to create space.
        #.  [1]. 1.     [1,2]. 2.  [1,2,3]. 3
        #.  remove the first value if n = length of list
            
        return head


        
