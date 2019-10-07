import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap)-k > 0:
            heapq.heappop(self.heap)
        
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap)==self.k:
            if val >= self.heap[0]:
                heapq.heappush(self.heap, val)
                heapq.heappop(self.heap)
        else:
            heapq.heappush(self.heap, val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
