# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        #recursive
        if list1 == None: return list2
        if list2 == None: return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        #Iterative
        # #mini functions if there is only one list left
        # if list1 == None: return list2
        # if list2 == None: return list1

        # #keeps track of where we are during sorting
        # curr1 = None
        # curr2 = None

        # #returning variable that holds the head
        # trackedll = None
        
        # if list1.val < list2.val: 
        #     trackedll = list1
        #     curr1 = list1.next
        #     curr2 = list2
        # else:
        #     trackedll = list2
        #     curr1 = list1
        #     curr2 = list2.next
            
        # tracking = trackedll #creates new ptr to track and keep the original ptr untopuched
        # while curr1 and curr2: #while there are ptrs in both linked lists
        #     if curr1.val < curr2.val: 
        #         tracking.next = curr1
        #         curr1 = curr1.next
        #     else: # if less or greater equal to
        #         tracking.next = curr2
        #         curr2 = curr2.next
        #     tracking = tracking.next

        # tracking.next = curr1 if curr1 else curr2

        # return trackedll




