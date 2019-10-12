class Solution(object):
    def longestCommonPrefix(self, strs):
        longestcommonprefix = ""
        if len(strs) == 0 or strs == None:
            return longestcommonprefix
        
        for i in range(0, len(strs[0])):
            for j in range(1, len(strs)):
                if i>=len(strs[j]) or strs[0][i] != strs[j][i]:
                    return longestcommonprefix
            longestcommonprefix += strs[0][i]
        return longestcommonprefix
        

