import heapq
class MedianFinder:
    def __init__(self):
        self.baja = []
        self.alta = []

    def addNumber(self,num):
        heapq.heappush(self.baja,-num)
        heapq.heappush(self.alta,-heapq.heappop(self.baja))
        if len(self.alta) > len(self.baja):
            heapq.heappush(self.baja, -heapq.heappop(self.alta))
    def findMedian(self):
        if len(self.baja) > len(self.alta):
            return -self.baja[0]
        else:
            return (-self.baja[0] + self.alta[0]) / 2

calculo = MedianFinder()
calculo.addNumber(4)
print(calculo.findMedian())
calculo.addNumber(5)
print(calculo.findMedian())