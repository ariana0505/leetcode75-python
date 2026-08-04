import heapq
class MedianFinder:
    def __init__(self):
        self.bajo = []
        self.alto = []

    def addNum(self, nodo):
        heapq.heappush(self.bajo, -nodo)
        heapq.heappush(self.alto, -heapq.heappop(self.bajo))
        if len(self.bajo)< len(self.alto):
            heapq.heappush(self.bajo,-heapq.heappop(self.alto))
    def findMedian(self):
        if len(self.bajo) > len(self.alto):
            return -self.bajo[0]
        else:
            return (-self.bajo[0] + self.alto[0]) / 2