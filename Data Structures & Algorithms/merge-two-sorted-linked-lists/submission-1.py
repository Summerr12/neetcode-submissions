# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None: return None

        #keeps track of where we are during sorting
        curr1 = None
        curr2 = None

        #returning variable that holds the head
        trackedll = None

        #mini functions if there is only one list left
        if list1 == None:
            trackedll = list2 #add head address
            list2 = list2.next #increment
            tracking = trackedll #create temp tracker to add sorted vals
            while list2: #no list1 so there is just list 2 add
                tracking.next = list2
                tracking = tracking.next
                list2 = list2.next
            return trackedll

        if list2 == None:
            trackedll = list1 #add head address
            list1 = list1.next #increment
            tracking = trackedll
            while list1:
                tracking.next = list1
                tracking = tracking.next
                list1 = list1.next
            return trackedll

        
        if list1.val < list2.val: 
            trackedll = list1
            curr1 = list1.next
            curr2 = list2
        else:
            trackedll = list2
            curr1 = list1
            curr2 = list2.next
            
        tracking = trackedll #creates new ptr to track and keep the original ptr untopuched
        while curr1 and curr2: #while there are ptrs in both linked lists
            if curr1.val < curr2.val: 
                tracking.next = curr1
                curr1 = curr1.next
            else: # if less or greater equal to
                tracking.next = curr2
                curr2 = curr2.next
            tracking = tracking.next

        while curr1:
            tracking.next = curr1
            tracking = tracking.next
            curr1 = curr1.next

        while curr2:
            tracking.next = curr2
            tracking = tracking.next
            curr2 = curr2.next
        
        return trackedll




