# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carryOver = 0
        head = None         # The head of the resulting list
        current = None      # PlaceHolder Node used to traverse the list

        while l1 or l2 or carryOver:
            # Get the current values of the list
            # If no val get 0 instead
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            #Add the 2 numbers
            #If num greater than 9 then store carry in carryOver and the num is the remainder
            carryOver, num = divmod(val1+val2+carryOver,10)

            #Add the digit to the new_node
            new_node = ListNode(num)
            
            #Check if head is null and if it is than initialize it
            if not head:
                head = new_node
                current = head
            #Else add the node to the result
            else:
                current.next = new_node
                current = current.next
            
            #Move to the next Node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head