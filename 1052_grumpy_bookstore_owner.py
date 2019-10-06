class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        alreadyhappy = 0
        
        for i in range(len(customers)):
            if not grumpy[i]:
                alreadyhappy+=customers[i]
                customers[i] = 0
        i, j = 1, X
        current=sum(customers[:X])
        max_happy=current
        
        while  j < len(customers):
            current = current - customers[i-1] + customers[j]
            max_happy = max(max_happy, current)
            i+=1
            j+=1

        return max_happy+alreadyhappy
