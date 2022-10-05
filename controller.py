import random
import sys
from maxHeap.py import maxHeapify.py
from maxHeap.py import maxHeapSort.py
from minHeap.py import minHeapify.py
from minHeap.py import minHeapSort.py



def main():
    size = int(sys.stdin.readline())
    almostHeap = size // 2
    array = random.shuffle(range(size))
    type = sys.stdin.readline().strip()
    if type == 'max':
        for i in range(almostHeap -1, -1, -1):
            maxHeapify(array, i)
        maxHeapSort(array)
    elif type == 'min':
        for i in range(almostHeap -1, -1, -1):
            minHeapify(array, i)
        minHeapSort(array)
    else:
        quit(1)

if __name__ == '__main__':
    main()
