class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def delete(self, key):
        i = self.heap.index(key)
        self.increase_key(i, float('inf'))
        self.extract_max()

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.max_heapify(0)
        return root

    def max_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def increase_key(self, i, new_key):
        if new_key < self.heap[i]:
            return
        self.heap[i] = new_key
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heap_sort(self):
        n = len(self.heap)
        for i in range(n - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.max_heapify_subtree(0, i)
        return self.heap

    def max_heapify_subtree(self, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left

        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify_subtree(largest, n)


# Example usage:

heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(15)
heap.insert(40)
heap.insert(50)
heap.insert(100)

print("Heap elements after insertion:", heap.heap)

heap.delete(40)
print("Heap elements after deleting 40:", heap.heap)

sorted_elements = heap.heap_sort()
print("Sorted elements from the heap:", sorted_elements)
