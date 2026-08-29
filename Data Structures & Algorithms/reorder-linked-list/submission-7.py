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
        # '''
        # it goes smallest, largest, smallest, largest..
        # find the middle and last node
        # get the second half of the Linked list and reverse it
        # Then call merge function which holds smallest and largest nodes and their next nodes
        # then merges and recursively calls the next nodes to reassign next pointers
        # '''
        # if not head or not head.next: return

        # slow, fast = head, head
        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # secondHalf = slow.next
        # slow.next = None #break off connection between first and second half
        # secondHalf = self.reversedList(secondHalf)

        # self.mergeAlt(head, secondHalf)



        

        #--------------------------------
        # '''
        # it goes smallest, largest, smallest, largest..
        # we first create a stack while incrementing the list to have a reference from right to left
        # we run a for loop that skips a point every instance (skipping the smallest and replacing the next value with the largest)
        # We pop largest value from stack,
        # keep track of all values on the front of curr,
        # replace with popped value and reattach the rest of the list that was "removed"
        # then increment
        # Lastly, to dictate odd and even length lists, if there is a odd list, it will just attach the "middle" last value to the end, else return
        # '''
        
        
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
            currll = currll.next
        
        currll.next = None
        
        return None



            
