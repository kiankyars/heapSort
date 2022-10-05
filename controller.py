import random
import sys
from maxHeap import maxHeapify, maxHeapSort
from minHeap import minHeapify, minHeapSort


def main():
    size = int(sys.stdin.readline())
    almostHeap = size // 2
    array = range(size)
    random.shuffle(array)
    type = sys.stdin.readline().strip()
    if type == 'max':
        for i in range(almostHeap -1, -1, -1):
            maxHeapify(array, i, size)
        maxHeapSort(array)
    elif type == 'min':
        for i in range(almostHeap -1, -1, -1):
            minHeapify(array, i)
        minHeapSort(array, size)
    else:
        quit(1)
    print(array)

if __name__ == '__main__':
    main()
