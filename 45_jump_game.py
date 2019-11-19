class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        max_jump_idx = 0
        minimum_steps = 0
        res = 0
        
        for i, jump in enumerate(nums[:-1]):
            max_jump_idx = max(max_jump_idx, i+jump)
            if i >= minimum_steps:
                minimum_steps = max_jump_idx
                res +=1
        return res 
            
    
    
    
    
    def bt(self, nums, seek, numsteps):
        if seek > len(nums)-1:
            return 
        if len(nums)-1 == seek:
            self.minsteps = min(self.minsteps, numsteps)
            return
        
        for step in range(nums[seek]):
                self.bt(nums, seek+step+1, numsteps+1)
        return
    
