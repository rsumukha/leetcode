class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        print(len(s))
        if len(s) == 0:
            return True
        if len(wordDict) == 0:
            return False

        special_case_ptr=-1

        wordSet = set(wordDict)
        ptr = 0
        match_ptr=-1
        for i in range(0, len(s)):


            word_to_search = s[ptr:i + 1]
            print(word_to_search)
            if word_to_search in wordSet:
                ptr = i + 1
                match_ptr = i+1
        print(match_ptr)
        if match_ptr == len(s):
            return True
        else:
            return False

if __name__=="__main__":
    s=Solution()
    print(s.wordBreak("aaaaaaa", ["aaaa","aaa"]))
    #"aaaaaaa"
    # print(s.wordBreak("leetcode", ["leet","code"]))

