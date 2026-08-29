# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        curr = result
        while l1 and l2:

            if l1.val <= l2.val: #if list1 val is smaller than l2 val, insert l2
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 if l1 else l2

        return result.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        loop through list of linked lists and sort list
        """
        if not lists: return None

        while len(lists) > 1:
            merged = []
            #merge pairs of lists till there is only one list
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.merge2(l1,l2))
            lists = merged
        
        return lists[0]