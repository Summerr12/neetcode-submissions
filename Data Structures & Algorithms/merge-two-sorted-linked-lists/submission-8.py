# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Notes:
#to use recursive calls, remember to use self.____ and to not call self in parameters

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:   
        #recursive
        if list1 == None: return list2 #link the rest of 2 to the list
        if list2 == None: return list1 #link the rest of 1 to the list

        if list1.val <= list2.val: # if v1 is less or equal to v2, point v1 to v2 and then update the merge
            list1.next = self.mergeTwoLists(list1.next, list2) # increment
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2


        #Iterative
        # if list1 == None: return list2
        # if list2 == None: return list1

        # trackedll = ListNode()
         
        # tracking = trackedll #creates new ptr to track and keep the original ptr untopuched
        # while list1 and list2: #while there are ptrs in both linked lists
        #     if list1.val < list2.val: 
        #         tracking.next = list1
        #         list1 = list1.next
        #     else: # if less or greater equal to
        #         tracking.next = list2
        #         list2 = list2.next
        #     tracking = tracking.next

        # tracking.next = list1 if list1 else list2

        # return trackedll.next