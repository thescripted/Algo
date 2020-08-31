class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Solution #1: O(N) Space, O(N) Time
    def remove_duplicates(self, head: ListNode) -> ListNode:
        hashset = set()
        prev = None
        curr = head
        while curr != None:
            if curr.val in hashset:
                prev.next = curr.next
            else:
                hashset.add(curr.val)
                prev = curr
            curr = curr.next
        return head
        
    # Solution #2: O(1) Space, O(N^2) Time
    def remove_duplicates_two(self, head: ListNode) -> ListNode:
        curr = head
        while curr != None:
            runner = curr
            while runner.next != None:
                if runner.next.val == curr.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
                curr = curr.next
        return head

# sol = Solution()
# linkedlist = ListNode(val=4, 
#              next=ListNode(val=2, 
#              next=ListNode(val=2, 
#              next=ListNode(val=1, 
#              next=None))))

# sol.remove_duplicates(linkedlist)
