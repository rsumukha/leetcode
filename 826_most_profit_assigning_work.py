class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        worker.sort()
        profit_to_difficulty = list(sorted(zip(difficulty, profit))) #zip sorts according to first value
        total_profit = 0
        jobnumber = 0
        bestfitjob=0
        for w in worker:
            
            while jobnumber < len(worker) and profit_to_difficulty[jobnumber][0] <= w: #to access zipO[idx][idxofval]
                bestfitjob = max(bestfitjob, profit_to_difficulty[jobnumber][1])
                jobnumber+=1
        
            total_profit += bestfitjob
        
        return total_profit
        
        
