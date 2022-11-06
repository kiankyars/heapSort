import random
import sys
from maxHeap import buildMaxHeap, maxHeapSort
from minHeap import buildMinHeap, minHeapSort


def main():
    '''
    main function that runs a test run on a random array
    '''
    if len(sys.argv) != 3:
        print("Usage: python3 main.py size max/min")
        return
    size = int(sys.argv[1])
    type = sys.argv[2]
    # print([*range(10)])
    array = [*range(size)]
    random.shuffle(array)
    print(f'array to be sorted as a {type}heap: {array}')
    if type == 'max':
        buildMaxHeap(array, size)
        print(maxHeapSort(array, size))
    elif type == 'min':
        buildMinHeap(array, size)
        print(minHeapSort(array, size))
    else:
        quit(1)

if __name__ == '__main__':
    main()