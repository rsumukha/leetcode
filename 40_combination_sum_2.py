class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        ans = []
        
        def dfs(index, array, tar):
            if tar == 0:
                ans.append(array)
                return
            if tar < 0:
                return
                
            for i in range(index, len(candidates)):
                if i>index and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, array+[candidates[i]], tar-candidates[i])
            
            
                    
                    
        dfs(0, [], target)
        return ans
                
            
        
