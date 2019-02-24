class Solution(object):
    def longestCommonPrefix(self, strs):
        string_=""
        try:
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                    if strs[0][i]!=strs[j][i]:
                        return string_
                string_=string_+strs[0][i]
            return string_
        except Exception as e:
            return string_

if __name__=="__main__":
    s=Solution()
    print(s.longestCommonPrefix(["aa","aaa","aab"]))

