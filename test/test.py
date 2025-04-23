'''
Priority queue implemented as a heap.
Cmput 204 sample code
Written by Martin Mueller.
Requires heap.py
'''

import heap, sys
sys.path.append("..")
from main.priorityQueue import priorityQueue

class priority_queue(object):
    def __init__(self, a):
        self.a = a
        self.size = heap.heap_size(a)
        heap.build_max_heap(a)
    
    def extract_max(self):
        assert self.size > 0
        result = self.a[1]
        self.a[1] = self.a[self.size]
        self.size -= 1
        if self.size > 0:
            heap.max_heapify(self.a, 1, self.size)
        return result

    def decrease_key(self, index, key):
        assert key <= self.a[index]
        self.a[index] = key
        heap.max_heapify(self.a, index, self.size)

    def increase_key(self, index, key):
        assert key >= self.a[index]
        heap.increase_key(self.a, index, key)

    def insert_key(self, key):
        heap.insert(self.a, key)
        self.size += 1
    
##############################################################################
# test:

def print_pq(pq):
    print(pq.a[1:])
    heap.print_tree(pq.a)
    
def test_pq():
    # Example from slides. But I keep changing the same pq,
    # So the content of the pq change away from the slides.
    
    # If you want the data as well, you can use a dictionary
    # and put the "key: data" pairs in there.
    # Then for efficiency, run the priority queue algorithm only 
    # on the keys in the heap, and access the data through the dict.

    a = [None, 4,1,7,9,3,10,14,8,2,16]
    b = []
    pq = priority_queue(a)
    print(pq.a)
    m = pq.extract_max()
    print('Extract max', m)
    print(pq.a)
    pq.increase_key(4, 17)
    print('increase_key(4, 17)')
    print(pq.a)
    pq.insert_key(15)
    print('insert_key(15)')
    print(pq.a)
    pq.decrease_key(2, 3)
    print('decrease_key(2, 3)')
    print(pq.a)

    pq = priorityQueue(b, len(b))
    print(pq.queue)
    m = pq.extractMax()
    print('Extract max', m)
    print(pq.queue)
    pq.increaseKey(4, 17)
    print('increase_key(4, 17)')
    print(pq.queue)
    pq.heapInsert(15)
    print('insert_key(15)')
    print(pq.queue)
    pq.decreaseKey(2, 3)
    print('decrease_key(2, 3)')
    print(pq.queue)

if __name__ == '__main__':
    test_pq()