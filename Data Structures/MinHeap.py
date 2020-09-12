# Min heap extracts the minimum element in a tree by popping the top element.
# Min heap can remove and add elements.

class Min_Heap:
    heap = []

    # extract_min:
    # grab the top element from the heap. take the last element from the min heap to the top and bubble it down.
    def extract_min(self):
        if not len(heap):
            raise IndexError("Min heap is already empty")

        minimum = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1] # replace last element to the root
        del heap[len(heap) - 1] 
        self._bubble_down(0)
        return minimum

    def _bubble_down(self, idx): # Take an element and swap it with its left or right child.
        min_child_idx = self._find_min_child_idx(idx)
        if min_child_idx == -1:
            return
        if self.heap[idx] > self.heap[min_child_idx]: # Swap the child
            self.heap[idx], self.heap[min_child_idx] = self.heap[min_child_idx], self.heap[idx]
            self._bubble_down(min_child_idx)
    
    def _bubble_up(self, idx): # Moves an element up the tree
        if idx == 0: 
            return
        parent_idx = (idx - 1) // 2
        if self.heap[parent_idx] > self.heap[idx]: # swap the elements
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self._bubble_up(parent_idx)
        

    def _find_min_child_idx(self, idx):
        left_idx = idx * 2 + 1
        right_idx = idx * 2 + 2
        if right_idx >= len(self.heap): # right child does not exist
            if left_idx >= len(self.heap): # left child does not exist
                return -1
            return left_idx
        #Comparision on both index
        if self.heap[right_idx] > self.heap[left_idx]:
            return right_idx
        else: 
            return left_idx
    
    def insert(self, value): # insert a value into the heap
        self.heap[len(self.heap) - 1] = value
        self._bubble_up(len(self.heap) - 1)
        


