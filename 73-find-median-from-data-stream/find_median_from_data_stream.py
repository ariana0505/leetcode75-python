import heapq

class MedianFinder:
    def __init__(self):
        self.baja = []
        self.alta = []
    def addNum(self, num:int):
        heapq.heappush(self.baja, -num) #todo numero agregado pasa a la baja
        heapq.heappush(self.alta,  -heapq.heappop(self.baja)) #el mayor de la baja se muda a la alta
        if len(self.alta) > len(self.baja): #si el total es impar, la mediana se mantiene en la baja
            heapq.heappush(self.baja, -heapq.heappop(self.alta))
    def findMedian(self):
        if len(self.baja)> len(self.alta):
            return -self.baja[0]
        return ((-self.baja[0] + self.alta[0])/ 2)


if __name__ == "__main__":
    # Ejemplo del enunciado
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # 1.5
    mf.addNum(3)
    print(mf.findMedian())  # 2.0

    # Traza del flujo 1, 5, 2, 4
    mf2 = MedianFinder()
    for num in [1, 5, 2, 4]:
        mf2.addNum(num)
        print(f"llega {num} -> mediana {mf2.findMedian()}")