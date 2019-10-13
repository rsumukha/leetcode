class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if len(cpdomains) ==0:
            return None
        ans = {}
        for domain in cpdomains:
            count, dom = domain.split(" ")
            prev, count = "", int(count)
            for each in reversed(dom.split(".")):
                newuri = " "+each+prev
                if ans.get(newuri, None):
                    ans[newuri]+=count
                else:
                    ans[newuri] = count
                prev="."+each+prev
        
        ret=[]
        for key, val in ans.items():
            ret.append(str(val)+""+key)
        return ret
