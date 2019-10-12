class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #hashset and intelligent sequence building
        #check if the num is the starting of the sequence 
        # if it is then traverse through it to find the count
        # since it is already traversed, N-1 will be there in nums_set
        
        if nums == None:
            return None
        if len(nums)==0:
            return 0
        if len(nums) == 1:
            return 1
        
        numset = set(nums)
        maxlength = 0
        for num in numset:
            length = 0
            if num-1 not in numset:                
                while num in numset:
                    num=num+1
                    length +=1
            maxlength = max(maxlength, length)
        return maxlength
        
