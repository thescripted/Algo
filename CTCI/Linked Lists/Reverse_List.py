class Solution:
    def revere_list(self, root):
        """Takes a linked list and reverses it"""
        current = root
        leader = root.next
        current.next = None
        while leader is not None:
            leader = current
            current = leader
            leader = leader.next
        
        return current