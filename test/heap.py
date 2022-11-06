'''
Binary min-heap implementation.
Cmput 204 sample code
The heap is a binary tree that is implicitly stored in an array.
Node n has parent at index floor(n/2), and children at indices 
2*n + 1 and 2*n + 2.
We ignore index 0, as in CLRS
We will use this heap datastructure as a priority queue.

Based on code by Jesse Huard, adapted for 204 and CLRS
by Martin Mueller.
The print_tree idea is from https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
'''

import math

def parent(index):
    return index // 2

def left_child(index):
    return 2 * index

def right_child(index):
    return 2 * index + 1

def heap_size(heap):
    return len(heap) - 1

def height(heap):
    n = heap_size(heap)
    return math.floor(math.log(n, 2))

# is element at index greater than all its children?
def has_heap_property(heap, index):
    size = heap_size(heap)
    assert index >= 1
    assert index <= size
    lc = left_child(index)
    rc = right_child(index)
    if lc <= size and heap[lc] > heap[index]:
        return False
    if rc <= size and heap[rc] > heap[index]:
        return False
    return True
    
def check_heap_property(heap, start):
    n = heap_size(heap)
    for i in range(start, n//2 + 1):
        if not has_heap_property(heap, i):
            return False
    return True

def is_heap(heap, start=1): return check_heap_property(heap, start)
def is_almost_heap(heap, start=1): return check_heap_property(heap, start+1)
    
def max_heapify(heap, i, size):
    # assert here is too slow, Theta(n), kills runtime. 
    # assert is_almost_heap(heap, i)
    assert i >= 1
    assert i <= size
    lc = left_child(i)
    rc = right_child(i)
    largest = i
    if lc <= size and heap[lc] > heap[largest]:
        largest = lc
    if rc <= size and heap[rc] > heap[largest]:
        largest = rc
    if largest != i: # largest is a child, needs swap and recursion
        temp = heap[i]
        heap[i] = heap[largest]
        heap[largest] = temp
        max_heapify(heap, largest, size)
    # assert here is too slow, Theta(n), kills runtime. 
    # assert is_heap(heap, i)
    
def build_max_heap(heap):
    assert heap[0] == None
    size = heap_size(heap)
    for i in range(size//2, 0, -1):
        max_heapify(heap, i, size)
    assert is_heap(heap, 1)
  
# Needed for priority queue. Not needed for heapsort.
def increase_key(heap, index, key):
    assert index >= 1
    assert index <= heap_size(heap)
    assert key >= heap[index]
    heap[index] = key
    p = parent(index)
    while index > 1 and heap[p] < heap[index]:
        # trickle up
        temp = heap[p]
        heap[p] = heap[index]
        heap[index] = temp
        index = p
        p = parent(index)
    assert is_heap(heap)
 
# Needed for priority queue. Not needed for heapsort.
def insert(heap, key):
    heap.append(key)
    increase_key(heap, heap_size(heap), key)

def print_tree(heap, index = 1, level = 0):
    if index <= heap_size(heap):
        print_tree(heap, right_child(index), level + 1)
        if level == 0: print(heap[index])
        else: print(' ' * 3 * level, heap[index])
        print_tree(heap, left_child(index), level + 1)

##############################################################################
# test:

if __name__ == '__main__':
    a = [None, 1, 3, 5, 7, 2, 4, 6, 8, 10]
    print(f'a = {a[1:]}')
    print_tree(a)
    build_max_heap(a)
    print(f'after build_max_heap, a = {a[1:]}')
    print_tree(a)