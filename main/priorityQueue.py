from maxHeap import buildMaxHeap, maxHeapSort, maxHeapify


class priorityQueue:
    ''''
    my implementation of a max priorityQueue
    '''

    def __init__(self, array, length):
        buildMaxHeap(array)
        self.queue = array
        self.length = length
        self.front = 0

    def parent(self, index):
        return index // 2 if index != 0 else IndexError

    def leftChild(self, index):
        return index * 2 if index < self.length else IndexError

    def rightChild(self, index):
        return index * 2 + 1 if index < self.length else IndexError

    def returnLength(self):
        return self.length

    def returnMax(self):
        return self.queue[0]

    def extractMax(self):
        self.queue[0], self.queue[self.length - 1] = self.queue[0], self.queue[self.length - 1]
        maxHeapify(self.queue, 0, self.length)
        return self.queue.pop()

    def increaseKey(self, i, key):
        self.queue[i] = key
        while (i > 0 and self.queue[i] > self.queue[self.parent(i)]):
            self.queue[i], self.queue[self.parent(i)] = self.queue[self.parent(i)], self.queue[i]
            i = self.parent(i)

    def decreaseKey(self, i, key):
        self.queue[i] = key
        while (self.leftChild(i) != None and self.queue[i] < self.queue[self.leftChild(i)]):
            self.queue[i], self.queue[self.leftChild(i)] = self.queue[self.leftChild(i)], self.queue[i]
            i = self.leftChild(i)
    
    def removeKey(self, i):
        self.decreaseKey(i, -1)
        self.queue.pop()
        self.length -= 1

    def heapInsert(self, value):
        self.length += 1
        self.queue.append(None)
        self.increaseKey(self.length, self.length - 1, value)