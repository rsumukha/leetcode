class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        
        for i, string in enumerate(strs):
            sort__="".join(sorted(string))
            if d.get(sort__, -1)==-1:
                d[sort__]=[]
                d[sort__].append(string)
            else:
                d[sort__].append(string)
        
        return d.values()
        