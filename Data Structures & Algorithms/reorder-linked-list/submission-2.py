# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # recursive , 2ptr, stack with 
        #one ptr holding head
        #one ptr iterating from left to right
        #one ptr at the end iterating from right to left

        #Recursive
        # if head == None: return None

        # #this just pushes all values to the stack
        # stackll = [] #1.  1,2.  1,2,3.  1,2,3,4.  1,2,3,4,5
        # stackll.append(head)
        # self.reorderList(head.next)

        # if head.next == None:
        #     sortedll = self.reorderList(head.next)
        #     return sortedll


        #Iterative
        stackll = []
        rl = head #right to left

        #this fill stack with a reversed list
        while rl:
            stackll.append(rl)
            rl = rl.next
        length = len(stackll)

        currll = head
        #iterate through values and replace pointers
        for i in range(length//2): #skip by 2 
            # insert largest val and reattach replaced address string
            back = stackll.pop()
            oldAddrs = currll.next #keeps track of what we are about to replace
            currll.next = back  

            currll = currll.next # step to new large val
            currll.next = oldAddrs # reattach old values

            currll = currll.next
        
        if length % 2 != 0:
            currll.next = stackll.pop()
            currll.next.next = None
        else:
            currll.next = None
        
        return None



            
