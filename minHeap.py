def minHeapify(array: list, index: int, length: int):
  """
  Turns an almost heap into a min heap
  """
  leftChild = index * 2
  rightChild = index * 2 + 1
  # largest is the index of the min of the following set: {array[index], array[leftChild], array[rightChild]}
  largest = index
  if leftChild < length and array[index] > array[leftChild]:
      largest = leftChild
  if rightChild < length and array[largest] > array[rightChild]:
      largest = rightChild
  if largest != index:
      array[index], array[largest] = array[largest], array[index] 
      minHeapify(array, largest, length)  

def minHeapSort(array, size):
    for i in range(size - 1, 1, -1):
        array[1], array[i] = array[i], array[1]
        minHeapify(array, 1, size - 1)
