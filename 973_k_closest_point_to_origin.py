import heapq
import math
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        res = []
        k=K
        for x,y in points:
            if k:
                heapq.heappush(heap, ((-1)*math.sqrt(x**2+y**2), [x,y])) 
                k-=1
            else:
                dist, _ = heap[0]
                newdist = -1 * math.sqrt(x**2 + y**2)
                if newdist > dist:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (newdist, [x, y]))
                           
        while K:
            _, p = heapq.heappop(heap)
            res.append(p)           
            K-=1
        return res
