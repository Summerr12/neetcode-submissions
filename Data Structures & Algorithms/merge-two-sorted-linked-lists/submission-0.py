# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None: return None
        
        x = list1
        y = list2

        #var to keep track of main linkedlist
        #keeps track of where we are
        curr1 = None
        curr2 = None

        trackedll = None

        if list1 == None:
            trackedll = list2
            list2 = list2.next
            tracking = trackedll
            while list2:
                tracking.next = list2
                tracking = tracking.next
                list2 = list2.next
            return trackedll

        if list2 == None:
            trackedll = list1
            list1 = list1.next
            tracking = trackedll
            while list1:
                tracking.next = list1
                tracking = tracking.next
                list1 = list1.next
            return trackedll

        
        if x.val < y.val: 
            trackedll = x
            curr1 = x.next
            curr2 = y
        else:
            trackedll = y
            curr1 = x
            curr2 = y.next
            
        tracking = trackedll #creates new ptr to track and keep the original ptr untopuched
        while curr1 and curr2: #while there are ptrs in both linked lists
            if curr1.val < curr2.val: 
                tracking.next = curr1
                curr1 = curr1.next
            else: # if less or greater equal to
                tracking.next = curr2
                curr2 = curr2.next
            tracking = tracking.next

        if curr1:
            while curr1:
                tracking.next = curr1
                tracking = tracking.next
                curr1 = curr1.next

        if curr2:
            while curr2:
                tracking.next = curr2
                tracking = tracking.next
                curr2 = curr2.next
        
        return trackedll




