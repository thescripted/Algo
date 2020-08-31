#Reverse a singly linked list.

class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            leader = curr.next
            curr.next = prev
            prev = curr
            curr = leader
        return prev
# Space: O(1)
# Time: O(N)
