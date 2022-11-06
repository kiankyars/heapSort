def maxHeapify(array: list, index: int, length: int):
  """
  Turns an almost heap into a max heap
  """
  leftChild = index * 2
  rightChild = index * 2 + 1
  #   largest is the index of the max of the following set: {array[index], array[leftChild], array[rightChild]}
  largest = index
  if leftChild < length and array[largest] < array[leftChild]:
      largest = leftChild
  if rightChild < length and array[largest] < array[rightChild]:
      largest = rightChild
  if largest != index:
      array[index], array[largest] = array[largest], array[index] 
      maxHeapify(array, largest, length)  


def buildMaxHeap(array: list, length: int):
    '''
    creates a max heap
    '''
    for i in range(length // 2, -1, -1):
        maxHeapify(array, i, length)


def maxHeapSort(array: list, length: int) -> list:
    '''
    sorts a max heap
    '''
    for i in range(length - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        length -= 1
        maxHeapify(array, 0, length)
    return array