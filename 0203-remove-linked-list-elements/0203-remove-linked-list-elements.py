# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        dummy_head = ListNode()
        dummy_head.next = head
        current_node = dummy_head
        next_node = current_node.next

        while next_node is not None:
            if next_node.val == val:
                current_node.next = next_node.next
            else:
                current_node = next_node
            next_node = current_node.next
                
        return dummy_head.next
