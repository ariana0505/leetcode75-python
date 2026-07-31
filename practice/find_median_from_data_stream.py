import heapq
class MedianFinder:
    def __init__(self):
        self.baja = []
        self.alta = []

    def findMedian(self):
        if len(self.baja) > len(self.alta):
            return -self.baja[0]
        else:
            return (-self.baja[0] + self.alta[0]) / 2
    def addNum(self,num):
        heapq.heappush(self.baja, -num)
        heapq.heappush(self.alta, -heapq.heappop(self.baja))
        if len(self.baja) < len(self.alta):
            heapq.heappush(self.baja, -heapq.heappop(self.alta))

calculo = MedianFinder()
calculo.addNum(2)
calculo.addNum(5)
calculo.addNum(8)
print(calculo.findMedian())