# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        
        middle_index = count // 2

        current = head
        for _ in range(middle_index):
            current = current.next  
        
        return current
        