class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas)==0 or sum(gas)<sum(cost):
            return -1
        
        current_gas = 0
        total_gas = 0
        result =0
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]
            if current_gas < 0:             #if the gas is negative restart the car from next point
                result = i +1
                current_gas = 0
            
        return -1 if total_gas<0 else result
    
    def bruteforce(self, gas, cost):
        if len(gas) == 0:
            return -1
        
        for i in range(len(gas)):
            start = i
            if cost[i] <= gas[i]:                
                gasremaining = gas[i]
                loop = False
                while not loop and cost[start] <= gasremaining:
                    gasremaining -= cost[start]
                    start = (start+1) % len(gas)
                    gasremaining += gas[start]      
                    if start == i:
                        return i
        return -1

                
                    
                    
                    
