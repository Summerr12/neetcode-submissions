# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeAlt(self, head: Optional[ListNode], secondHalf: Optional[ListNode]) -> Optional[ListNode]:
        
        if not secondHalf: 
            return

        firstNext = head.next
        secondNext = secondHalf.next

        first = head
        second = secondHalf

        first.next = second
        second.next = firstNext
        # print(first.val, " and ", second.val)

        self.mergeAlt(firstNext,secondNext)
    
    def reversedList(self, secondHalf: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = secondHalf
        while curr: #1 2 3 -> 3 2 1
            next_node = curr.next
            curr.next = prev #reverse arrow
            prev = curr # update prev to curr before we go next
            curr = next_node #update curr after we reversed connections

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        #Recursive
        if not head or not head.next: return

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None #break off connection between first and second half
        secondHalf = self.reversedList(secondHalf)

        self.mergeAlt(head, secondHalf)



        

        #--------------------------------
        #Iterative
        # stackll = []
        # rl = head #right to left

        # #this fill stack with a reversed list
        # while rl:
        #     stackll.append(rl)
        #     rl = rl.next
        # length = len(stackll)

        # currll = head
        # #iterate through values and replace pointers
        # for i in range(length//2): #skip by 2 
        #     # insert largest val and reattach replaced address string
        #     back = stackll.pop()
        #     oldAddrs = currll.next #keeps track of what we are about to replace
        #     currll.next = back  

        #     currll = currll.next # step to new large val
        #     currll.next = oldAddrs # reattach old values

        #     currll = currll.next
        
        # if length % 2 != 0:
        #     currll.next = stackll.pop()
        #     currll = currll.next
        
        # currll.next = None
        
        # return None



            
