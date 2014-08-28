class PriorityQueue:
    def __init__(self, elements=[]):
        i = len(elements) / 2

        self.size = len(elements)
        self.heap = [0] + elements[:]
       
        while (i > 0):
            self._decrease(i)
            i -= 1


    def _increase(self, i):
        while i/2 > 0:
            if self.heap[i] < self.heap[i/2]:
                self.heap[i], self.heap[i/2] = self.heap[i/2], self.heap[i]
            i /= 2

    def enqueue(self, element):
        self.heap.append(element)
        self.size += 1

        #Adjust the newly added node if nessary
        self._increase(self.size)

    def _decrease(self, i):
        while i*2 <= self.size:
            lowest = self._get_lowest(i)
            if self.heap[i] > self.heap[lowest]:
                self.heap[i], self.heap[lowest] = self.heap[lowest], self.heap[i]
            i = lowest

    def _get_lowest(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def dequeue(self):
        root = self.heap[1]

        #Set the last node as the root
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1

        #Readjust the priority of the root
        self._decrease(1)

        return root

    def readjust(self, element):
        self._increase(self.heap.index(element,1))

    def get(self, element):
        return self.heap[self.heap.index(element,1)]

    def contains(self, element):
        for e in self.heap[1:]:
            if e == element:
                return True
        return False