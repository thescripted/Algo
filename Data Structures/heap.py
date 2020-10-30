# Implementation of a Heap/Priority Queue
# Implementation involves the main methods required
#   .isEmpty()
#   .peek()
#   .insert(value)
#   .remove()
import math

class MinHeap:
    def __init__(self):
        self.heap = []
        pass

    def isEmpty(self):
        if len(self.heap) <= 0:
            return True
        return False

    def peek(self):
        if self.isEmpty():
            raise ValueError("Cannot peak a heap that is empty")
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up()

    def remove(self):
        if self.isEmpty():
            raise ValueError("Cannot remove from a heap that is empty")
        top = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down()
        return top

    def _heapify_up(self):
        idx = len(self.heap)
        parent = math.floor(idx/2)
        if parent <= 0:
            return

        while parent > 0:
            if self.heap[parent - 1] > self.heap[idx - 1]:
                self.heap[parent - 1], self.heap[idx - 1] = self.heap[idx - 1], self.heap[parent - 1]
                idx = parent
                parent = Math.floor(parent/2)
            else:
                break

    #TODO: Update this code.
    def _heapify_down(self):
        parent = 1
        heaplen = len(self.heap)
        leftchild = parent * 2
        rightchild = parent * 2 + 1
        while leftchild <= heaplen or rightchild <= heaplen:
            if leftchild <= heaplen and rightchild <= heaplen:
                if self.heap[leftchild - 1] < self.heap[rightchild - 1]:
                    self.heap[leftchild - 1], self.heap[parent-1] = self.heap[parent - 1], self.heap[leftchild - 1]
                    parent = leftchild
                    leftchild = parent * 2
                    rightchild = parent * 2 + 1
                else:
                    self.heap[rightchild- 1], self.heap[parent-1] = self.heap[parent - 1], self.heap[rightchild - 1]
                    parent = rightchild 
                    leftchild = parent * 2
                    rightchild = parent * 2 + 1
            if leftchild >= heaplen:
                self.heap[rightchild- 1], self.heap[parent-1] = self.heap[parent - 1], self.heap[rightchild - 1]
                parent = rightchild 
                leftchild = parent * 2
                rightchild = parent * 2 + 1
            else:
                self.heap[leftchild - 1], self.heap[parent-1] = self.heap[parent - 1], self.heap[leftchild - 1]
                parent = leftchild
                leftchild = parent * 2
                rightchild = parent * 2 + 1
