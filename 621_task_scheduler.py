import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not n:
            return len(tasks)
        ctr = collections.Counter(tasks)
        minvalue = min(ctr.values())
        heap =[i*-1 for i in ctr.values()]
        heapq.heapify(heap)
        
        cycles=0
        while heap:
            mycycle=[]
            for i in range(0, n+1):
                if len(heap)>0:
                    mycycle.append(heapq.heappop(heap))
                else:
                    break
            
            for item in mycycle:
                if item+1:
                    heapq.heappush(heap, item+1)
                    
            if heap:
                cycles += (n+1)
            else:
                cycles += len(mycycle)
        return cycles
        
        
        
            
        
