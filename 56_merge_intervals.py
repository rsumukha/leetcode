class Solution(object):
    def merge(self, intervals):
        if len(intervals)==0:
            return []
        if len(intervals)==1:
            return intervals
        
        ans =[]
        sortedi = sorted(intervals, key=lambda x:x[0])
        cur = sortedi[0]
        i=1
        while i < len(sortedi): 
            nxt = sortedi[i]
            if cur[1]>=nxt[0]:
                cur = [cur[0], nxt[1] if nxt[1]> cur[1] else cur[1] ]
                i+=1
            else:
                i+=1
                ans.append(cur)
                cur = nxt[:]
        ans.append(cur)
        return ans
        
