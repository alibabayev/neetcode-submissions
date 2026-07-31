class MedianFinder:

    def __init__(self):
        self.small_heap = [] # max heap
        self.large_heap = [] # min heap
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -1 * num)

        while (self.large_heap and (-1 * self.small_heap[0]) > self.large_heap[0]) or len(self.small_heap) > len(self.large_heap) + 1:
            extra_val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, extra_val)
        
        
        if len(self.large_heap) > len(self.small_heap) + 1:
            extra_val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -1 * extra_val)

        # if self.large_heap and (-1 * self.small_heap[0]) > self.large_heap[0]:
        #     large_val = -1 * heapq.heappop(self.small_heap)
        #     heapq.heappush(self.large_heap, large_val)
        
        # if len(self.small_heap) > len(self.large_heap) + 1:
        #     # since values in small heap are negative versions of originals
        #     extra_val = -1 * heapq.heappop(self.small_heap)
        #     heapq.heappush(self.large_heap, extra_val)
        # elif len(self.large_heap) > len(self.small_heap) + 1:
        #     extra_val = heapq.heappop(self.large_heap)
        #     heapq.heappush(self.small_heap, -1 * extra_val)
        
        
        
        
        

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.large_heap):
            return -1 * self.small_heap[0]
        if len(self.small_heap) < len(self.large_heap):
            return self.large_heap[0]
        return (-1 * self.small_heap[0] + self.large_heap[0]) / 2

