class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        def recur(list1, list2):

            if not list1:
                return list2
            
            if not list2:
                return list1

            
            if list1.val > list2.val:
                list2.next = recur(list1, list2.next)
                return list2
                
            else:
                list1.next = recur(list1.next, list2)
                return list1


        return recur(list1, list2)
