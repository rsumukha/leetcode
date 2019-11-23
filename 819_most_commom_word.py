class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        mydict = {}
        for word in re.findall(r'([a-zA-Z]+)', paragraph.lower()):
            if not word in banned:
                if word in mydict:
                    mydict[word] += 1
                else:
                    mydict[word] = 1
        # print(mydict)
        return max(mydict.keys(), key=lambda x : mydict[x] )
        
