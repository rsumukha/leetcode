class Solution(object):
    def mctFromLeafValues(self, arr):
        #Greedy approach that finding the minimum element will result in optimal solution
        
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr[0]
        if len(arr) == 2:
            return arr[0]*arr[1]
        
        ans = 0
        while len(arr)>=2:
            print(arr)
            minidx = arr.index(min(arr))
            if minidx==0:
                nodetobuild = minidx+1
            elif minidx==len(arr)-1:
                nodetobuild = minidx -1
            else:
                nodetobuild = minidx-1 if arr[minidx+1]>=arr[minidx-1] else minidx+1
            ans += (arr[minidx] * arr[nodetobuild])
            print(ans)
            arr.pop(minidx)
        return ans
                
